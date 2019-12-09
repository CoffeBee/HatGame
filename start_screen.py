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
        root_box = FloatLayout(orientation='horizontal')
        root_box.add_widget(self.build())
        self.add_widget(root_box)

    def build(self): 
        """ use a (r, g, b, a) tuple """
        root_box = Button(text ="Начать игру!", 
                   font_size ="20sp", 
                   background_color =(1, 1, 1, 1), 
                   color =(255, 1, 1, 1),  
                   size =(32, 32), 
                   size_hint =(.2, .2), 
                   pos_hint={'y' : .4, 'x' : .4}) 
 
        return root_box

    def start_callback(self, instance):
    	self.manager.current = self.manager.next()