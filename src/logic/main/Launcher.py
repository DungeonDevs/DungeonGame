from src.logic.main.Game import Game
#import src.logic.main.PlayerClass as playerTypes
from src.logic.main.PlayerClass import *
from tkinter import *
import sys, inspect

'''
creates a new instance of the game
'''
class Launcher:
    def __init__(self):
        game = Game(Healer())
        return
        self.window = Tk()
        self.window.title('Launcher')
        self.window.minsize(600,400)
        self.window.maxsize(600,400)
        self.backgroundImage = PhotoImage(file="resources/menu.png")
        self.background=Label(self.window,image = self.backgroundImage)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        def startGame(event):
            self.start = True
            self.window.destroy()
        possibleHeroes=["Healer","Knight"]
        self.hero = StringVar()
        self.hero.set(possibleHeroes[0])
        self.dropdown_Object = OptionMenu(self.window, self.hero,*possibleHeroes,command=startGame)
        self.dropdown_Object.pack(anchor=CENTER)
        self.window.mainloop()
        if(self.start == True):
            def callback(gameWon):
                window = Tk()
                window.title('Endscreen')
                if(gameWon):
                    Text=Label(self.window,text = "You WON!")
                    self.background.place(x=0, y=0, relwidth=1, relheight=1)
                else:
                    Text=Label(self.window,text = "GameOver!")
                    self.background.place(x=0, y=0, relwidth=1, relheight=1)
            hero = self.hero.get()
            if hero == "Healer":
                game=Game(Healer())
            elif hero == "Knight":
                game=Game(Knight())
            elif hero == "Adventurer":
                game=Game(Adventurer())
            elif hero == "Thief":
                game=Game(Thief())

