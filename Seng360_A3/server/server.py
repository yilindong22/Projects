from threading import Thread
from server_socket import ServerSocket
from socket_wrapper import SocketWrapper
from db import DB
from config import *
from response_protocol import *
import random

class Server(object):

    def __init__(self):

        self.server_socket = ServerSocket()
        self.clients = dict()
        self.request_handle_functions = dict()
        self.register(REQUEST_LOGIN, lambda sf,data:self.request_login_handle(sf,data))
        self.register(REQUEST_CHAT,lambda sf,data:self.request_chat_handle(sf,data))
        self.register(REQUEST_SIGIN, lambda sf,data:self.request_sigin_handle(sf,data))
        self.register(REQUEST_DELETE, lambda sf,data:self.request_delete_handle(sf,data))

    # remove the offline users
    def remove_offline_user(self, client_sock): 
        username = None
        for uname, csock in self.clients.items():
            if csock['sock'].sock == client_sock.sock:
                username = uname
        del self.clients[username]

    def register(self, request_id, handle_function):

        self.request_handle_functions[request_id] = handle_function

    def startup(self):
        """start the server"""

        while True:
            sock,addr = self.server_socket.accept()
            client_sock = SocketWrapper(sock)
            Thread(target=lambda:self.request_handle(client_sock)).start()

    def request_handle(self, client_sock):
        ## handle the requests
        while True:
            request_text = client_sock.recv_data()
            if not request_text:
                print("OFF LINE!")
                self.remove_offline_user(client_sock)
                break
            # 
            request_data = self.parse_request_text(request_text)
            # 
            handle_function = self.request_handle_functions[request_data["request_id"]]
            if handle_function:
                handle_function(client_sock,request_data)

    ## handle sigin request 
    def request_sigin_handle(self,client_sock,request_data):
        username = request_data["username"]
        password = request_data["password"]
        ret1, nickname2, username3 = self.check_user_sign(username,password)
        if (ret1 != 1):
            ret, nickname, username = self.user_sinUp(username,password,username)
            if ret == "1":
                self.clients[username] = {'sock':client_sock,'nickname':nickname}
            response_text = ResponseProtocol.response_login_result(ret,nickname,username)
        # 
            client_sock.send_data(response_text)


    ## handle delete request 
    def request_delete_handle(self,client_sock,request_data):
        username = request_data["username"]
        password = request_data["password"]
        ret = self.delete(username,password)
        # 

    ## handle login request 
    def request_login_handle(self,client_sock,request_data):
        """"""

        # 
        username = request_data["username"]
        password = request_data["password"]

        # 
        ret, nickname, username = self.check_user_login(username,password)
        # 
        if ret == "1":
            self.clients[username] = {'sock':client_sock,'nickname':nickname}
        # 
        response_text = ResponseProtocol.response_login_result(ret,nickname,username)
        # 
        client_sock.send_data(response_text)

     ## check if the login inforamtion exists in the SQL database
    def check_user_login(self,username,password):
        """"""

        # 
        sql = "select * from users where user_name='" + username + "'"
        # 
        db_conn = DB()
        results = db_conn.get_one(sql)
        # 
        if not results:
            return "0","",username
        # 
        if results['user_password'] != password:
            return "0","",username

        return "1",results["user_nickname"],username

     ## check if the username has already been signed up
    def check_user_sign(self,username,password):
        """"""
        # 
        sql = "select * from users where user_name='" + username + "'"
        # 
        db_conn = DB()
        results = db_conn.get_one(sql)
        # 
        if not results:
            return "0","",username
        # 
        return "1",results["user_nickname"],username

     ## sign up the user
    def user_sinUp(self,username,password,nickname):
        SQL = "insert into users(user_id,user_name,user_password,user_nickname) values (%s, %s,%s,%s)"
        #VAL = ("John", "Highway 21")
        id = random.randint(0,2000)
        val = (str(id),username,password,username)
        db_conn = DB()
        results = db_conn.save_in(SQL,val)
        ret, nickname, username = self.check_user_login(username,password)
        return ret, nickname, username

    ## delete the user's information from database
    def delete(self,username,password):
        sql = "DELETE FROM users WHERE user_name = %s AND user_password = %s"
        val = (username,password)
        db_conn = DB()
        results = db_conn.delete(sql,val)
        return db_conn.cursor.rowcount



    ## handlke chatting request
    def request_chat_handle(self,client_sock,request_data):

        # 
        username = request_data["username"]
        messages = request_data["messages"]
        nickname = self.clients[username]["nickname"]

        # 
        response_text = ResponseProtocol.response_chat(nickname,messages)

        # 
        for uname,csock in self.clients.items():
            # 
            if uname == username:
                continue
            # 
            csock["sock"].send_data(response_text)

    @staticmethod
    def parse_request_text(request_text):
        """"""

        request_text_list = request_text.split(DELIMITER)
        # 
        request_data = dict()

        request_data['request_id'] = request_text_list[0]
        if request_text_list[0] == REQUEST_LOGIN:
            request_data['username'] = request_text_list[1]
            request_data['password'] = request_text_list[2]

        if request_text_list[0] == REQUEST_CHAT:
            request_data['username'] = request_text_list[1]
            request_data['messages'] = request_text_list[2]
        
        if request_text_list[0] == REQUEST_SIGIN:
            request_data['username'] = request_text_list[1]
            request_data['password'] = request_text_list[2]

        if request_text_list[0] == REQUEST_DELETE:
            request_data['username'] = request_text_list[1]
            request_data['password'] = request_text_list[2]
        
        return request_data


if __name__ == "__main__":
    server = Server()
    server.startup()