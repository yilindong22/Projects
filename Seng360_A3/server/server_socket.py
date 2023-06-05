from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from config import SERVER_IP,SERVER_PORT

class ServerSocket(socket):

    def __init__(self):
        super(ServerSocket,self).__init__(AF_INET,SOCK_STREAM)

        self.bind((SERVER_IP,SERVER_PORT))
        # bind ip address and port

        self.listen(128)
        #max number listen

if __name__ == '__main__':
    server = ServerSocket()
    