import numpy as np
import math 
import matplotlib.pyplot as plt
from util import zeros
from QCEncode import QCEncode
from QCLDPCBaseH import QCLDPCBaseH
from LDPCDecode import LDPCDecode  

CodeLength=576
CodeRate=1/2
qcH,Hb=QCLDPCBaseH(CodeLength,CodeRate) #generate check matrix qcH
row,col=qcH.shape
rowb,colb=Hb.shape
block=CodeLength/colb

NewsLength = CodeRate*CodeLength #length of each weight to be encoded
print(' The unit message length is:'+ str(NewsLength))


# Function to clear the kth bit of n, k start from 1, ex: '10101' has k = 1 -> '10100' )
def clear_nBit(num, n):
    # num and n must be integer
    return (num >> n) << n


def Encode(InputData):
    #data to be encoded
    #change to model weights, each weight is (CodeLength*CodeRate) bits
    CodeNum=len(InputData) #number of weights

    #As the clear_nBit function needs interger input so here I change InputData to interger first. 
    #However, we also need to change the intermediate bits back. So maybe redefine a function with binary is better?
    #e.g. 0101110111 set least significant 5 bits to 0, get 0101100000. Encode this 0101100000 by QCEncode to get PerCode=0101100000XXXXXXXXXX.
    # But before through the channel, we need to change PerCode to 0101110111XXXXXXXXXX, change the first part back to original 0101110111.
    DataOri = np.fix(InputData*100000); #expand to integer
    Pn=10 # Set least significant Pn bit to 0
    DataPn = clear_nBit(DataOri, Pn) 

    for i in range(CodeNum) :
        PerData=zeros(1,NewsLength)
        PerData[i]=bin(DataPn[i])
    
        #partial encoding
        PerCode=zeros(1,CodeNum)
        PerCode[i]=QCEncode(PerData[i],qcH,Hb)
    
        #through the channel
        snr=2
        SNR=10^(snr/10)
        sigma=math.sqrt(1/(2*CodeRate*SNR))
        Noise=np.random.randn(PerCode.shape)*sigma
        ChannelNoise=(-(2*PerCode-1))+Noise
    return ChannelNoise

def bitExtracted(number, k, p):  
    return (((1 << k) - 1)  &  (number >> (p-1)))


def separate_encoded_data(encoded_data, CodeRate, CodeLength):
    num_1 = CodeRate*CodeLength
    num_2 = CodeLength - num_1
    Codeword1 = bitExtracted(encoded_data,num_1, num_2+1)
    Codeword2 = bitExtracted(encoded_data,num_2, 1)
    return Codeword1,Codeword2

def concat_binary(Codeword1,Codeword2, CodeRate, CodeLength):
    num_2 = CodeLength*(1-CodeRate)
    return Codeword1 << int(num_2) | Codeword2




def Decode(encoded_data):
    #data to be encoded
    #change to model weights, each weight is (CodeLength*CodeRate) bits
    CodeNum=len(encoded_data) #number of weights

    ITERNum=10 #Decoding iterations

    for i in range(CodeNum) :

        snr=2
        SNR=10^(snr/10)
        sigma=math.sqrt(1/(2*CodeRate*SNR))
        
        #BP decoding
        Codeword1,Codeword2 = separate_encoded_data(encoded_data)
        codeword1_tail = bitExtracted(Codeword1, 5, 1)
        Codeword1= clear_nBit(Codeword1,5) #change the least significant 5 bits of first part of OutputChannelOri to 0
        OutputDecode = concat_binary(Codeword1, Codeword2, CodeRate, CodeLength)
        BPOutputdecodeOri=LDPCDecode(OutputDecode,rowb,colb,block,qcH,sigma,ITERNum)
        BPOutputdecode = clear_nBit(BPOutputdecodeOri,5) | codeword1_tail #change the least significant 5 bits of first part of BPOutputdecodeOri to its noisy type

    return BPOutputdecode
