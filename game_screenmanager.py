"""This module contains GameScreenManager class"""

from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ListProperty, NumericProperty, StringProperty
class GameScreenManager(ScreenManager):
    """This class is contains names"""
    names = ListProperty()
    mode = NumericProperty()
    dicts = StringProperty
