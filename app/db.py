from pymysql import connect

connection = connect(host=$(),user=$(),passwd=$(),db=$())

cursor = connection.cursor()

cursor.close()
connection.close()
