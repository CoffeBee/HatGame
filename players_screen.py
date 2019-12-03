"""This module contains PlayerScreen class"""

from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class PlayerScreen(Screen):
    """No ideas"""
    def __init__(self, **kwargs):
        super(PlayerScreen, self).__init__(**kwargs)
        box = BoxLayout(orientation="vertical")
        name_input = TextInput(text='Hello world')
        box.add_widget(name_input)
        grid = GridLayout(cols=3)
        box.add_widget(grid)
        self.add_widget(box)
