# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from Admin_DB import DataBase

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    DataBase.add("admin","admin@admin.com","321","yes")
    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                DataBase.add(self.namee.text, self.email.text, self.password.text, "no") #Add to database
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


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
   
    def loginBtn(self):
        logEmail = self.email.text
        logPass = self.password.text
        print(logEmail)
        print(logPass)
        if DataBase.validate(logEmail, logPass):
            DataBase.read()
            self.reset()
            sm.current = "main"
        elif DataBase.validate(logEmail, logPass) and DataBase.getAdmin("yes") == "yes")):
            DataBase.read()
            self.reset()
            sm.current = "test"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
    def test(self):
        self.reset()
        sm.current = "test"

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

  
        
        
class TestWindow(Screen):
    def testbtn(self):
        self.reset()

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


screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),TestWindow(name="test")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        self.title = 'Feed The Hungry'
        return sm


if __name__ == "__main__":
    MyMainApp().run()