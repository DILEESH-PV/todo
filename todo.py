import requests
import json
import mysql.connector

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='tododb')
except mysql.connector.Error as e:
    print("db connection error")
    
    
mycursor=mydb.cursor()

data=requests.get("https://jsonplaceholder.typicode.com/todos").text

data_info=json.loads(data)
for i in data_info:
    if(i['completed']==False):
        id=str(i['userId'])
        cmpt=str(i['completed'])
        sql="INSERT INTO `todo`(`userid`, `title`, `completed`) VALUES ('"+id+"','"+i['title']+"','"+cmpt+"')"
        mycursor.execute(sql)
        mydb.commit()
        print("data inserted successfully",id)
    