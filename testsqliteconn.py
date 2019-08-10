import sqlite3
conn=sqlite3.connect("test.db")
cursor=conn.cursor()
# cursor.execute("create table user (id varchar(20) primary key, name varchar(50))")
cursor.execute("insert into user (id,name) values(\'3\',\'HUANG Youyue\')")
print(cursor.rowcount)
conn.commit()
cursor.execute("select * from user")
values=cursor.fetchall()
print(values)
cursor.close()
conn.close
print("Open database successfully.")