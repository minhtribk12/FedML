from multiprocessing.connection import Client
import numpy as np
import matplotlib.pyplot as plt
#import cv2
from math import pi
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Input, Convolution2D, ZeroPadding2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from PIL import Image
import numpy as np
#from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from os import walk
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM,Dropout,BatchNormalization,Masking,Embedding
from numpy import array
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from sklearn import preprocessing
from matplotlib import pyplot
import tensorflow as tf
# return training data
import scipy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import imageio as im
import os
import statsmodels.api as sm
from sklearn.neural_network import MLPRegressor,MLPClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
import pickle
import os, argparse
from numpy import loadtxt
import copy
import pickle
import numpy as np
from numpy.lib import math
from sklearn.linear_model import LinearRegression, SGDRegressor
from statsmodels.regression import linear_model
import copy
import os
import cv2,time
import numpy as np
from PIL import Image
import copy
from PIL import Image
import glob
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn import datasets, metrics
from sklearn.metrics import accuracy_score
import random
import sklearn
from tensorflow.keras import regularizers
from sklearn.preprocessing.data import StandardScaler
import tensorflow as tf
from sklearn.utils import shuffle
from sklearn.metrics import classification_report
import pandas as pd 
from sklearn.utils import shuffle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import scale
from tqdm import tqdm    
import copy
import torch
from torch import nn
from tensorflow.keras import backend
from tensorflow.keras.optimizers import SGD
from communicate import send, client_receive


comms_round=2
client_names=['1']


SERVER_IP = '10.100.7.1'
SERVER_PORT = 4455



#Enable all GPUs

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)

def test_model(X_t, y_t, global_model):
    score = global_model.evaluate(X_t, y_t, verbose=0) 
    return score[0],score[1]



def select_sub(id):
    print(id)
    df_user = pd.read_csv('../data/dataset/Mixed_U'+str(id)+'_X.csv', keep_default_na=False)
    df_user_y = pd.read_csv('../data/dataset/Mixed_U'+str(id)+'_y.csv', keep_default_na=False)

    return df_user,df_user_y

def build_global_model(avg,get_model):
    model = Sequential()
    
    model.add(Dense(30, input_dim=3, activation='relu'))
    model.add(Dense(12,activation='softmax'))

    model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy', 
    metrics=['accuracy'],
    )
    if(get_model==False):
        model.set_weights(avg)
   
    return model
    
def write_weight_to_file(w,cl_id,comm_r,tr):
    w_new=[]
    f=open('./local_weight/weight_U'+str(cl_id)+'_'+str(comm_r)+'_'+str(tr)+'.txt','w')
    for x in w[0]:
        for a in x:
            w_new.append(a)
            f.write(str(a))
            f.write('\n')
    for x in w[1]:
        w_new.append(x)
        f.write(str(x))
        f.write('\n')
    
    for x in w[2]:
        for a in x:
            w_new.append(a)
            f.write(str(a))
            f.write('\n')
            
    for x in w[3]:
        w_new.append(x)
        f.write(str(x))
        f.write('\n')
    f.close
  
def load_weight_from_file(cl_id,comm_r,tr):
    X0,y0=select_sub(1)
    n_cols = X0.shape[1]

    model = Sequential()
    
    model.add(Dense(30, input_dim=n_cols, activation='relu'))
    model.add(Dense(12,activation='softmax'))
 
    model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
    )
    
    w=model.get_weights()
    #return w

    w_new=[]
    
    f = open('./acc_loss/weight_U'+str(cl_id)+'_'+str(comm_r)+'_'+str(tr)+'.txt', "r")

    for x in f:
        w_new.append(float(x))
    f.close
    i=0
    j=0
    for x in w[0]:
        
        k=0
        for a in x:
            old=w[0][j][k]
            w[0][j][k]=(w_new[i])
            i=i+1
            k=k+1

        j=j+1
    k=0
    for x in w[1]:
        
        w[1][k]=w_new[i]
        k=k+1
        i=i+1

    j=0
    for x in w[2]:
        
        k=0
        for a in x:
            w[2][j][k]=w_new[i]
            k=k+1
            i=i+1
        j=j+1
    k=0
    for x in w[3]:
        
        w[3][k]=w_new[i]
        k=k+1
        i=i+1

    return w
    
    
def retrain_model(c_id,g_w,comm_r,tr):

    
    X0,y0=select_sub(c_id)
    
    y0 = to_categorical(y0)
    # print(y0.shape)

    n_cols = X0.shape[1]
    from tensorflow.keras.layers import BatchNormalization
    model = Sequential()
    
    model.add(Dense(30, input_dim=n_cols, activation='relu'))
    model.add(Dense(12,activation='softmax'))
    # print(model.summary())
    lr = 0.01
    optimizer = SGD(lr=lr, 
    decay=lr / comms_round, 
    momentum=0.9
    )
    model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy', 
    metrics=['accuracy'],
    )
    
    model.set_weights(g_w)
    model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy', 
    metrics=['accuracy'],
    )
    history =model.fit(X0,y0,epochs=40,    shuffle=True ,verbose=False)
    print(history.history.keys())
    with open('./acc_loss/history.txt', 'w') as f:
        for item in history.history['accuracy']:
            f.write("%s\n" % item)
    
    #return model.get_weights()
    write_weight_to_file(model.get_weights(),c_id,comm_r,tr)
    

    
    
def FedAvg(cl_id, client_port):

    # Training data
    X_t=pd.read_csv('../data/dataset/Mixed_Eval_X.csv')
    y_t=pd.read_csv('../data/dataset/Mixed_eval_y.csv', keep_default_na=False)
    X_t, y_t = shuffle(X_t, y_t, random_state=10)


    y_t = to_categorical(y_t)

    for tr in range(1,5):

        print('Trial N= '+ str(tr))
        for comm_round in range(comms_round):
            file_name = 'weight_U0_'+str(comm_round)+'_'+str(tr)+'.txt'

            client_receive('./global_weight/', client_port, file_name)
            #####################################################
            # Communicate to receive new global weights from server
            # After get global weight from server
            #####################################################
            # TO DO: Implement communication

            global_weights = load_weight_from_file(0,comm_round,tr)

            retrain_model(cl_id,global_weights,comm_round,tr)

            #####################################################
            # Communicate to send new weights to server
            # Send weight back to server
            #####################################################
            # TO DO: Implement communication
            
            send_flag = False
            while ~send_flag:
                try:
                    send('./local_weight/', 'weight_U'+str(cl_id)+'_'+str(comm_round)+'_'+str(tr)+'.txt',SERVER_IP, SERVER_PORT)
                    send_flag = True
                except Exception as e:
                    print('Error during sending weight to server: {}'.format(e))
                    time.sleep(1)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Client Training")
    parser.add_argument('--cl', help='Client ID', default=0)
    parser.add_argument('--port', help='Client reveiving port', default=4455)
    args = parser.parse_args()
    FedAvg(args.cl, int(args.port))
    sys.exit(main())  