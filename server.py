import pandas as pd
import tensorflow as tf
import numpy as np
import time, json, argparse
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import tensorflow as tf  
from sklearn.utils import shuffle 
from communicate import send, server_receive, open_socket,load_weight_from_file,write_weight_to_file

SERVER_IP = '127.0.0.1'
SERVER_PORT = 4477

comms_round=2
CLIENT_NAMES=['1','2']

CLIENT_IP = ['127.0.0.1', '127.0.0.1']
CLIENT_PORT = [4455,4466]

#Enable all GPUs
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)

def test_model(X_t, y_t, global_model):
    score = global_model.evaluate(X_t, y_t, verbose=0) 
    return score[0],score[1]

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
    
  


def broadcast_file(file_path, file_name, client_ips, client_ports, client_names):
    send_flag = False
    while send_flag == False:
        tolerance = 3
        for i in range(len(client_names)):
            flag_i = False
            tol_count = 0
            while flag_i == False:
                flag_i = send(file_path, file_name,client_ips[i], client_ports[i])
                flag_i = True
                if flag_i == False:
                    print('Error during sending file to client {}'.format(i))
                    tol_count += 1
                    time.sleep(1)
                    if tol_count == tolerance:
                        break
        send_flag = True
   
def FedAvg(server_ip=SERVER_IP, server_port=SERVER_PORT, client_ips=CLIENT_IP, client_ports=CLIENT_PORT, client_names= CLIENT_NAMES):

    # Training data
    X_t=pd.read_csv('../data/dataset/Mixed_Eval_X.csv')
    y_t=pd.read_csv('../data/dataset/Mixed_eval_y.csv', keep_default_na=False)
    X_t, y_t = shuffle(X_t, y_t, random_state=10)
    y_t = to_categorical(y_t)
    recv_socket = open_socket(server_ip, server_port)

    acc_arr=[]
    loss_arr=[]
    global_model=build_global_model(0,True)
    score=global_model.evaluate(X_t,y_t)
    print(score)
    
    model_json = global_model.to_json()
    with open("./server_model/global_model.json", "w") as json_file:
        json_file.write(model_json)
    broadcast_file('./server_model/','global_model.json', client_ips, client_ports, client_names)

    for tr in range(2):

        print('Trial N= '+ str(tr))
        for comm_round in range(comms_round+1):

            if comm_round == 0:
                average_weights = global_model.get_weights()    
            else:
                #get weights 
                s_weights = list()
                #####################################################
                # Communicate to receive new weights from clients
                # After get weight from clients
                #####################################################
                # TO DO: Implement communication
                server_receive('./server_folder/local_weight/', recv_socket, len(client_names))

                #For each client
                for client in client_names:

                    client_model_w=load_weight_from_file('./server_folder/local_weight/',global_model, client,comm_round-1,tr).get_weights()
                    s_weights.append(client_model_w)
                average_weights = np.mean(s_weights, axis=0)
                global_model.set_weights(average_weights)
            write_weight_to_file('./server_folder/global_weight/',global_model,0,comm_round,tr)

            #####################################################
            # Communicate to send new weights to clients
            # Send weight back to client
            #####################################################
            # TO DO: Implement communication

            if comm_round < comms_round:
                broadcast_file('./server_folder/global_weight/','weight_U0_'+str(comm_round)+'_'+str(tr)+'.h5', client_ips, client_ports, client_names)    

            global_acc, global_loss = test_model(X_t, y_t, global_model)
            acc_arr.append(global_acc)
            loss_arr.append(global_loss)
            print('---------')
            print(global_acc,global_loss)
            
            with open('./acc_loss/history.txt', 'w') as f:
                for item in acc_arr:
                    f.write("%s\n" % item)
                
            with open('./acc_loss/history.txt', 'w') as f:
                for item in loss_arr:
                    f.write("%s\n" % item)     
            f.close()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Federated Learning Server")
    parser.add_argument('--sc', help='Server Configuration File', default='./server_conf.json')
    args = parser.parse_args()
    server_config = json.load(open(args.sc))
    FedAvg(server_config['server']['ip'], server_config['server']['port'], server_config['client']['ip'], server_config['client']['port'],server_config['client']['name']) 