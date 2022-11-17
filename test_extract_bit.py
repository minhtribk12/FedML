import numpy as np 
from util import zero
def convert_int_to_np(number):
    bin_num = str('{:032b}'.format(number))
    bin_num = (",".join(bin_num))
    return np.fromstring(bin_num, dtype=int, sep=',')

def QCEncode(InputB,qcH,Hb):
    mb,nb = Hb.shape
    rqc,cqc = qcH.shape
    #print("qcH shape: ", qcH.shape)
    kb = nb-mb
    z = int(cqc/nb)
    CheckB = np.zeros([mb*z,1])
    #print("CheckB type: ", type(CheckB))
    #print("CheckB shape: ", CheckB.shape)
    ZhInverse = np.zeros(z)
    ZhInverse = qcH[0:z,z*kb:z*kb+z] + qcH[z*5:z*5+z,z*kb:z*kb+z] + qcH[z*(mb-1):z*mb,z*kb:z*kb+z]
    ZhInverse = np.mod(ZhInverse,2)


    ZSum=np.zeros([z,1])
    for j in range(kb):
        ZMid = np.zeros([z,1])
        print("ZMid0 type: ", type(ZMid))
        print("ZMid0 shape: ", ZMid.shape)
        print(ZMid)
        ZHb = np.zeros(z)
        for i in range(mb):
            if Hb[i,j] >= 0:
                ZHb = qcH[z*i:z*(i+1),z*j:z*(j+1)]
                print("ZHb shape: ", ZHb.shape)#24*24
                print("InputB shape: ", InputB.shape)#(1, 288)
                print(z*(j))
                print(z*(j+1))
                XX=InputB[:,z*(j):z*(j+1)]
                #print(XX)
                #print("ZHb type: ", type(ZHb))
                #print("XX type: ", type(XX))
                print("XX shape: ", XX.shape)
                #XX=np.mat(InputB[z*(j):z*(j+1)]).T #XX:24*1
                ZMid=ZMid+np.dot(ZHb,XX.T) #matrix multiply
                
                print("ZMid shape: ", ZMid.shape)
        #print("1 ZSum shape: ", ZSum.shape)
        ZSum=ZMid+ZSum  #ZMid:24*1  ZSum:24*1
        #print("2 ZSum shape: ", ZSum.shape)
    ZSum=np.mod(ZSum,2)
    #print("ZhInverse shape: ", ZhInverse.shape)
    #print("ZSum shape: ", ZSum.shape)
    #print("np.mod(ZhInverse*ZSum,2) shape: ", np.mod(ZhInverse*ZSum,2).shape)
    
    CheckB[0:z]=np.mod(np.dot(ZhInverse,ZSum),2)
    ZSum2=np.zeros([z,1])
    #print("ZSum2 shape: ", ZSum2.shape)
    
    for k in range(kb):
        if Hb[0,k] >= 0:
            #print("qcH[0:z,z*k:z*(k+1)] shape: ", qcH[0:z,z*k:z*(k+1)].shape)
            #print("InputB[z*k:z*(k+1)] shape: ", InputB[z*k:z*(k+1)].shape)
            ZSum2 = ZSum2 + np.dot(qcH[0:z,z*k:z*(k+1)],InputB[:,z*k:z*(k+1)].T)
            #print("ZSum2 shape: ", ZSum2.shape)

    CheckB[z:2*z] = np.mod(ZSum2+np.dot(qcH[0:z,z*kb:z*(kb+1)],CheckB[0:z]),2)

    for m in range(2,mb):
        ZSumR=np.zeros([z,1])
        if m != 6:
            for k in range(kb):
                if Hb[m-1,k] >= 0:
                    #print("qcH[z*(m-2):z*(m-1),z*(k-1):z*k]", qcH[z*(m-2):z*(m-1),z*(k-1):z*k].shape)
                    #print("InputB[0,z*(k-1):z*k] ", InputB[0,z*(k-1):z*k].shape)
                    ZSumR=ZSumR+np.dot(qcH[z*(m-2):z*(m-1),z*(k-1):z*k],InputB[:,z*(k-1):z*k].T)

            CheckB[z*(m-1):z*m]=CheckB[z*(m-2):z*(m-1)]+ZSumR
        else:
            for k in range(kb):
                if Hb[m-1,k] >= 0:
                    ZSumR=ZSumR+np.dot(qcH[z*(m-2):z*(m-1),z*(k-1):z*k],InputB[:,z*(k-1):z*k].T)

            CheckB[6*z:7*z]=CheckB[5*z:6*z]+ZSumR+np.dot(qcH[5*z:6*z,z*kb:z*(kb+1)],CheckB[0:z])


    CheckB=np.mod(CheckB,2)
    print("CheckB shape", CheckB.shape)
    print("InputB shape", InputB.shape)
    QCCode=np.hstack((InputB,CheckB.T))
    return QCCode

