"""This module contains GameScreen class"""
import sched
import time
from functools import partial
import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from game_state import Game

class DurationClock(Label):
    """This is custom Label which make for timer"""
    def update(self, index, *args):
        """This method is update kivy clock"""
        if index == '0':
            self.text = 'Время закончилось нажмите чтобы передать ход'
            self.parent.children[1].text = 'Начать'
            self.parent.children[1].unbind(on_press=self.parent.parent.get)
            self.parent.children[1].unbind(on_press=self.parent.parent.start_game)
        else:
            self.text = self.text.split('\n')[0]
            self.text += '\nОсталось {} секунд'.format(index)



class GameScreen(Screen):
    """No ideas"""
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.game = Game(['DEFAULT', 'DEFAULT'], 0)
        self.words = open('dictionary').readlines()
        self.timer = sched.scheduler(time.time, time.sleep)
        root_box = BoxLayout(orientation="vertical")
        root_box.add_widget(self.configure_player_now_bar_())
        name_label = DurationClock(text='Нажмите чтобы начать')
        root_box.add_widget(name_label)
        root_box.add_widget(Button(text='Начать', on_press=self.start_game))
        root_box.add_widget(self.config_status_bar_())
        self.add_widget(root_box)


    def on_enter(self, *largs):
        """This method is config game when window is push"""
        self.game = Game(self.manager.names, 0)
        self.upd()

    @staticmethod
    def configure_player_now_bar_():
        """This method is config player now bar"""
        player_box = BoxLayout(orientation="horizontal", size_hint=(1, .2))
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

    def upd(self):
        """"This method is update player now bar labels"""
        now = self.game.now_play()
        score = self.game.now_players_scroe()
        self.children[0].children[3].children[0].text = now[0] + ' ' + str(score[0])
        self.children[0].children[3].children[1].text = now[1] + ' ' + str(score[1])

    def next(self, instance):
        """This method is push next player"""
        self.upd()
        instance.parent.children[2].text = 'Нажмите чтобы начать'

    def exit(self, instance):
        """This method is push prev window"""
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.previous()

    def get(self, instance):
        """This method update score when word is get"""
        text = instance.parent.children[2].text.split('\n')
        text[0] = random.choice(self.words)
        instance.parent.children[2].text = ''.join(text)
        self.game.get_word()
        self.upd()

    def start_game(self, instance):
        """This method start hat timer"""
        instance.text = 'Угадано'
        instance.parent.children[2].text = random.choice(self.words)
        instance.bind(on_press=self.get)
        instance.unbind(on_press=self.start_game)
        for i in range(30, -1, -1):
            Clock.schedule_once(partial(instance.parent.children[2].update, str(i)), 30 - i)
