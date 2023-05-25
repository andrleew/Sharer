from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior

class FileCard(MDCard, RoundedRectangularElevationBehavior):
    Name: str
    
    def __init__(self, name: str, **kwargs):
        super(FileCard, self).__init__(**kwargs)
        self.Name = name
        self.label = self.ids['card_text']
        self.label.text = self.Name