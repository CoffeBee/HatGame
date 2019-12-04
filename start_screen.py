"""This module is contains StartScreen class"""
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label

class StartScreen(Screen):
    """No ideas"""
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        root_box = BoxLayout(orientation='horizontal')
        root_box.add_widget(Button(text='Начать игру', on_press=self.start_callback))
        self.add_widget(root_box)

    def start_callback(self, instance):
    	self.manager.current = self.manager.next()