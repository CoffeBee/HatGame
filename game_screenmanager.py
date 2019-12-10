"""This module contains GameScreenManager class"""

from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ListProperty
class GameScreenManager(ScreenManager):
    names = ListProperty()
