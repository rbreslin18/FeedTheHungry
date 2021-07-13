import mysql.connector
import sys
import datetime
import sqlite3

# create first connection with database !
connect = sqlite3.connect('database.db')

# create a cursor
cr = connect.cursor()

# create database tabel for user login
cr.execute("""CREATE TABLE IF NOT EXISTS logins
        (name TEXT,
        email TEXT,
        password TEXT)""")


class DataBase:

        
    
   
    # add user to database
    def add(name, email, password):
        with connect:
            cr.execute("INSERT INTO logins VALUES(?,?,?)",(name, email, password))
            connect.commit()
            print("user added !")
            
    def delete(name, email, password):
        with connect:
            sql = ("DELETE FROM logins WHERE email=?")
            cr.execute(sql, (email,))
       
            connect.commit()
               
          
            print("user deleted!")

    def read():
        with connect:
            cr.execute("SELECT * FROM logins")
            log = cr.fetchall()
            print(log)
            
    def validate(email, password):
        with connect:
            sql = ("DELETE FROM logins WHERE email=?")
            cr.execute(sql, (email,))
       
            if sql != -1:
                
                connect.commit()
            else:
                return False
  
            
    # read data from database        
    
