from pymysql import connect

connection = connect(host=$(HOST),user=$(USER),passwd=$(PASS),db=$("el_salvador"))

cursor = connection.cursor()

cursor.close()
connection.close()
