from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3 as sql
import mysql.connector
import sys
import datetime
from kivy.uix.screenmanager import ScreenManager, Screen



class LoginScreen(Screen):
    pass
class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass



class App(MDApp):

   
    def build(self):
        self.title = 'Feed the Hungry'
        return Builder.load_file("main.kv")
        
       
if __name__ == '__main__':
    App().run()