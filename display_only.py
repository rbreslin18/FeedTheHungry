import sqlite3 
from t import DataBase
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
import mysql.connector

connect = sqlite3.connect('databases.db')

# create a cursor
cr = connect.cursor()
Builder.load_file("display.kv")

class MyLayout(BoxLayout):
    rows = ListProperty([("name","email","password")])
    def get_data(self):
        with connect:
            cr.execute("SELECT * FROM users")
            self.rows = cr.fetchall()
            print(self.rows)
runTouchApp(MyLayout())
