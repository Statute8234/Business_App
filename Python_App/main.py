from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.textfield import MDTextField
from kivy.properties import StringProperty
from kivy.clock import Clock
import pythonDatabase
# show notification
def show_notification(check):
    if check:
        toast('Sorry, Somthing has gone wrong')
    else:
        toast('Success')
# app
class WindowManager(ScreenManager):
    pass

class Home_Screen(Screen):
    def __init__(self, **kwargs):
        super(Home_Screen, self).__init__(**kwargs)
        Builder.load_file('home_screen.kv')

class Login_Screen(Screen):
    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)
        Builder.load_file('login_screen.kv')

    def check_input(self):
        self.LoginBusinessName_input = self.ids.businessName_input
        self.LoginSymbolEmblem_input = self.ids.symbolEmblem_input
        self.LoginPassword_input = self.ids.text_field
        # ----
        self.LoginBusinessName = self.LoginBusinessName_input.text
        self.LoginSymbolEmblem = self.LoginSymbolEmblem_input.text
        self.LoginPassword = self.LoginPassword_input.text

class Forgotpassword_Screen(Screen):
    def __init__(self, **kwargs):
        super(Forgotpassword_Screen, self).__init__(**kwargs)
        Builder.load_file('forgotpassword_screen.kv')

    def check_input(self):
        self.ForgotBusinessName_input = self.ids.businessName_input
        self.ForgotSymbolEmblem_input = self.ids.symbolEmblem_input
        self.ForgotEmail_input = self.ids.email_input
        # ----
        self.ForgotBusinessName = self.LoginBusinessName_input.text
        self.ForgotSymbolEmblem = self.LoginSymbolEmblem_input.text
        self.ForgotEmail = self.ForgotEmail_input.text

class Signup_Screen(Screen):
    def __init__(self, **kwargs):
        super(Signup_Screen, self).__init__(**kwargs)
        Builder.load_file('signup_screen.kv')

    def check_input(self):
        self.SignupBusinessName_input = self.ids.businessName_input
        self.SignupSymbolEmblem_input = self.ids.symbolEmblem_input
        self.SignupEmail_input = self.ids.email_input
        self.SignupPassword_input = self.ids.text_field
        # ----
        self.SignupBusinessName = self.SignupBusinessName_input.text
        self.SignupSymbolEmblem = self.SignupSymbolEmblem_input.text
        self.SignupEmail = self.SignupEmail_input.text
        self.SignupPassword = self.SignupPassword_input.text
        #show_notification(pythonDatabase.check_sign_up(self.SignupEmail))

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')

if __name__ == '__main__':
    Window.size = (360, 640)
    MainApp().run()