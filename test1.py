#import math

#import matplotlib.pyplot as plt
import numpy as np
#from LDPCDecode import LDPCDecode
#from QCEncode import QCEncode
#from QCLDPCBaseH import QCLDPCBaseH
#from util import zero
#from QCLDPC import clear_nBit
#file = open('./acc_loss/weight_U0_0_1.txt', "rb")
#data = file.read()
#print(data)
#int_data = int.from_bytes(data, byteorder='big', signed=False)
#print(int_data)

file = open('./client_1_folder/local_weight/weight_U1_0_1.h5', "rb")
data = file.read()
int_data = int.from_bytes(data, byteorder='big', signed=False)
print(int_data)
#can't distinguish each data

# def clear_nBit(num, n):
#     # num and n must be integer
#     return (num >> n) << n
  
# num=88888888
# print(bin(num))
# n=5
# num=clear_nBit(num, n)
# print(num)
# print(bin(num))

#A=bin(59431876531254967685342)
#30b1100100101011100111011111000101101011001100101100111000111000101000011011110
#Input= np.array([0.985,0.556])
#InputA=Input*10
#print(InputA)
#CodeNum=len(InputData) #number of weights

    #As the clear_nBit function needs interger input so here I change InputData to interger first. 
    #However, we also need to change the intermediate bits back. So maybe redefine a function with binary is better?
    #e.g. 0101110111 set least significant 5 bits to 0, get 0101100000. Encode this 0101100000 by QCEncode to get PerCode=0101100000XXXXXXXXXX.
    # But before through the channel, we need to change PerCode to 0101110111XXXXXXXXXX, change the first part back to original 0101110111.
#Data = np.trunc(Input*1000).astype(int) #expand to integer
#CodeNum=len(Input)
#print(CodeNum)
#for i in range(CodeNum):
 # print(i)
  #PerData=np.trunc(np.zeros(5)).astype(int) 
  #print(PerData)
  #PerData[i]=bin(Data[i])
  #PerData[i]=Data[i]
  #print(PerData)

#DataPn = clear_nBit(DataOri, 10) 
#print(Data)
#print(PerData)