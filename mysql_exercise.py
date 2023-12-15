import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="lalitha",
    password="12345678",
    database="todos"
)
mycursor = mydb.cursor()
# mycursor.execute("insert into task (chore) values  ('create query')")
# mydb.commit()
mycursor.execute("select * from task")
result = mycursor.fetchall()
for i in result:
    print(i)

# mycursor.execute(
#     "create table cafe_menu (menu_id int, menu_name varchar(100), price int)")
# mycursor.execute("insert into cafe_menu values (1,'idly', 5)")
# mycursor.execute("insert into cafe_menu values (2,'vada', 6)")
# mycursor.execute("insert into cafe_menu values (3,'tea', 10)")
# mydb.commit()
mycursor.execute("update cafe_menu set price = 3 where menu_id = 3 ")
mydb.commit()
mycursor.execute("select * from cafe_menu")
result = mycursor.fetchall()
for i in result:
    print(i)

mydb.close()
