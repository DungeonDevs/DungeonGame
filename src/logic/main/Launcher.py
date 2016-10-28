from src.logic.main.Game import Game
from src.logic.main.PlayerClass import Knight, Healer, Adventurer, Thief
import tkinter

'''
creates a new instance of the game
'''
game = Game(Healer())
class Launcher:
    def __init__(self):
        self.window = Tk()