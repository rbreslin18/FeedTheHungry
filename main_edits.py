 
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
from db1 import DataBase
from kivy.uix.checkbox import CheckBox
from kivymd.app import MDApp
from kivy.properties import ListProperty
import sqlite3 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.core.window import Window



connect = sqlite3.connect('database.db')
cr = connect.cursor()
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                if self.ids.adm.active: #Checks if the admin checkbox is active
                    DataBase.add(self.namee.text, self.email.text, self.password.text, "admin") #Add to database
                    DataBase.read() #Display current database
                elif self.ids.organ.active: #checks if the organization checkbox is active
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
        pop = Popup(title='Terms of Use',
                
                  content=Label(text=''''Terms and Conditions 
  
Agreement between User and Feed The Hungry 
Welcome to Feed The Hungry. The Feed The Hungry website
(the "Site") is comprised of various web pages operated by Feed The Hungry ("Feed The Hungry").
Feed The Hungry is offered to you conditioned on your acceptance without modification of the terms,
conditions, and notices contained herein (the "Terms").
Your use of Feed The Hungry constitutes your agreement to all such Terms.
Please read these terms carefully, and keep a copy of them for your reference. 
  
Feed The Hungry is a Non-Profit Site. 
  
Food Donations 
  
Privacy 
Your use of Feed The Hungry is subject to Feed The Hungry's Privacy Policy.
Please review our Privacy Policy,
which also governs the Site and informs users of our data collection practices. 
  
Electronic Communications 
Visiting Feed The Hungry or sending emails to Feed The Hungry constitutes electronic communications.
You consent to receive electronic communications
and you agree that all agreements, notices, disclosures and other
communications that we provide to you electronically, via email and on the Site,
satisfy any legal requirement that such communications be in writing. 
  
Your Account 
If you use this site, you are responsible for maintaining the confidentiality of your account and password
and for restricting access to your computer, and you agree to accept responsibility
for all activities that occur under your account or password. You may not assign or
otherwise transfer your account to any other person or entity.
You acknowledge that Feed The Hungry is not responsible for third party access to your account that results from theft or misappropriation of your account.
Feed The Hungry and its associates reserve the right to refuse or cancel service, terminate accounts, or remove or edit content in our sole discretion. 
  
Children Under Thirteen 
Feed The Hungry does not knowingly collect, either online or offline, personal information from persons under the age of thirteen. If you are under 18, you may use Feed The Hungry only with permission of a parent or guardian. 
  
Cancellation/Refund Policy 
Cancel within 24 hours of delivery 
  
Links to Third Party Sites/Third Party Services 
Feed The Hungry may contain links to other websites ("Linked Sites"). The Linked Sites are not under the control of Feed The Hungry and Feed The Hungry is not responsible for the contents of any Linked Site, including without limitation any link contained in a Linked Site, or any changes or updates to a Linked Site. Feed The Hungry is providing these links to you only as a convenience, and the inclusion of any link does not imply endorsement by Feed The Hungry of the site or any association with its operators. 
  
Certain services made available via Feed The Hungry are delivered by third party sites and organizations. By using any product, service or functionality originating from the Feed The Hungry domain, you hereby acknowledge and consent that Feed The Hungry may share such information and data with any third party with whom Feed The Hungry has a contractual relationship to provide the requested product, service or functionality on behalf of Feed The Hungry users and customers. 
  
No Unlawful or Prohibited Use/Intellectual Property 
You are granted a non-exclusive, non-transferable, revocable license to access and use Feed The Hungry strictly in accordance with these terms of use. As a condition of your use of the Site, you warrant to Feed The Hungry that you will not use the Site for any purpose that is unlawful or prohibited by these Terms. You may not use the Site in any manner which could damage, disable, overburden, or impair the Site or interfere with any other party's use and enjoyment of the Site. You may not obtain or attempt to obtain any materials or information through any means not intentionally made available or provided for through the Site. 
  
All content included as part of the Service, such as text, graphics, logos, images, as well as the compilation thereof, and any software used on the Site, is the property of Feed The Hungry or its suppliers and protected by copyright and other laws that protect intellectual property and proprietary rights. You agree to observe and abide by all copyright and other proprietary notices, legends or other restrictions contained in any such content and will not make any changes thereto. 
  
You will not modify, publish, transmit, reverse engineer, participate in the transfer or sale, create derivative works, or in any way exploit any of the content, in whole or in part, found on the Site. Feed The Hungry content is not for resale. Your use of the Site does not entitle you to make any unauthorized use of any protected content, and in particular you will not delete or alter any proprietary rights or attribution notices in any content. You will use protected content solely for your personal use, and will make no other use of the content without the express written permission of Feed The Hungry and the copyright owner. You agree that you do not acquire any ownership rights in any protected content. We do not grant you any licenses, express or implied, to the intellectual property of Feed The Hungry or our licensors except as expressly authorized by these Terms. 
  
International Users 
The Service is controlled, operated and administered by Feed The Hungry from our offices within the USA.
If you access the Service from a location outside the USA, you are responsible for compliance with all local laws.
You agree that you will not use the
Feed The Hungry Content accessed through Feed The Hungry in any country or in any manner prohibited by any applicable laws, restrictions or regulations. 
  
Indemnification 
You agree to indemnify, defend and hold harmless Feed The Hungry, its officers, directors, employees, agents and third parties, for any losses, costs, liabilities and expenses (including reasonable attorney's fees) relating to or arising out of your use of or inability to use the Site or services, any user postings made by you, your violation of any terms of this Agreement or your violation of any rights of a third party, or your violation of any applicable laws, rules or regulations. Feed The Hungry reserves the right, at its own cost, to assume the exclusive defense and control of any matter otherwise subject to indemnification by you, in which event you will fully cooperate with Feed The Hungry in asserting any available defenses. 
  
Arbitration 
In the event the parties are not able to resolve any dispute between them arising out of or concerning these Terms and Conditions, or any provisions hereof, whether in contract, tort, or otherwise at law or in equity for damages or any other relief, then such dispute shall be resolved only by final and binding arbitration pursuant to the Federal Arbitration Act, conducted by a single neutral arbitrator and administered by the American Arbitration Association, or a similar arbitration service selected by the parties, in a location mutually agreed upon by the parties. The arbitrator's award shall be final, and judgment may be entered upon it in any court having jurisdiction. In the event that any legal or equitable action, proceeding or arbitration arises out of or concerns these Terms and Conditions, the prevailing party shall be entitled to recover its costs and reasonable attorney's fees. The parties agree to arbitrate all disputes and claims in regards to these Terms and Conditions or any disputes arising as a result of these Terms and Conditions, whether directly or indirectly, including Tort claims that are a result of these Terms and Conditions. The parties agree that the Federal Arbitration Act governs the interpretation and enforcement of this provision. The entire dispute, including the scope and enforceability of this arbitration provision shall be determined by the Arbitrator. This arbitration provision shall survive the termination of these Terms and Conditions. 
  
Class Action Waiver 
Any arbitration under these Terms and Conditions will take place on an individual basis; class arbitrations and class/representative/collective actions are not permitted. THE PARTIES AGREE THAT A PARTY MAY BRING CLAIMS AGAINST THE OTHER ONLY IN EACH'S INDIVIDUAL CAPACITY, AND NOT AS A PLAINTIFF OR CLASS MEMBER IN ANY PUTATIVE CLASS, COLLECTIVE AND/ OR REPRESENTATIVE PROCEEDING, SUCH AS IN THE FORM OF A PRIVATE ATTORNEY GENERAL ACTION AGAINST THE OTHER. Further, unless both you and Feed The Hungry agree otherwise, the arbitrator may not consolidate more than one person's claims, and may not otherwise preside over any form of a representative or class proceeding. 
  
Liability Disclaimer 
THE INFORMATION, SOFTWARE, PRODUCTS, AND SERVICES INCLUDED IN OR AVAILABLE THROUGH THE SITE MAY INCLUDE INACCURACIES OR TYPOGRAPHICAL ERRORS. CHANGES ARE PERIODICALLY ADDED TO THE INFORMATION HEREIN. FEED THE HUNGRY AND/OR ITS SUPPLIERS MAY MAKE IMPROVEMENTS AND/OR CHANGES IN THE SITE AT ANY TIME. 
  
FEED THE HUNGRY AND/OR ITS SUPPLIERS MAKE NO REPRESENTATIONS ABOUT THE SUITABILITY, RELIABILITY, AVAILABILITY, TIMELINESS, AND ACCURACY OF THE INFORMATION, SOFTWARE, PRODUCTS, SERVICES AND RELATED GRAPHICS CONTAINED ON THE SITE FOR ANY PURPOSE. TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, ALL SUCH INFORMATION, SOFTWARE, PRODUCTS, SERVICES AND RELATED GRAPHICS ARE PROVIDED "AS IS" WITHOUT WARRANTY OR CONDITION OF ANY KIND. FEED THE HUNGRY AND/OR ITS SUPPLIERS HEREBY DISCLAIM ALL WARRANTIES AND CONDITIONS WITH REGARD TO THIS INFORMATION, SOFTWARE, PRODUCTS, SERVICES AND RELATED GRAPHICS, INCLUDING ALL IMPLIED WARRANTIES OR CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. 
  
TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL FEED THE HUNGRY AND/OR ITS SUPPLIERS BE LIABLE FOR ANY DIRECT, INDIRECT, PUNITIVE, INCIDENTAL, SPECIAL, CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS OF USE, DATA OR PROFITS, ARISING OUT OF OR IN ANY WAY CONNECTED WITH THE USE OR PERFORMANCE OF THE SITE, WITH THE DELAY OR INABILITY TO USE THE SITE OR RELATED SERVICES, THE PROVISION OF OR FAILURE TO PROVIDE SERVICES, OR FOR ANY INFORMATION, SOFTWARE, PRODUCTS, SERVICES AND RELATED GRAPHICS OBTAINED THROUGH THE SITE, OR OTHERWISE ARISING OUT OF THE USE OF THE SITE, WHETHER BASED ON CONTRACT, TORT, NEGLIGENCE, STRICT LIABILITY OR OTHERWISE, EVEN IF FEED THE HUNGRY OR ANY OF ITS SUPPLIERS HAS BEEN ADVISED OF THE POSSIBILITY OF DAMAGES. BECAUSE SOME STATES/JURISDICTIONS DO NOT ALLOW THE EXCLUSION OR LIMITATION OF LIABILITY FOR CONSEQUENTIAL OR INCIDENTAL DAMAGES, THE ABOVE LIMITATION MAY NOT APPLY TO YOU. IF YOU ARE DISSATISFIED WITH ANY PORTION OF THE SITE, OR WITH ANY OF THESE TERMS OF USE, YOUR SOLE AND EXCLUSIVE REMEDY IS TO DISCONTINUE USING THE SITE. 
  
Termination/Access Restriction 
Feed The Hungry reserves the right, in its sole discretion, to terminate your access to the Site and the related services or any portion thereof at any time, without notice. To the maximum extent permitted by law, this agreement is governed by the laws of the State of Michigan and you hereby consent to the exclusive jurisdiction and venue of courts in Michigan in all disputes arising out of or relating to the use of the Site. Use of the Site is unauthorized in any jurisdiction that does not give effect to all provisions of these Terms, including, without limitation, this section. 
  
You agree that no joint venture, partnership, employment, or agency relationship exists between you and Feed The Hungry as a result of this agreement or use of the Site. Feed The Hungry's performance of this agreement is subject to existing laws and legal process, and nothing contained in this agreement is in derogation of Feed The Hungry's right to comply with governmental, court and law enforcement requests or requirements relating to your use of the Site or information provided to or gathered by Feed The Hungry with respect to such use. If any part of this agreement is determined to be invalid or unenforceable pursuant to applicable law including, but not limited to, the warranty disclaimers and liability limitations set forth above, then the invalid or unenforceable provision will be deemed superseded by a valid, enforceable provision that most closely matches the intent of the original provision and the remainder of the agreement shall continue in effect. 
  
Unless otherwise specified herein, this agreement constitutes the entire agreement between the user and Feed The Hungry with respect to the Site and it supersedes all prior or contemporaneous communications and proposals, whether electronic, oral or written, between the user and Feed The Hungry with respect to the Site. A printed version of this agreement and of any notice given in electronic form shall be admissible in judicial or administrative proceedings based upon or relating to this agreement to the same extent and subject to the same conditions as other business documents and records originally generated and maintained in printed form. It is the express wish to the parties that this agreement and all related documents be written in English. 
  
Changes to Terms 
Feed The Hungry reserves the right, in its sole discretion, to change the Terms under which Feed The Hungry is offered. The most current version of the Terms will supersede all previous versions. Feed The Hungry encourages you to periodically review the Terms to stay informed of our updates. 
  
Contact Us 
Feed The Hungry welcomes your questions or comments regarding the Terms: 
  
Feed The Hungry 

  
Effective as of July 26, 2021 
  
 '''),
                  size_hint=(None, None), size=(300, 200))

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
                sm.current = "admin"
            elif DataBase.validateType(logEmail, "donator"): #check if the type is donator
                sm.current = "donator"
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
    rows = ListProperty([("id","type","creator","reciever")])
    def get_data(self):
        
        with connect:
            cr.execute("SELECT * FROM orders")
            self.rows = cr.fetchall()
            print(self.rows)
class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(300, 200))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(300, 200))

    pop.open()


kv = Builder.load_file("app.kv")
sm = WindowManager()
#Below is the screens that are used by the screen manager and allow buttons to transition
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),TestWindow(name="test"),resetPasswordWindow(name="resetPass"),CreateOrderWindow(name="createOrder"),OrganizationWindow(name="org"),AdminWindow(name="admin"),ShowOrderWindow(name="showorders")]
for screen in screens: #for each screen in the array of screens
    sm.add_widget(screen) #add the screen

sm.current = "login"


class MyMainApp(MDApp):
    
    def build(self):
        Window.size=(400,550)
        self.theme_cls.theme_style = "Dark"
        self.title = 'Feed The Hungry' #title for the application
        return sm #return screen manager


if __name__ == "__main__":
    MyMainApp().run()
