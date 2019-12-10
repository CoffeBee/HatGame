"""This module contains Game class"""

class Game:
    """This class host and update hat game state"""
    def __init__(self, names, mode):
        self.names = names
        self.people_cnt = len(names)
        self.mode = mode
        self.now = (0, 1)
        self.delta = 1
        self.inv = False
        self.score = {}
        for name in names:
            self.score[name] = 0
    def next_circle_(self):
        """This method is update game state when people turn in pair circle"""
        if self.now[0] == self.people_cnt - 1:
            self.delta += 1
            self.delta %= self.people_cnt
        self.now = ((self.now[0] + 1) % self.people_cnt,
                    (self.now[0] + 1 + self.delta) % self.people_cnt)

    def next_pair_(self):
        """This method is update game state when people turn in pair mode"""
        self.now = ((self.now[0] + 2) % self.people_cnt, (self.now[1] + 2) % self.people_cnt)
        if self.now == (0, 1) or self.now == (1, 0):
            self.inv = not self.inv
            self.now = (self.now[1], self.now[0])

    def next(self):
        """This method is update game state when people turn"""
        if self.mode == 0:
            self.next_circle_()
        else:
            self.next_pair_()

    def get_word(self):
        """This method is update score state"""
        self.score[self.names[self.now[0]]] += 1
        self.score[self.names[self.now[1]]] += 1

    def now_play(self):
        """This method is return who is now playing"""
        return (self.names[self.now[0]], self.names[self.now[1]])

    def now_players_scroe(self):
        """This method is return score"""
        return (self.score[self.names[self.now[0]]], self.score[self.names[self.now[1]]])
