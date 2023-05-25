# from kivymd.uix.stacklayout import MDStackLayout
from kivy.uix.screenmanager import Screen

from glob import glob
from file_card import FileCard

class MainActivity(Screen):
    UserId: int
    DefaultDict: str = r'./*'

    def __init__(self, user_id, **kwargs):
        super(MainActivity, self).__init__(**kwargs)
        self.UserId = user_id

    def on_enter(self):
        self.CardLayout = self.ids['cards_layout']
        for file in glob(self.DefaultDict):
            self.CardLayout.add_widget(FileCard(file))
        