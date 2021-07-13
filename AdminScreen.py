from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy import Config
from datetime import datetime
from db1 import DataBase
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
import sqlite3

        


# load kivy file styles
Builder.load_file("AdminScreen.kv")

class Home(Screen):
    
    def getuser(self):
        name = self.ids.name.text
        email = self.ids.name.text
        password = self.ids.name.text
        DataBase.add(name,email,password)
        DataBase.read()
        self.ids.Toplabel.text = "User Inserted !"
        
    def deleteuser(self):
        name = self.ids.name.text
        email = self.ids.name.text
        password = self.ids.name.text
        DataBase.delete(name,email,password)
        DataBase.read()
        self.ids.Toplabel.text = "User Deleted !"


   
        
    

    #def displayuse(self):
      #  display(name,email,password)




Screen_Manager = ScreenManager()
# create screen 
Screen_Manager.add_widget(Home(name="Home"))


class MainApp(App):
    title = "Admin Portal"
    def build(self):
        return Screen_Manager

if __name__ == "__main__":
    MainApp().run()
