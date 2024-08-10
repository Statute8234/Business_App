from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp

class WindowManager(ScreenManager):
    pass

class Login_Screen(Screen):
    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)
        Builder.load_file('login_screen.kv')

class Forgotpassword_Screen(Screen):
    def __init__(self, **kwargs):
        super(Forgotpassword_Screen, self).__init__(**kwargs)
        Builder.load_file('forgotpassword_screen.kv')

class Signup_Screen(Screen):
    def __init__(self, **kwargs):
        super(Signup_Screen, self).__init__(**kwargs)
        Builder.load_file('signup_screen.kv')

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')

if __name__ == '__main__':
    Window.size = (360, 640)
    MainApp().run()