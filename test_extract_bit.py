import numpy as np 
from util import zero
def convert_int_to_np(number):
    bin_num = str('{:032b}'.format(number))
    bin_num = (",".join(bin_num))
    return np.fromstring(bin_num, dtype=int, sep=',')

def QCEncode(InputB,qcH,Hb):
    mb,nb = Hb.shape
    rqc,cqc = qcH.shape
    kb = nb-mb
    z = int(cqc/nb)
    CheckB = np.zeros([mb*z,1])
    ZhInverse = np.zeros(z)
    ZhInverse = qcH[0:z,z*kb:z*kb+z] + qcH[z*5:z*5+z,z*kb:z*kb+z] + qcH[z*(mb-1):z*mb,z*kb:z*kb+z]
    ZhInverse = np.mod(ZhInverse,2)


    ZSum=np.zeros([z,1])
    for j in range(kb):
        ZMid = np.zeros([z,1])
        ZHb = np.zeros(z)
        for i in range(mb):
            if Hb[i,j] >= 0:
                ZHb = qcH[z*i:z*(i+1),z*j:z*(j+1)]
                ZMid=ZMid+ZHb*InputB[z*(j):z*(j+1)].T
        print("1 ZSum shape: ", ZSum.shape)
        ZSum=ZMid+ZSum
        print("2 ZSum shape: ", ZSum.shape)
    ZSum=np.mod(ZSum,2)
    print("ZhInverse shape: ", ZhInverse.shape)
    print("ZSum shape: ", ZSum.shape)
    print("np.mod(ZhInverse*ZSum,2) shape: ", np.mod(ZhInverse*ZSum,2).shape)
    CheckB[0:z,0]=np.mod(ZhInverse*ZSum,2)
    ZSum2=np.zeros([z,1])

    for k in range(kb):
        if Hb[0,k] >= 0:
            ZSum2 = ZSum2 + qcH[0:z-1,z*k:z*(k+1)-1]*InputB[0,z*k:z*(k+1)-1].T

    CheckB[z:2*z-1,0] = np.mod(ZSum2+qcH[0:z-1,z*kb:z*(kb+1)-1]*CheckB[0:z-1,0],2)

    for m in range(2,mb):
        ZSumR=np.zeros(z,1)
        if m != 6:
            for k in range(kb):
                if Hb(m-1,k) >= 0:
                    ZSumR=ZSumR+qcH[z*(m-2):z*(m-1)-1,z*(k-1):z*k-1]*InputB[0,z*(k-1):z*k-1].T

            CheckB[z*(m-1):z*m-1,0]=CheckB[z*(m-2):z*(m-1)-1,0]+ZSumR
        else:
            for k in range(kb):
                if Hb[m-1,k] >= 0:
                    ZSumR=ZSumR+qcH[z*(m-2):z*(m-1)-1,z*(k-1):z*k-1]*InputB[0,z*(k-1):z*k-1].T

            CheckB[6*z:7*z-1,0]=CheckB[5*z:6*z-1,0]+ZSumR+qcH[5*z:6*z-1,z*kb:z*(kb+1)-1]*CheckB[0:z-1,0]


    CheckB=np.mod(CheckB,2)
    QCCode=(InputB,CheckB.T)
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
InputB = np.array(list(map(convert_int_to_np,np_input))).flatten()

qcH, Hb = QCLDPCBaseH(Nbit, Rate)


result = QCEncode(InputB, qcH, Hb)
print(result)
