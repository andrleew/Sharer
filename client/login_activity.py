from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.clock import mainthread

import utils

from main_activity import MainActivity

class LoginActivity(Screen):
    def __init__(self, **kwargs):
        super(LoginActivity, self).__init__(**kwargs)

    @mainthread
    def on_enter(self):
        self.LoginActivityWidget = self.ids['login_window']
        self.LoginWidget = self.ids['login']
        self.PasswordWidget = self.ids['password']
        self.SignInButton = self.ids['sign_in']
        self.SignUpButton = self.ids['sign_up']
        self.SignInButton.bind(on_press=self.SignIn)
        self.SignUpButton.bind(on_press=self.SignUp)
        self.App = App.get_running_app()
        
    def Sign(self, button, command, wrong_msg):
        data = utils.send(f'{command}', login=self.LoginWidget.text, password=self.PasswordWidget.text)
        if data['status'] == 0:
            self.App.root.add_widget(MainActivity(data['id'], name='main'))
            self.App.root.current = 'main'
        else:
            Snackbar(text=f'{wrong_msg}').open()
        

    def SignIn(self, button):
        self.Sign(button, command='sign_in', wrong_msg='wrong login or password')
    
    def SignUp(self, button):
        self.Sign(button, command='sign_up', wrong_msg='Login Already exists')
