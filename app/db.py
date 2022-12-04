import os
from pymysql import connect

host = os.environ["HOST"]
user = os.environ["USER"]
passwd = os.environ["PASS"]

connection = connect(host=host,
                     user=user,
                     passwd=passwd,
                     db="el_salvador")

cursor = connection.cursor()

cursor.close()
connection.close()
