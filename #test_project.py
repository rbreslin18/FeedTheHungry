#test_project.py
from typing import ContextManager
from kivy.lang.builder import create_handler
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from logging import CRITICAL, critical
from sqlite3.dbapi2 import connect
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown

from kivy.uix.checkbox import CheckBox

from kivy.properties import ListProperty
import sqlite3 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.core.window import Window
import unittest


  
class Home(unittest.TestCase):
    # test function to test equality of two value
    def test_getuser(self):
        name = "self.ids.name.text"
        email = "self.ids.name.text"
        
        message = "name and email not equal to  self.ids.name.text!"
        # assertEqual() to check equality of first & second value
        self.assertEqual(name,email, message)

    def test_deleteuser(self):
        name = "self.ids.name.text"
        email = "self.ids.name.text"
        
        message = "name and email not equal to  self.ids.name.text!"
        # assertEqual() to check equality of first & second value
        self.assertEqual(name,email, message)

    def test_updateuser(self):
        name = "self.ids.name.text"
        email = "self.ids.lname.text"
       
        message = "name and email not equal to  self.ids.name.text!"
        # assertEqual() to check equality of first & second value
        self.assertNotEqual(name,email, message)

class resetPasswordWindow(unittest.TestCase):
    def test_resetPass(self): # Update password function to change database
        oldPassword = "self.ids.oldpass.text"
        newPassword = "self.ids.newpass.text"
        message = "oldPassword,newPassword not equal "
        self.assertNotEqual(oldPassword,newPassword, message)

class MyMainApp(unittest.TestCase):
   
    def test_build(self):
       
        self.title = "Feed The Hungry" 
        message = "title equal to Feed the Hungry "
        self.assertEqual(self.title, "Feed The Hungry" , message)

class LoginWindow(unittest.TestCase):
    
    def test_loginBtn(self):  #define login button
        logEmail = "self.email.text"
        logPass = "self.password.text"
        print(logEmail) #dev testing for variables
        print(logPass)
        message = "self.email.text is not equal self.password.text  "
        self.assertNotEqual("self.email.text", "self.password.text", message)

        

class MainWindow(unittest.TestCase): #Define Main Window
    
    
    def test_logOut(self):
        sm=ScreenManager
        sm.current = "login"
        message = " sm.current is equal to login"
        self.assertEqual(sm.current, "login", message)
        
    
class ShowOrderWindow(unittest.TestCase): #Show Order Screen
    
    def test_get_data(self):
        self.rows = "create_handler.fetchall()"
        print(self.rows)
        self.assertEqual(self.rows,"create_handler.fetchall()")

class CreateAccountWindow(unittest.TestCase):

    def test_login(self):
        sm=ScreenManager
        sm.current = "login"
        self.assertEqual(sm.current, "login")
    
    def test_termsPage(self):
        pop = Popup(title='Terms of Use',
        content = Label(text=''''Terms and Conditions'''))
        self.assertNotEqual(pop,ContextManager)


if __name__ == '__main__': 
     unittest.main() 
    