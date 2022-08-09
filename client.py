from tensorflow.keras.models import  model_from_json
import pandas as pd
import tensorflow as tf
import argparse
import time
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from sklearn.utils import shuffle  
from communicate import send, client_receive, open_socket,load_weight_from_file,write_weight_to_file,select_sub

comms_round=2
client_names=['1']

SERVER_IP = '10.100.7.1'
CLIENT_IP = '10.100.7.1'
SERVER_PORT = 4477

#Enable all GPUs

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)

def test_model(X_t, y_t, global_model):
    score = global_model.evaluate(X_t, y_t, verbose=0) 
    return score[0],score[1]

def retrain_model(c_id,model):
    
    X0,y0=select_sub(c_id)
    
    y0 = to_categorical(y0)
    # print(y0.shape)

    n_cols = X0.shape[1]
    model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy', 
    metrics=['accuracy'],
    )
    
    history = model.fit(X0,y0,epochs=40, shuffle=True ,verbose=False)
    print(history.history.keys())
    with open('./acc_loss/history.txt', 'w') as f:
        for item in history.history['accuracy']:
            f.write("%s\n" % item)
    return model

def load_model_from_json(file_path):
    json_file = open(file_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    return model_from_json(loaded_model_json)

    
def FedAvg(cl_id, client_port):
    # Training data
    X_t=pd.read_csv('../data/dataset/Mixed_Eval_X.csv')
    y_t=pd.read_csv('../data/dataset/Mixed_eval_y.csv', keep_default_na=False)
    X_t, y_t = shuffle(X_t, y_t, random_state=10)
    y_t = to_categorical(y_t)

    recv_socket = open_socket(CLIENT_IP, client_port)
    global_model = None
    client_receive('./client_'+str(cl_id)+'_model/', recv_socket, 'global_model.json')
    global_model = load_model_from_json('./client_'+str(cl_id)+'_model/global_model.json')

    for tr in range(2):   
        print('Trial N= '+ str(tr))
        for comm_round in range(comms_round):  
            if global_model != None:
                file_name = 'weight_U0_'+str(comm_round)+'_'+str(tr)+'.h5'
                client_receive('./client_'+str(cl_id)+'_folder/global_weight/', recv_socket, file_name)
                print(global_model.summary())
                #####################################################
                # Communicate to receive new global weights from server
                # After get global weight from server
                #####################################################
                # TO DO: Implement communication

                global_model = load_weight_from_file('./client_'+str(cl_id)+'_folder/global_weight/', global_model,0,comm_round,tr)
                print("retraining model")
                local_model = retrain_model(cl_id,global_model)
                write_weight_to_file('client_'+str(cl_id)+'_folder/local_weight/',local_model,cl_id,comm_round,tr)

                #####################################################
                # Communicate to send new weights to server
                # Send weight back to server
                #####################################################
                # TO DO: Implement communication
                
                send_flag = False
                while send_flag == False:
                    try:
                        send('./client_'+str(cl_id)+'_folder/local_weight/', 'weight_U'+str(cl_id)+'_'+str(comm_round)+'_'+str(tr)+'.h5',SERVER_IP, SERVER_PORT)
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