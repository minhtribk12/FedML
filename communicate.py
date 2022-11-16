import sys,os
import socket, time
import pandas as pd
from QCLDPC import Encode, Decode

# IP = socket.gethostbyname(socket.gethostname())
# PORT = 4455
# ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 20480

def send(file_path, file_name, ip, port):
    try:
        addr = (ip, port)

        """ Staring a TCP socket. """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        """ Connecting to the server. """
        client.connect(addr)

        """ Opening and reading the file data. """
        file = open(file_path + file_name, "rb")
        data = file.read()

        int_data = int.from_bytes(data, signed=False)

        ### ENCODE DATA ###
        # To do
        int_data = Encode(int_data)
        byte_data = int_data.to_bytes(int_data.bit_length(), signed=False)



        """ Sending the filename to the server. """
        client.send(file_name.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Sending the file data to the server. """

        client.send(byte_data)
        # client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        """ Closing the file. """
        file.close()

        """ Closing the connection from the server. """
        client.close()
        return True
    except Exception as e:
        print('Error during sending weight to client: {}'.format(e))
        time.sleep(1)
        return False

def open_socket(ip, port):
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    maddr = (ip, port)
    print(maddr)

    """ Bind the IP and PORT to the server. """
    recv_socket.bind(maddr)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    recv_socket.listen()
    print("[LISTENING] Server is listening.")
    return recv_socket

def client_receive(file_path, recv_socket, file_name):
    # ip = socket.gethostbyname(socket.gethostname()) 
    receive_flag = False
    while receive_flag == False:
        """ Server has accepted the connection from the client. """
        conn, addr = recv_socket.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(file_path + filename, "wb")
        conn.send("Filename received.".encode(FORMAT))

        """ Receiving the file data from the client. """
        data = conn.recv(SIZE)

        ### Decode ####
        int_data = int.from_bytes(data, signed=False)
        int_data = Decode (int_data)
        byte_data = int_data.to_bytes(int_data.bit_length(), signed=False)


        # data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(byte_data)
        conn.send("File data received".encode(FORMAT))

        """ Closing the file. """
        file.close()

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        if file_name == filename:
            receive_flag = True

def server_receive(file_path, recv_socket, num_client):
    # ip = socket.gethostbyname(socket.gethostname())
    count_client = 0
    while count_client < num_client:
        """ Server has accepted the connection from the client. """
        conn, addr = recv_socket.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(file_path + filename, "wb")
        conn.send("Filename received.".encode(FORMAT))

        """ Receiving the file data from the client. """
        data = conn.recv(SIZE)

        ### Decode ####
        int_data = int.from_bytes(data, signed=False)
        int_data = Decode (int_data)
        byte_data = int_data.to_bytes(int_data.bit_length(), signed=False)

        # data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(byte_data)
        conn.send("File data received".encode(FORMAT))

        """ Closing the file. """
        file.close()

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        count_client += 1

def write_weight_to_file(file_path, model, cl_id, comm_r,tr):
    file_name = 'weight_U'+str(cl_id)+'_'+str(comm_r)+'_'+str(tr)+'.h5'
    url = file_path + file_name
    model.save_weights(url)

def load_weight_from_file(file_path, model, cl_id,comm_r,tr):
    file_name = 'weight_U'+str(cl_id)+'_'+str(comm_r)+'_'+str(tr)+'.h5'
    url = file_path + file_name
    model.load_weights(url)
    return model

def select_sub(id):
    df_user = pd.read_csv('../data/dataset/Mixed_U'+str(id)+'_X.csv', keep_default_na=False)
    df_user_y = pd.read_csv('../data/dataset/Mixed_U'+str(id)+'_y.csv', keep_default_na=False)
    return df_user,df_user_y