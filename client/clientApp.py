from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from login_activity import LoginActivity

Builder.load_file('client.kv')

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.add_widget(LoginActivity())

class Sharer(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        sm = ScreenManager()
        sm.add_widget(LoginActivity(name='login'))
        return sm
        # return MainActivity(1)

if __name__ ==  "__main__":
    Sharer().run()
    
