"""This module is run and configure kivy app"""
from kivy.app import App
from players_screen import PlayerScreen
from game_screenmanager import GameScreenManager
from game_screen import GameScreen
from start_screen import StartScreen

class MyApp(App):
    """This is main class of app"""
    def build(self):
        """This method is build app"""
        root = GameScreenManager()
        root.add_widget(StartScreen(name="start"))
        root.add_widget(PlayerScreen(name="players"))
        root.add_widget(GameScreen(name="players2"))
        return root

if __name__ == '__main__':
    MyApp().run()
