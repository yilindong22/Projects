from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from config import SERVER_IP
from config import SERVER_PORT

class ClientSocket(socket):

    def __init__(self):
        super(ClientSocket,self).__init__(AF_INET,SOCK_STREAM)

    #connect to the server
    def connect_server(self):
        self.connect((SERVER_IP,SERVER_PORT))
        self.setblocking(0)

    # recive the data
    def recv_data(self):
        return self.recv(512).decode("utf-8")

    #send the data
    def send_data(self,messages):
        self.send(messages.encode("utf-8"))

if __name__ == '__main__':
    cs = ClientSocket()
    cs.connect_server()