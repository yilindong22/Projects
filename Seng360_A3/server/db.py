from pymysql import connect
from config import *

class DB(object):

    def __init__(self):
        """init sql connect """

        # connect sql
        self.conn = connect(host=DB_HOST,
                            user = DB_USER,
                            password = DB_PASS,
                            database=DB_NAME,
                            autocommit=True,
                            port = DB_PORT)
        
        self.cursor = self.conn.cursor()

    def save_in (self,sql,val):
        # save the inforation into the database
        #SQL = "INSERT INTO users (id,name,password,nickname) VALUES (%s, %s,%s,%s)"
        #VAL = ("John", "Highway 21")
        self.cursor.execute(sql,val)
        print("successfully insert")
        return 0

    def delete(self,sql,val):
        # save the inforation into the database

        self.cursor.execute(sql,val)
        print("successfully deleted")
        return 0

    def get_one(self,sql):

        self.cursor.execute(sql)
        query_result = self.cursor.fetchone()

        if not query_result:
            return None
        # 
        fields = [field[0] for field in self.cursor.description]

        
        # 
        return_data = dict()
        for field,value in zip(fields,query_result):
            return_data[field] = value

        return return_data

    def close(self):

        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    db = DB()
    print(db.get_one("select * from users where user_name='emma'"))

