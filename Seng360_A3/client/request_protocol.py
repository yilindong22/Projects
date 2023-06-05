from config import *


class RequestProtocol(object):
    ''''''

    @staticmethod
    def request_login(username, password):
        """
  
        """
        return DELIMITER.join([REQUEST_LOGIN,username,password])

    @staticmethod
    def request_chat(username,message):
        """
    
        """
        return DELIMITER.join([REQUEST_CHAT,username,message])

    @staticmethod
    def request_sign(username,message):
        """

        """
        return DELIMITER.join([REQUEST_SIGIN,username,message])

    
    @staticmethod
    def request_delete(username,message):
        """

        """
        return DELIMITER.join([REQUEST_DELETE,username,message])

    