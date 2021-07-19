# main.py
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen



class MyGrid(Widget):
    pass

 
 
    def popup(self):
        pop=Popup(title="Popup",
                 content=Label(text=" Are you sure you wnat to submit"),
                 size_hint=(None, None), size= (400,400))
     
        pop.open()


class NoTitleDialog(Popup):
    pass

class MyApp(App): 
    def build(self):
        return MyGrid()


    
        

if __name__ == "__main__":
    MyApp().run()

    
