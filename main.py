"""This module is run and configure kivy app"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from players_screen import PlayerScreen

class MyApp(App):
    """This is main class of app"""
    def build(self):
        """This method is build app"""
        root = ScreenManager()
        root.add_widget(PlayerScreen(name="players"))
        return root

if __name__ == '__main__':
    MyApp().run()
