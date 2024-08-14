from humanfriendly.terminal import message
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.toast import toast
# ----- hand made
import python_database
#python_database.clear_table()
#python_database.add_user("RedInfinity_Pro", "username", "email",python_database.hash_password("password"))
# show notification
def show_notification(check):
    if check:
        toast('Sorry, Somthing has gone wrong')
    else:
        toast('Success')
# app
class WindowManager(ScreenManager):
    pass

class Login_Screen(Screen):
    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)
        Builder.load_file('login_screen.kv')

    def check_input(self):
        self.LoginUsername_input = self.ids.username_input
        self.LoginPassword_input = self.ids.text_field
        self.LoginUsername = self.LoginUsername_input.text
        self.LoginPassword = self.LoginPassword_input.text

        user_exists, message = python_database.check_user_data('login', username=self.LoginUsername, password=self.LoginPassword)
        if not (len(self.LoginUsername) >= self.LoginUsername_input.max_text_length) or (len(self.LoginPassword) >= self.LoginPassword_input.max_text_length):
            show_notification(user_exists)

class Forgotpassword_Screen(Screen):
    def __init__(self, **kwargs):
        super(Forgotpassword_Screen, self).__init__(**kwargs)
        Builder.load_file('forgotpassword_screen.kv')

    def check_input(self):
        self.ForgotUsername_input = self.ids.username_input
        self.ForgotEmail_input = self.ids.email_input
        self.ForgotUsername = self.ForgotUsername_input.text
        self.ForgotEmail = self.ForgotEmail_input.text

        user_exists, message = python_database.check_user_data('forgot_password', username=self.ForgotUsername, email=self.ForgotEmail)
        if not (len(self.ForgotUsername) >= self.ForgotUsername_input.max_text_length) or (len(self.ForgotEmail) >= self.ForgotEmail_input.max_text_length):
            show_notification(user_exists)

class Signup_Screen(Screen):
    def __init__(self, **kwargs):
        super(Signup_Screen, self).__init__(**kwargs)
        Builder.load_file('signup_screen.kv')

    def check_input(self):
        self.SignupBusiness_input = self.ids.business_input
        self.SignupUsername_input = self.ids.username_input
        self.SignupEmail_input = self.ids.email_input
        self.SignupPassword_input = self.ids.text_field
        self.SignupBusiness = self.SignupBusiness_input.text
        self.SignupUsername = self.SignupUsername_input.text
        self.SignupEmail = self.SignupEmail_input.text
        self.SignupPassword = self.SignupPassword_input.text

        user_exists, message = python_database.check_user_data('sign_up', business_name=self.SignupBusiness, username=self.SignupUsername, email=self.SignupEmail, password=self.SignupPassword)
        if (not (len(self.SignupBusiness) >= self.SignupBusiness_input.max_text_length)
                or (len(self.SignupUsername) >= self.SignupUsername_input.max_text_length)
                or (len(self.SignupEmail) >= self.SignupEmail_input.max_text_length)
                or (len(self.SignupPassword) >= self.SignupPassword_input.max_text_length) ):
            show_notification(not(user_exists))

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')

if __name__ == '__main__':
    Window.size = (360, 640)
    MainApp().run()