from config import *

class ResponseProtocol(object):
    #server response the protocol

    @staticmethod
    ## parameter :
    # result: 0 means failed 1 means successed 
    # nickname: 
    # username:               
    def response_login_result(result,nickname,username):
        return DELIMITER.join([RESPONSE_LOGIN_RESULT,result,nickname,username])

    @staticmethod
    def response_chat(nickname,messages):

        return DELIMITER.join([RESPONSE_CHAT,nickname,messages])