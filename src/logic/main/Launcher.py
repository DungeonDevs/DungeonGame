from src.logic.main.Game import Game
from src.logic.main.PlayerClass import *
import tkinter

'''
creates a new instance of the game
'''
#game = Game(AppleFanboy())
class Launcher:
    def __init__(self):
        game = Game(Healer())