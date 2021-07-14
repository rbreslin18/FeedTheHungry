#db1.py
import sys
import datetime
import sqlite3
import mysql.connector

 # create first connection with database !
connect = sqlite3.connect('database.db')
# create a cursor
cr = connect.cursor()

class DataBase:
    
  

    # create database tabel for user login
    cr.execute("""CREATE TABLE IF NOT EXISTS logins
                (name TEXT,
                 email TEXT,
                 password TEXT
                 admin TEXT)""")

    # add user to database

    def add(name, email, password, admin):
        with connect:
            cr.execute("INSERT INTO logins VALUES(?,?,?,?)", (name, email, password, admin))
            connect.commit()
            print("user added !")
            
    def delete(name, email, password):
        with connect:
            sql = ("DELETE FROM logins WHERE email=?")
            cr.execute(sql, (email,))
       
            connect.commit()
               
          
            print("user deleted!")
    # validate user for login
    def validate(email, password):
        with connect:
            cr.execute('SELECT * FROM logins WHERE email = ? AND password = ?', (email, password)) #Collect the email and password from database
            if cr.fetchall(): #check if there is no values
                return True #return true if there is an email and password present with the login given
            else:
                return False    #return false if no login with those credentials are present

    def validateAdmin(admin):
        with connect:
            cr.execute('SELECT * FROM logins WHERE admin = ?', (admin)) #Collect the email and password from database
            if cr.fetchall(): #check if there is no values
                return True #return true if there is an email and password present with the login given
            else:
                return False    #return false if no login with those credentials are present


    # read data from database
    def read():
        with connect:
            cr.execute("SELECT * FROM logins")
            log = cr.fetchall()
            print(log)