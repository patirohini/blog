from flask import Flask
import mysql.connector.connect(host='localhost',user='root',password='system',db='blog')
with mysql.connector.connect(host='localhost',user='root',password='system',db='blog'):
    cursor=mydb.cursor(buffered=True)
    cursor.execute("create table if not exists registration(username varchar(30) primary key,mobile varchar(20) unique,address varchar(50),email varchar(30) unique,password varchar(20))")
app=Flask(__name__)
@app.route('/')
def home():
    return "Homepage of blog"
@app.route('/reg')
app.run(debug=True)
