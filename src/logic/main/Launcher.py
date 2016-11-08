from src.logic.main.Game import Game
from src.logic.main.PlayerClass import *
from tkinter import *

'''
creates a new instance of the game
'''
class Launcher:
    def __init__(self):
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
        possibleHeroes=["Healer","Knight","Adventurer","Thief","Dragon","Tank","Nerd","AngryGrandmother","AppleFanboy","SamsungFanboy","Error404"]
        self.hero = StringVar()
        self.hero.set("Choose Your Hero")
        self.dropdown_Object = OptionMenu(self.window, self.hero,*possibleHeroes,command=startGame)
        self.dropdown_Object.pack(anchor=CENTER)
        self.window.mainloop()
        if(self.start == True):
            hero = self.hero.get()
            if hero == "Healer":
                game=Game(Healer())
            elif hero == "Knight":
                game=Game(Knight())
            elif hero == "Adventurer":
                game=Game(Adventurer())
            elif hero == "Thief":
                game=Game(Thief())
            elif hero == "Dragon":
                game=Game(Dragon())
            elif hero == "Tank":
                game=Game(Tank())
            elif hero == "Nerd":
                game=Game(Nerd())
            elif hero == "AngryGrandmother":
                game=Game(AngryGrandmother())
            elif hero == "AppleFanboy":
                game=Game(AppleFanboy())
            elif hero == "SamsungFanboy":
                game=Game(SamsungFanboy())
            elif hero == "Error404":
                game=Game(Error404())