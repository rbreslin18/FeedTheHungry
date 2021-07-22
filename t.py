import mysql.connector
import sys
import datetime
import sqlite3
from kivy.uix.boxlayout import BoxLayout
# create first connection with database !
connect = sqlite3.connect('databases.db')

# create a cursor
cr = connect.cursor()

# create database table for user login
cr.execute("""CREATE TABLE IF NOT EXISTS users
        (name TEXT,
        email TEXT,
        password TEXT)""")


class DataBase:

    
    
   
    # add user to database
    def add(name, email, password):
        with connect:
            cr.execute("INSERT INTO users VALUES(?,?,?)",(name, email, password))
            connect.commit()
            print("user added !")
            
    def delete(name, email, password):
        with connect:
            sql = ("DELETE FROM users WHERE email=?")
            cr.execute(sql, (email,))
       
            connect.commit()
               
          
            print("user deleted!")
            
    # read data from database
    
    def read():
        with connect:
            cr.execute("SELECT * FROM users")
            log = cr.fetchall()
            print(log)
            
