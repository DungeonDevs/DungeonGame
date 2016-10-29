from tkinter import *
from tkinter.filedialog import *
from src.logic.main.Map import *
from src.logic.objects.Monsters import *
import src.logic.objects.Monsters as MonstersModule
from src.logic.objects.GameObjects import *
import src.logic.objects.GameObjects as GameObjectsModule
import threading
import os
import sys, inspect

"""
returns a dictionary of argName:defaultValues for the input function
"""
def getDefaultParameter(func):
    try:
        parameter, varparameter, keywords, defaults = inspect.getargspec(func)
        print(dict(zip(parameter[-len(defaults):], defaults)))
        return dict(zip(parameter[-len(defaults):], defaults))
    except TypeError as tp:
        print("Error")
        return {}
'''
A tkinter gui to create maps for the game.
The programm exports to a simple .py file so every export can be edited afterwards by hand.
To create a new Level simply call Levelbuilder() with the wanted width and height.
>>> Levelbuilder(10,20)
In the menu on the top of the window can be selected what is edited.
-> Gameobject Mode
    -> leftclick a button to open the gameobjectsettings menu
-> Mob Mode
    -> leftclick a button to open the mobsettings menu
-> Wall Mode
    -> leftclick a button to change this tiles solid state

you can set the playerposition (marked with P) by doublerightclicking a tile
you can always set a tiles solid state by rightclicking the tile
'''
class Levelbuilder(object):
    def __init__(self,ySize=20, xSize=20):
        #prepare datastructure
        self.possibleGameObjects = ["Empty"] + [i[0] for i in inspect.getmembers(GameObjectsModule, inspect.isclass)]# A list of all possible GameObjects)
        excludes = ["GameObject","Interactable","Item","LevelEnd"]
        self.possibleGameObjects = [x for x in self.possibleGameObjects if x not in excludes]
        self.possibleMobs = ["None"] + [i[0] for i in inspect.getmembers(MonstersModule, inspect.isclass)] # A list of all possible Mobs
        self.possibleMobs = [x for x in self.possibleMobs if x not in excludes]
        self.playerposition =(0,0)
        self.GameObjects =[]
        self.Mobs = []
        #prepare window
        self.window = Tk()
        self.window.title('Levelbuilder')
        self.window.minsize(600,400)

        #prepare map
        if xSize > 20:
            xSize = 20
        if ySize > 32:
            ySize = 32
        self.map = Frame(self.window)
        self.map.grid(row=0, column=0)
        self.gameMap = MapHandler().createMap(xSize,ySize)
        self.buttonMap = [[None for _ in range(xSize)] for _ in range(ySize)]
        for y in range(len(self.gameMap)):
            for x in range(len(self.gameMap[0])):
                f = Frame(self.map, height=32, width=32)
                f.pack_propagate(0) # don't shrink
                f.grid(row=x, column=y)
                self.buttonMap[y][x] = Button(f, command = self.getHandelerFunction(y,x), width=2, height = 2)
                self.buttonMap[y][x].bind('<Button-3>', lambda event,y=y, x=x: self.setWall(y,x))
                self.buttonMap[y][x].bind('<Triple-Button-3>', lambda event,y=y, x=x: self.setPlayer(y,x))
                self.buttonMap[y][x].pack(fill=BOTH, expand=1)

        #prepare settings
        self.settings = Frame(self.window)
        self.settings.grid(row=0, column=1, sticky=E)
        #select what to show
        self.setMode(0)
        self.updateMap()
        #Menubar
        self.menubar = Menu(self.window)
        self.menubar.add_command(label="quit", command=self.window.quit)
        self.menubar.add_command(label="export", command=self.export)
        self.menubar.add_command(label="Gameobject Mode", command= lambda : self.setMode(0))
        self.menubar.add_command(label="Mob Mode", command= lambda : self.setMode(1))
        self.menubar.add_command(label="Wall Mode", command= lambda : self.setMode(2))
        self.window.config(menu=self.menubar)

        self.window.mainloop()

    #calls the method set as handeler with the parameter x and y
    def handelClick(self,x,y):
        self.handeler(x,y)

    #changes a tiles solid state
    def setWall(self, xCo, yCo):
        self.gameMap[xCo][yCo].isSolid = not self.gameMap[xCo][yCo].isSolid
        self.updateMap()

    #sets the mode
    def setMode(self, mode):
        self.mode = mode
        if(self.mode ==0):
            self.handeler = self.openGameObjectSettings
            self.settings.destroy()
            self.handelClick(0,0)
        elif(self.mode ==1):
            self.handeler = self.openMobSettings
            self.settings.destroy()
            self.handelClick(0,0)
        elif(self.mode ==2):
            self.handeler = self.setWall
            self.settings.destroy()
        self.updateMap()

    def setPlayer(self, xCo, yCo):
        self.playerposition = (xCo,yCo)
        self.updateMap()

    #returns a function handeling a click at the coordinates x and y
    def getHandelerFunction(self,xCo, yCo):
        def function():
            self.handelClick(xCo,yCo)
        return function

    def openGameObjectSettings(self, x, y):
        self.settings.destroy()
        self.settings = Frame(self.window)
        self.settings.grid(row=0, column=1, sticky=NW)
        def okButtonFunction():
            if(not self.settings.selected):
                return
            self.settings.selectedObject[4] = [cuco.get() for cuco in self.settings.cuCoInput]
            self.settings.selectedObject[3] = [","+ self.settings.parameterLabels[a].cget("text")+"="+ self.settings.parameterInputFields[a].get() for a in range(len(self.settings.parameterLabels))]
            self.setGameObjectAt(x,y, self.settings.selectedObject[0], self.settings.selectedObject[3], self.settings.selectedObject[4])
            self.updateMap()
        def selectButtonFunction(event):
            if(self.settings.name.get()== "Empty"):
                self.deleteGameObjectAt(x,y)
                self.updateMap()
                self.openSettings(x,y)
                return
            self.settings.selected = True
            self.settings.selectedObject[0] = self.settings.name.get()
            self.settings.parameterLabels = []
            self.settings.parameterInputFields = []
            defaultParameterDict = getDefaultParameter(eval(self.settings.selectedObject[0]))
            if(not defaultParameterDict == {}): #if there are no defaultarguments return and do not offer this menu
                for key in defaultParameterDict:
                    self.settings.parameterLabels.append(Label(self.settings.ParameterInput,text=key))
                    self.settings.parameterLabels[-1].grid(row= len(self.settings.parameterLabels), column = 0)
                    self.settings.parameterInputFields.append(Entry(self.settings.ParameterInput))
                    default = defaultParameterDict.get(key, None)
                    self.settings.parameterInputFields[-1].insert(0,default)
                    self.settings.parameterInputFields[-1].grid(row= len(self.settings.parameterInputFields), column = 1)
                    print(key)
                #HeaderArguments
                self.settings.parameterInputHeader= Label(self.settings.ParameterInput,text='Arguments')
                self.settings.parameterInputHeader.grid(row=0,column = 0,columnspan=2)
            #CustomCOde
            def addCuCoInput():
                if(len(self.settings.cuCoInput) > 7):
                    return
                self.settings.cuCoInput.append( Entry(self.settings.CuCoInput))
                self.settings.cuCoInput[-1].grid(row=len(self.settings.cuCoInput)+1,columnspan=3)
            def removeCuCoInput():
                self.settings.cuCoInput[-1].destroy()
                del self.settings.cuCoInput[-1]
            self.settings.cuCoInput = []
            addCuCoInput()
            self.settings.cuCoInputHeader= Label(self.settings.CuCoInput,text='CustomCode')
            self.settings.cuCoInputHeader.grid(row=0,column = 0)
            self.settings.addCuCoButton = Button(self.settings.CuCoInput, text="+", command=addCuCoInput)
            self.settings.addCuCoButton.grid(row=0,column=1)
            self.settings.removeCuCoButton = Button(self.settings.CuCoInput, text="-", command=removeCuCoInput)
            self.settings.removeCuCoButton.grid(row=0,column=2)
            for cuco in self.settings.selectedObject[4]:
                self.settings.cuCoInput[-1].insert(0, cuco)
                if(cuco != self.settings.selectedObject[4][-1]):
                    addCuCoInput()

        self.settings.selected = False
        self.settings.ParameterInput = Frame(self.settings)
        self.settings.ParameterInput.grid(row = 3)
        self.settings.CuCoInput = Frame(self.settings)
        self.settings.CuCoInput.grid(row = 3,column=1)
        self.settings.selectedObject = self.getGameObjectAt(x,y)
        if(self.settings.selectedObject is None):
            self.settings.selectedObject = ["Empty",x,y,{},[]]
            self.settings.containing = False
        else:
            self.settings.containing = True
        self.settings.header = Label(self.settings,text="Editing the field: (" + str(x) + "|"+str(y)+")")
        self.settings.header.grid(row=0,sticky=NW)
        self.settings.description = Label(self.settings,text='Choose an Object')
        self.settings.description.grid(row=1,sticky=W)

        self.settings.name = StringVar()
        self.settings.name.set(self.settings.selectedObject[0])
        self.settings.dropdown_Object = OptionMenu(self.settings, self.settings.name,*self.possibleGameObjects,command=selectButtonFunction)
        self.settings.dropdown_Object.grid(row=2, column=0, sticky=W)
        self.settings.okButton = Button(self.settings, text="save", command=okButtonFunction)
        self.settings.okButton.grid(sticky=SW)
        if(self.settings.containing is True):
            selectButtonFunction()

    def openMobSettings(self, x, y):
        self.settings.destroy()
        self.settings = Frame(self.window)
        self.settings.grid(row=0, column=1, sticky=NW)
        def okButtonFunction():
            if(not self.settings.selected):
                return
            self.settings.selectedMob[4] = [cuco.get() for cuco in self.settings.cuCoInput]
            self.settings.selectedMob[3] = [","+ self.settings.parameterLabels[a].cget("text")+"="+ self.settings.parameterInputFields[a].get() for a in range(len(self.settings.parameterLabels))]
            self.setMobAt(x,y, self.settings.selectedMob[0], self.settings.selectedMob[3],self.settings.selectedMob[4])
            self.updateMap()
        def selectButtonFunction(event):
            if(self.settings.name.get()== "None"):
                self.deleteMobAt(x,y)
                self.updateMap()
                self.openSettings(x,y)
                return
            self.settings.selected = True
            self.settings.selectedMob[0] = self.settings.name.get()
            self.settings.parameterLabels = []
            self.settings.parameterInputFields = []
            defaultParameterDict = getDefaultParameter(eval(self.settings.selectedMob[0]))
            if(not defaultParameterDict == {}): #if there are no defaultarguments return and do not offer this menu
                for key in defaultParameterDict:
                    self.settings.parameterLabels.append(Label(self.settings.ParameterInput,text=key))
                    self.settings.parameterLabels[-1].grid(row= len(self.settings.parameterLabels), column = 0)
                    self.settings.parameterInputFields.append(Entry(self.settings.ParameterInput))
                    default = defaultParameterDict.get(key, None)
                    if(inspect.isclass(default)):
                        default = default.__class__.__name__
                    self.settings.parameterInputFields[-1].insert(0,defaultParameterDict.get(key, None))
                    self.settings.parameterInputFields[-1].grid(row= len(self.settings.parameterInputFields), column = 1)
                    print(key)
                #HeaderArguments
                self.settings.parameterInputHeader= Label(self.settings.ParameterInput,text='Arguments')
                self.settings.parameterInputHeader.grid(row=0,column = 0,columnspan=2)
            #CustomCode
            def addCuCoInput():
                if(len(self.settings.cuCoInput) > 7):
                    return
                self.settings.cuCoInput.append( Entry(self.settings.CuCoInput))
                self.settings.cuCoInput[-1].grid(row=len(self.settings.cuCoInput)+1,columnspan=3)
            def removeCuCoInput():
                self.settings.cuCoInput[-1].destroy()
                del self.settings.cuCoInput[-1]
            self.settings.cuCoInput = []
            addCuCoInput()

            self.settings.cuCoInputHeader= Label(self.settings.CuCoInput,text='CustomCode')
            self.settings.cuCoInputHeader.grid(row=0,column = 0)
            self.settings.addCuCoButton = Button(self.settings.CuCoInput, text="+", command=addCuCoInput)
            self.settings.addCuCoButton.grid(row=0,column=1)
            self.settings.removeCuCoButton = Button(self.settings.CuCoInput, text="-", command=removeCuCoInput)
            self.settings.removeCuCoButton.grid(row=0,column=2)
            for cuco in self.settings.selectedMob[4]:
                self.settings.cuCoInput[-1].insert(0, cuco)
                if(cuco != self.settings.selectedMob[4][-1]):
                    addCuCoInput()
        self.settings.selected = False
        self.settings.ParameterInput = Frame(self.settings)
        self.settings.ParameterInput.grid(row = 3)
        self.settings.CuCoInput = Frame(self.settings)
        self.settings.CuCoInput.grid(row = 3,column=1,sticky=N)
        self.settings.selectedMob = self.getMobAt(x,y)
        if(self.settings.selectedMob is None):
            self.settings.selectedMob = ["None",x,y,{},[]]
            self.settings.containing = False
        else:
            self.settings.containing = True
        self.settings.header = Label(self.settings,text="Editing the field: (" + str(x) + "|"+str(y)+")")
        self.settings.header.grid(row=0,sticky=NW)
        self.settings.description = Label(self.settings,text='Choose an Mob')
        self.settings.description.grid(row=1,sticky=W)

        self.settings.name = StringVar()
        self.settings.name.set(self.settings.selectedMob[0])
        self.settings.dropdown_Object = OptionMenu(self.settings, self.settings.name,*self.possibleMobs,command=selectButtonFunction)
        self.settings.dropdown_Object.grid(row=2, column=0,sticky=W)
        self.settings.okButton = Button(self.settings, text="save", command=okButtonFunction)
        self.settings.okButton.grid(sticky=SW)
        if(self.settings.containing is True):
            selectButtonFunction()

    def updateMap(self):
        #clears the map
        for x in self.buttonMap:
            for y in x:
                y.config(text="")
        #displays solid tiles as black and nosolid as white
        for x in range(len(self.buttonMap)):
            for y in range(len(self.buttonMap[0])):
                if( self.gameMap[x][y].isSolid is True):
                    self.buttonMap[x][y].config(bg="black")
                    self.buttonMap[x][y].config(fg="white")
                else:
                    self.buttonMap[x][y].config(bg="white")
                    self.buttonMap[x][y].config(fg="Black")

        #shows the playerposition
        self.buttonMap[self.playerposition[0]][self.playerposition[1]].config(text="P")
        #TODO: maybe add images
        if self.mode == 0:
            for gO in self.GameObjects:
                try:
                    self.buttonMap[gO[1]][gO[2]].image = PhotoImage(file="../../resources/" + gO[0]+"default.png")
                    self.buttonMap[gO[1]][gO[2]].config(image=self.buttonMap[gO[1]][gO[2]].image)
                except Exception:
                    self.buttonMap[gO[1]][gO[2]].config(text=gO[0][0])
        elif self.mode == 1:
            for mob in self.Mobs:
                try:
                    self.buttonMap[mob[1]][mob[2]].image = PhotoImage(file="../../resources/" + mob[0]+".png")
                    self.buttonMap[mob[1]][mob[2]].config(image=self.buttonMap[mob[1]][mob[2]].image)
                except Exception:
                    self.buttonMap[mob[1]][mob[2]].config(text=mob[0][0])


    #exports the edited map to the selected file by replacing [WallDeclarations], [ObjectDeclarations] and [MobDeclarations]
    def export(self):
        path = asksaveasfilename() #asks for a filepath
        print(path)
        #prepares Tiles
        resultMap = ""
        xCo = 0
        yCo = 0
        for x in self.gameMap:
            for y in x:
                if( self.gameMap[xCo][yCo].getIsSolid()):
                    resultMap += "gameMap[" + str(xCo) + "]["+str(yCo)+"] = Wall()\n"
                else:
                    resultMap += "gameMap[" + str(xCo) + "]["+str(yCo)+"] = Ground(Empty())\n"
                yCo = yCo + 1
            yCo = 0
            xCo = xCo + 1

        #prepares items and other gameobjects
        resultObjects =  ""
        for gO in self.GameObjects:
            resultObjects += "gameMap["+str(gO[1])+"]["+str(gO[2])+"].setGameObject("+str(gO[0])+'('+"".join(mob[3])+"))\n"
            for CustomCode in gO[4]:
                if not CustomCode.strip() == "":
                    resultObjects +="gameMap["+str(gO[1])+"]["+str(gO[2])+"].gameObject."+str(CustomCode)+"\n"
        #prepares Mobs
        resultMobs = ""
        for mob in self.Mobs:
            resultMobs += "mobs.append("+str(mob[0])+"("+str(mob[1])+", "+str(mob[2])+"".join(mob[3])+"))\n"
            for CustomCode in mob[4]:
                if not CustomCode.strip() == "":
                    resultMobs += "mobs[-1]."+str(CustomCode)+"\n"

        template = open('././resources/maps/levelTemplate.py', 'r').read() #opens the templete file
        updatedFile = template.split("[WallDeclarations]")[0]+ resultMap.replace("\n", "\n    ") + template.split("[WallDeclarations]")[1]
        updatedFile = updatedFile.split("[ObjectDeclarations]")[0]+ resultObjects.replace("\n", "\n    ") + updatedFile.split("[ObjectDeclarations]")[1]
        updatedFile = updatedFile.split("[MobDeclarations]")[0] + resultMobs.replace("\n", "\n    ") + updatedFile.split("[MobDeclarations]")[1]
        updatedFile = updatedFile.replace("<playerPositionX>", str(self.playerposition[0]))
        updatedFile = updatedFile.replace("<playerPositionY>", str(self.playerposition[1]))
        updatedFile = updatedFile.replace("<width>", str(len(self.gameMap[0])))
        updatedFile = updatedFile.replace("<height>", str(len(self.gameMap)))
        open(path,"w").write(updatedFile) #writes the edited file to filesystem


    #================Functions for editing mobs and gameobjects at specific places===========
    def getGameObjectAt(self, x,y):
        for gO in self.GameObjects:
            if(gO[1]== x and gO[2]== y):
                return gO
        return None

    def setGameObjectAt(self, x, y, name, customCodes):
        self.GameObjects.append([name,x,y,customCodes])
        self.updateMap()

    def deleteGameObjectAt(self,x,y):
        for gameobject in self.GameObjects:
            if(gameobject[1]== x and gameobject[2]== y):
                self.GameObjects.remove(gameobject)

    def getMobAt(self, x,y):
        for mob in self.Mobs:
            if(mob[1]== x and mob[2]== y):
                return mob
        return None

    def setMobAt(self, x, y, name, parameter, customCodes):
        if(name == "None"):
           self.deleteMobAt(x,y)
           return
        self.Mobs.append([name,x,y,parameter, customCodes])
        self.updateMap()

    def deleteMobAt(self,x,y):
         for mob in self.Mobs:
            if(mob[1]== x and mob[2]== y):
                self.Mobs.remove(mob)