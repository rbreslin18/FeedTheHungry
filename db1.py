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
                 password TEXT,
                 type TEXT)""")
    
    # add user to database
    
    def add(name, email, password, type):
        with connect:
            cr.execute("INSERT INTO logins VALUES(?,?,?,?)",(name, email, password, type))
            connect.commit()
            print("user added !")
            
    def delete(name, email, password): #Delete function to delete items from the logins table
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
    def updatePass(email, password):# checks for password to find password
        with connect:
            cr.execute('UPDATE logins SET password = ? WHERE password = ?', (password, email)) #set password when the old password is found in database
            connect.commit()
    def updatePassWithEmail(email, password):# checks for email to find password
        with connect:
            cr.execute('UPDATE logins SET password = ? WHERE email = ?', (password, email)) #set password when email is found in database
            connect.commit()
    def validateType(email, type):
        with connect:
            cr.execute('SELECT type FROM logins WHERE email = ? AND type = ?', (email, type)) #Collect the email and password from database
            if cr.fetchone(): #check if there is no values
                return True #return true if there is an email and password present with the login given
            else:
                return False    #return false if no login with those credentials are present
    # read data from database
    def read():
        with connect:
            cr.execute("SELECT * FROM logins")
            log = cr.fetchall()
            print(log)

    def getAccType(email):
        with connect:
            cr.execute('SELECT type FROM logins WHERE email = ?', (email,))
            accType = cr.fetchone()
            return accType

    # Create table for orders
    cr.execute("""CREATE TABLE IF NOT EXISTS orders
                (id TEXT,
                 foodtype TEXT,
                 creator TEXT,
                 reciever TEXT)""")
    def addOrder(id, foodtype, creator, reciever): #add order to table of orders
        with connect:
            cr.execute("INSERT INTO orders VALUES(?,?,?,?)",(id, foodtype, creator, reciever))
            connect.commit()
            print("order added !")
    def readOrders(): #read orders to display table in the log
        with connect:
            cr.execute("SELECT * FROM orders")
            log = cr.fetchall()
            print(log)