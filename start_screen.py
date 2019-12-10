"""This module is contains StartScreen class"""
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class StartScreen(Screen):
    """No ideas"""
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        root_box = FloatLayout()
        root_box.add_widget(self.config_start_button_())
        self.add_widget(root_box)

    def config_start_button_(self):
        """This method is config start game button"""
        start_button = Button(text="Начать игру!",
                              font_size="20sp",
                              background_color=(1, 1, 1, 1),
                              color=(255, 1, 1, 1),
                              size=(32, 32),
                              size_hint=(.2, .2),
                              pos_hint={'y' : .4, 'x' : .4},
                              on_press=self.start_callback)

        return start_button
    def start_callback(self, instance):
        """This method is push next window"""
        self.manager.current = self.manager.next()
