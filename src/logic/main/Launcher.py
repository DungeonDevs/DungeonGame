from src.logic.main.Game import Game
from src.logic.main.PlayerClass import Knight, Healer, Adventurer, Thief
import tkinter

'''
creates a new instance of the game
'''
class Launcher:
    def __init__(self):
        game = Game(Healer())