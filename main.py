# main.py
# Feed The Hungry App
# Coded by Rodney Breslin, Aqueelah Akbar, Zaheda Akthar
# CSC 4111 Summer
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from dbfile import DataBase
from kivy.uix.checkbox import CheckBox
from kivymd.app import MDApp
from kivy.properties import ListProperty
import mysql.connector
import sqlite3 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
connect = sqlite3.connect('database.db')
cr = connect.cursor()
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
            
                if self.ids.organ.active: #checks if the organization checkbox is active
                    DataBase.add(self.namee.text, self.email.text, self.password.text, "org") #Add to database
                    DataBase.read() #Display current database
                elif self.ids.donator.active: #checks if the donator checkbox is active
                    DataBase.add(self.namee.text, self.email.text, self.password.text, "donator") #Add to database
                    DataBase.read() #Display current database
                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def termsPage(self):
        pop = Popup(title='Terms and Coniditions',
                  content=Label(text='Agree to the following Terms'),
                  size_hint=(None, None), size=(400, 400))

        pop.open()
    

        

class LoginWindow(Screen): #Define Login Window
    
    email = ObjectProperty(None) #Email variable for user
    password = ObjectProperty(None) #password variable for user
   
    def loginBtn(self):  #define login button
        logEmail = self.email.text
        logPass = self.password.text
        print(logEmail) #dev testing for variables
        print(logPass) #dev testing for variables
        if DataBase.validate(logEmail, logPass): #check if database has the username and password provided
            if DataBase.validateType(logEmail, "admin"): #Check if the type is admin
                sm.current = "test"
            elif DataBase.validateType(logEmail, "donator"): #check if the type is donator
                sm.current = "donate"
            elif DataBase.validateType(logEmail, "org"): #check if the type is organization
                sm.current = "org"
           
            
            DataBase.read() #dev testing to display database
            self.reset() #reset variables
            #sm.current = "main" #set users screen to the main screen
        else:
            invalidLogin()

    def createBtn(self): #Create account button
        self.reset()
        sm.current = "create" #Transitions to create account screen when pressed

    def reset(self):
        self.email.text = ""
        self.password.text = ""
    
    
    def test(self): #Test Button
        self.reset()
        sm.current = "test" #Transitions to the donators page to skip logging in
    def rePass(self): #Reset password button
        self.password.text = ""
        sm.current = "resetPass" #transistions to reset password screen when pressed

class MainWindow(Screen): #Define Main Window
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

class TestWindow(Screen): #Define Test Window
    def testbtn(self):
        self.reset()

class CreateOrderWindow(Screen): #Define CreateOrderWindow
    id = ObjectProperty(None)
    foodtype = ObjectProperty(None)
    creator = ObjectProperty(None)
    reciever = ObjectProperty(None)
    def submitOrder(self): #Submit Order function to submit to orders database
        DataBase.addOrder(self.ids.ID.text,self.ids.type.text,self.ids.creator.text,self.ids.reciever.text) #Currently just adds in these variables from user input, will change to make sure all order ids are unique
        DataBase.readOrders() #dev testing to read orders to see if the database actually worked
    def testbtn(self):
        self.reset()     
    def submit(self): 
        pop = Popup(title='Are you Sure?',# Test popup
                  content=Label(text='Are you sure you want to create this order?'),
                  size_hint=(None, None), size=(400, 400))

        pop.open() #open popup
    def cancel(self):
        DataBase.deleteOrder(self.ids.ID.text)
        DataBase.readOrders()

class resetPasswordWindow(Screen): #Define resetPasswordWindow
    oldPassword = ObjectProperty(None)
    newPassword = ObjectProperty(None)
    def testbtn(self):
        self.reset()
    def resetPass(self): # Update password function to change database
        oldPassword = self.ids.oldpass.text
        newPassword = self.ids.newpass.text
        DataBase.updatePass(oldPassword, newPassword) #changes database with new password that a user has entered
        DataBase.read() #dev testing - read to the log to check the change

class OrganizationWindow(Screen): #Define class Organization Scren
   pass

class AdminWindow(Screen): #Define class Admin Window
    def getuser(self):
        name = self.ids.name.text
        email = self.ids.lname.text
        password = self.ids.ID.text
        DataBase.add(name,email,password) #Add function to allow admins to change user information
        DataBase.read()
        self.ids.Toplabel.text = "User Inserted !"
        
    def deleteuser(self):
        name = self.ids.name.text
        email = self.ids.name.text
        password = self.ids.name.text
        DataBase.delete(name,email,password)
        DataBase.read()
        self.ids.Toplabel.text = "User Deleted !"
    def updateuser(self):
        name = self.ids.name.text
        email = self.ids.lname.text
        password = self.ids.ID.text
        self.ids.Toplabel.text = "User Updated !"
        DataBase.updatePassWithEmail(email, password)
        DataBase.read()
    def readtable(self):
        DataBase.read()
class ShowOrderWindow(Screen): #Show Order Screen
    rows = ListProperty([("id","type","creator","reciever")]) # Variables to be added
    def get_data(self):
        
        with connect:
            cr.execute("SELECT * FROM orders")
            self.rows = cr.fetchall()
            print(self.rows)
class DonationWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("app.kv")
sm = WindowManager()
#Below is the screens that are used by the screen manager and allow buttons to transition
screens = [DonationWindow(name="donate"),LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),TestWindow(name="test"),resetPasswordWindow(name="resetPass"),CreateOrderWindow(name="createOrder"),OrganizationWindow(name="org"),AdminWindow(name="admin"),ShowOrderWindow(name="showorders")]
for screen in screens: #for each screen in the array of screens
    sm.add_widget(screen) #add the screen

sm.current = "login"


class MyMainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.title = 'Feed The Hungry' #title for the application
        return sm #return screen manager


if __name__ == "__main__":
    MyMainApp().run()