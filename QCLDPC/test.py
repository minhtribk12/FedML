import numpy as np
#import math 
#from QCLDPC import clear_nBit

#CodeLength=8
#CodeRate=1/2
#NewsLength = int(CodeRate*CodeLength) 
#Input=np.random.random_integers(2, size=(1,2*NewsLength))-1
#Code=np.trunc(Input*100000).astype(int)
#DataPn = clear_nBit(Code, 2) 
#print(DataPn)

nb = 24
z = 24
mb = 12
#kb = nb-mb            
#Hz = np.zeros((z,z)) 
#SubH = np.zeros((z,z)) 
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
#HbNew=np.zeros(Hb.shape)
#i=0
#j=0
#if Hb[i,j] < 0:
   # Hz = np.zeros((z,z)) 
#elif Hb[i,j] == 0:
#Hz = np.identity(z)
#else:
#        HbNew[i,j]= np.floor(Hb[i,j]*z/96)
        #Hz = np.roll(np.identity(z), (0,int(HbNew[i,j])), axis=(0,1))
Hz = np.roll(np.identity(24), 1, axis=1)
                
#if j == 0:
#         SubH = Hz
#else:
 #       #SubH = np.concatenate((SubH,Hz),axis = 1)
 #       SubH = np.concatenate((SubH,Hz),axis = 1)
        
print(Hz)        
#print(SubH)