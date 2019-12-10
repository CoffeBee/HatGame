"""This module contains PlayerScreen class"""

from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
class PlayerScreen(Screen):
    """No ideas"""
    def __init__(self, **kwargs):
        super(PlayerScreen, self).__init__(**kwargs)
        root_box = BoxLayout(orientation="vertical")
        root_box.add_widget(self.config_player_add_inteface_())
        player_grid = GridLayout(cols=2, size_hint=(1, .85), spacing=10.0)
        root_box.add_widget(player_grid)
        root_box.add_widget(self.config_status_bar_())
        self.add_widget(root_box)

    def config_player_add_inteface_(self):
        """Method to configure player add interface"""
        dicts = ['swift_dict', 'dictionary']
        dropdown = DropDown()
        for index in range(2):
            btn = Button(text=dicts[index], size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        mainbutton = Button(text='choose dict', size_hint=(.3, 1))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        dropdown.bind(on_select=self.upd)
        add_user_box = BoxLayout(orientation="horizontal", size_hint=(1, .05))
        name_input = TextInput(text='', size_hint=(.5, 1))
        add_button = Button(text='add', size_hint=(.2, 1),
                            on_press=self.add_callback)
        add_user_box.add_widget(mainbutton)
        add_user_box.add_widget(name_input)
        add_user_box.add_widget(add_button)
        return add_user_box

    def upd(self, instance, text):
        """This method is upd dropdown """
        self.manager.dicts = text

    def config_status_bar_(self):
        """Method to configure status bar add interface"""
        res_box = BoxLayout(orientation='horizontal', size_hint=(1, .1))
        res_box.add_widget(Button(text='Круговая', on_press=self.next_circle_callback,
                                  size_hint=(.2, 1)))
        res_box.add_widget(Button(text='Парная', on_press=self.next_pair_callback,
                                  size_hint=(.2, 1)))
        res_box.add_widget(Button(text='Отмена', on_press=self.prev_callback,
                                  size_hint=(.2, 1)))
        return res_box

    def add_callback(self, instance):
        """Callback method to add player"""
        player_name = instance.parent.children[1].text
        instance.parent.children[1].text = ''
        player_grid = instance.parent.parent.children[1]
        name_label = Label(text=player_name)
        player_grid.add_widget(name_label)
        self.manager.names.append(player_name)

    def next_circle_callback(self, instance):
        """Method to push next window"""
        self.manager.mode = 0
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = self.manager.next()

    def next_pair_callback(self, instance):
        """Method to push next window"""
        self.manager.mode = 1
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = self.manager.next()

    def prev_callback(self, instance):
        """This method is push prev window"""
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.previous()
