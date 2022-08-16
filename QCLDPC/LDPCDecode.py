from tabnanny import check
import numpy as np
from util import zeros
import math

def LDPCDecode(Sign,row,col,block,H,sigma,IterNum):

    rows=row*block
    cols=col*block
    LLRsigma=sigma
    IterNumLen=len(IterNum)


    ErrDecode=zeros(1,IterNumLen)

    # channel initial LLR value
    LLRInitial=zeros(1,cols)
    for i in range(cols):
        LLRInitial[0,i]=2*Sign[0,i]/(LLRsigma^2)
    LLRQ=zeros(rows,cols);  
    LLRR=zeros(rows,cols);  
    for i in range(rows):
        for j in range(cols):
            if H[i,j] != 0:
                LLRQ[i,j] = LLRInitial(0,j)
    

    Outputdecode=zeros(1,cols)

    for iter in range(IterNumLen):
        for i in range(rows):
            for j in range(cols):
                if H[i,j] != 0:
                    LLRRPro = 1
                    for k in range(cols):
                        if (H[i,k] != 0) & (k != j):
                            LLRRPro=LLRRPro*math.tanh(LLRQ(i,k)/2); 

                    if LLRRPro != 0:
                        LLRR[i,j]=2*math.atan(LLRRPro)
                    else:
                        LLRR[i,j] = 0

        for i in range(cols):
            for j in range(rows):
                LLRMid = 0
                if H[j,i] != 0:
                    for k in range(rows):
                        if (k != j) & (H[k,i] != 0):
                            LLRMid = LLRR[k,i]+LLRMid
                    LLRQ[j,i] = LLRMid + LLRInitial[0,i]

        LQ = zeros(1,cols)

        for i in range(cols):
            LQMid = 0 
            for j in range(rows):
                LQMid = LLRR[j,i] + LQMid
            LQ[0,i] = LQMid + LLRInitial[0,i]

        decode=zeros(1,cols)
        for i in range(cols):
            if LQ(0,i) < 0:
                decode[0,i] = 1
        
        # check = []
        check = H*decode.T
        mark = 0
        for i in range(rows):
            if np.mod(check[i,0], 2) == 1:
            # if (check[i,0] % 2) == 1:
                mark = 1
                break
        if mark == 0:
            break

    return Outputdecode