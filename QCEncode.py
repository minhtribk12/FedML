import numpy as np
from util import zero

def QCEncode(InputB,qcH,Hb):
    mb,nb = Hb.shape
    rqc,cqc = qcH.shape
    kb = nb-mb
    z = cqc/nb
    CheckB = np.zeros(mb*z,1)
    ZhInverse = np.zeros(z)
    ZhInverse = qcH[0:z-1,z*kb:z*kb+z-1] + qcH[z*5:z*5+z-1,z*kb:z*kb+z-1] + qcH[z*(mb-1):z*mb-1,z*kb:z*kb+z-1]
    ZhInverse = np.mod(ZhInverse,2)

    ZSum=np.zeros(z,1)
    for j in range(kb):
        ZMid = np.zeros(z,1)
        ZHb = np.zeros(z)
        for i in range(mb):
            if Hb[i,j] >= 0:
                ZHb = qcH[z*i:z*(i+1)-1,z*j:z*(j+1)-1]
                ZMid = ZMid + ZHb*InputB[z*j:z*(j+1)-1].T
        ZSum=ZMid+ZSum
    ZSum=np.mod(ZSum,2)
    CheckB[0:z,0]=np.mod(ZhInverse*ZSum,2)
    ZSum2=np.zeros(z,1)

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