def QCLDPCBaseH(Nbit,Rate):
    nb = 24
    z = int(Nbit/nb)
    mb = int(nb-nb*Rate)
    #kb = nb-mb            
    Hz = np.zeros((z,z)) 
    SubH = np.zeros((z,z))
    Hb = np.array([
        [-1, 94, 73, -1, -1, -1, -1, -1, 55, 83, -1, -1, 7, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 27, -1, -1, -1, 22, 79, 9, -1, -1, -1, 12, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 24, 22, 81, -1, 33, -1, -1, -1, 0, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
        [61, -1, 47, -1, -1, -1, -1, -1, 65, 25, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 39, -1, -1, -1, 84, -1, -1, 41, 72, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 46, 40, -1, 82, -1, -1, -1, 79, 0, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1],
        [-1, -1, 95, 53, -1, -1, -1, -1, -1, 14, 18, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1],
        [-1, 11, 73, -1, -1, -1, 2, -1, -1, 47, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1],
        [12, -1, -1, -1, 83, 24, -1, 43, -1, -1, -1, 51, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1],
        [-1, -1, -1, -1, -1, 94, -1, 59, -1, -1, 70, 72, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1],
        [-1, -1, 7, 65, -1, -1, -1, -1, 39, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0],
        [43, -1, -1, -1, -1, 66, -1, 41, -1, -1, -1, 26, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]
    ])
    HbNew=np.zeros(Hb.shape)

    for i in range(mb):
        for j in range(nb):
            if Hb[i,j] < 0:
                Hz = np.zeros((z,z))
            elif Hb[i,j] == 0:
                Hz = np.identity(z)
            else:
                HbNew[i,j]= np.floor(Hb[i,j]*z/96)
                #Hz = np.roll(np.identity(z), (0,int(HbNew[i,j])), axis=(0,1))
                Hz = np.roll(np.identity(z), int(HbNew[i,j]), axis=1)
                
            if j == 0:
                SubH = Hz
            else:
                #SubH = np.concatenate((SubH,Hz),axis = 1)
                SubH = np.concatenate((SubH,Hz),axis = 1)
        
        if i == 0:
            qcH=SubH
        else:
            qcH = np.concatenate((qcH,SubH), axis = 0)

    return qcH,Hb

Nbit = 576
Rate = 0.5
np_input = np.array([6435,324,54534,342,23423,5356,2342,23425,6564])
#print("np_input type", type(np_input))
#print("np_input shape", np_input.shape)
#print(np_input)
InputB = np.array(list(map(convert_int_to_np,np_input)))
print("InputB00 shape", InputB.shape) 
InputB = np.array(list(map(convert_int_to_np,np_input))).flatten()
print("InputB0 shape", InputB.shape) #(288,)
InputB=InputB.reshape(-1,1)
print("InputB shape", InputB.shape)#(288,1)
InputB=InputB.T
print("InputBT shape", InputB.shape)
#print("InputB type", type(InputB))
#print("InputB shape", InputB.shape)
#print(InputB)
qcH, Hb = QCLDPCBaseH(Nbit, Rate)


result = QCEncode(InputB, qcH, Hb)
print("InputB:",InputB)
print("InputB shape", InputB.shape)
print("result:",result)