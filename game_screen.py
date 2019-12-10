"""This module contains GameScreen class"""

from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from game_state import Game
import sched, time
from kivy.clock import Clock
from functools import partial
import random
class DurationClock(Label):
    def update(self, index, *args):
        if index == '0':
            self.text = 'Время закончилось нажмите чтобы передать ход'
            self.parent.children[1].text = 'Начать'
            self.parent.children[1].unbind(on_press = self.parent.parent.get)
            self.parent.children[1].unbind(on_press = self.parent.parent.start_game)
        else:
            self.text = self.text.split('\n')[0]
            self.text += '\nОсталось {} секунд'.format(index)



class GameScreen(Screen):
    """No ideas"""
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.words = open('dictionary').readlines()
        self.timer = sched.scheduler(time.time, time.sleep)
        root_box = BoxLayout(orientation="vertical")
        root_box.add_widget(self.configure_player_now_bar_())
        name_label = DurationClock(text='Нажмите чтобы начать', size_hint=(0.5, 0.5), pos_hint= {'center_x': 0.5, 'center_y': 0.5})
        root_box.add_widget(name_label)
        root_box.add_widget(Button(text='Начать', on_press=self.start_game))
        root_box.add_widget(self.config_status_bar_())
        self.add_widget(root_box)


    def on_enter(self, *largs):
        self.game = Game(self.manager.names, 0)
        self.upd_next()

    def configure_player_now_bar_(self):
        player_box = BoxLayout(orientation="horizontal", size_hint=(1,.2))
        player_box.add_widget(Label(text='ф'))
        player_box.add_widget(Label(text='a'))
        return player_box

    def config_status_bar_(self):
        """Method to configure status bar add interface"""
        res_box = BoxLayout(orientation='horizontal', size_hint=(1, .1))
        res_box.add_widget(Button(text='Передать ход', on_press=self.next,
                           size_hint=(.2, 1)))
        res_box.add_widget(Button(text='Выйти', on_press=self.exit,
                                  size_hint=(.2, 1)))
        return res_box

    def upd_next(self):
        now = self.game.now_play()
        score = self.game.now_players_scroe()
        self.children[0].children[3].children[0].text = now[0] + ' ' + str(score[0])
        self.children[0].children[3].children[1].text = now[1] + ' ' + str(score[1])

    def next(self, instance):
        self.upd_next()
        instance.parent.children[2].text = 'Нажмите чтобы начать'

    def exit(self, instance):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.previous()

    def end_game(self):
        self.upd_next()

    def get(self, instance):
        text = instance.parent.children[2].text.split('\n')
        text[0] = random.choice(self.words)
        instance.parent.children[2].text = ''.join(text)
        self.game.get_word()
        self.upd_next()

    def start_game(self, instance):
        instance.text = 'Угадано'
        instance.parent.children[2].text = random.choice(self.words)
        instance.bind(on_press = self.get)
        instance.unbind(on_press = self.start_game)
        for i in range(30, -1, -1):
            Clock.schedule_once(partial(instance.parent.children[2].update, str(i)), 30 - i )
