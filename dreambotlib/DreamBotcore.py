# DreamBot Core
import hashlib
import pymysql
import json
import time
import uuid


def hashmd5(data):
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()


class DbotCore:
    def __init__(self, logger, DataBase_Server, DataBase_UserName, DataBase_Port, DataBase_PassWord, DataBase_DBName):
        self.DB_info = {
            "server": DataBase_Server,
            "username": DataBase_UserName,
            "port": DataBase_Port,
            "password": DataBase_PassWord,
            "dbname": DataBase_DBName
        }
        self.logger = logger

    def base_connectmysql(self, Log_Prefix):
        self.logger.debug("%s A new Client init operation " % (Log_Prefix,))
        try:
            self.logger.debug("%s Connect To DATABASE ....." % (Log_Prefix,))
            connection = pymysql.connect(host=self.DB_info['server'],
                                         user=self.DB_info["username"],
                                         password=self.DB_info["password"],
                                         port=self.DB_info["port"],
                                         database=self.DB_info["dbname"])
            self.logger.debug(
                "%s  Connected... \n \t Getting cursor..." % (Log_Prefix,))
            cursor = connection.cursor()
            self.logger.debug("%s Getted ..." % (Log_Prefix,))
            return {"status": True,
                    "cursor": cursor,
                    "connection": connection}
        except Exception as e:
            # 数据库连接错误
            self.logger.error(
                "%s Cannot connect to this database " % (Log_Prefix,))
            self.logger.error("%s Error information :%s" % (Log_Prefix, e,))
            self.logger.debug("%s Operation Failed !" % (Log_Prefix,))
            return {"status": False,
                    }

    def WebUI_Login_Update_Token(self, cursor, connection, user_id, username):
        token_data = uuid.uuid5(uuid.NAMESPACE_DNS, "%s%s" %
                                (username, time.time()))
        try:
            cursor.execute("UPDATE `DreamBot`.`User` SET `token`='%s' WHERE  `id`=%s;" % (
                token_data, user_id))
            connection.commit()
            return token_data
        except:
            connection.rollback()
            return None

    def WebUI_Login(self, username, password):
        cursor_dict = self.base_connectmysql("[ZHSZ_init]")
        if cursor_dict["status"]:
            cursor = cursor_dict["cursor"]
            connection = cursor_dict["connection"]
        else:
            return {
                "status": False,
                "errcode": 1
            }
        sql = "SELECT `id`,`username`,`password`,`token` FROM `User` WHERE `username`='%s';"(
            username,)
        count = cursor.execute(sql)
        if count == 1:
            user_information = cursor.fetchall()
            if user_information[2] == hashmd5(password):
                # 登录成功
                user_id = user_information[0]
                Token_data = self.WebUI_Login_Update_Token(
                    cursor, connection, user_id, username)
                if not Token_data == None:
                    return {
                        "status": True,
                        "errcode": 0,
                        "token": Token_data
                    }
                else:
                    # 获取Token失败
                    return {
                        "status": False,
                        "errcode": 2,
                        "token": None
                    }
            else:
                # 登录失败
                return {
                    "status": False,
                    "errcode": 3,
                    "token": None
                }


