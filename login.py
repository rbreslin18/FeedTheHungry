from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3 as sql
class MainApp(MDApp):
    con = sql.connect('user.db')
    cur = con.cursor()
    cur.execute(""" CREATE TABLE id(
        user text,
        password text)
        """)
    con.commit()
    con.close()
    def build(self):
        self.theme_cls.theme_style = "Light" #background file
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('login.kv')

MainApp().run()