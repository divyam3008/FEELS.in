import mysql.connector as msc #pip install mysql_connector_python
db1 = msc.connect(host = "localhost" , username = "root" , password = "Divyamdj7" , database = "world")
print(db1)
# for i in db1: # will throw error as db1 is not an iterable , eventhough it is lazy evaluated object
#     print(i)
# print(db1.__dict__) # .__dict__ is a method that returns a dictionary for any given class , function , lazy evaluated object (LEO)
#                     # and this dictionary contains all the attributes of the LEO as keys and their values
# print(db1._user)
# print(db1._password)

cursor1 = db1.cursor()
cursor1.execute("show tables;")
t = cursor1.fetchall()
print(t)

cursor1.execute("select * from country ;")
print(cursor1.fetchone())
for i in cursor1:
    print(i)
