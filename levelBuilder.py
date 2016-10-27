from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import Dialog
from src.logic.main.Map import *
from src.logic.objects.Monsters import *
import threading
import os

class Levelbuilder():
    def __init__(self,width, height):
        self.GameObjects = ["Empty","Sword"] # A list of all possible GameObjects
        self.Mobs = ["Monster","Hunter"] # A list of all possible GameObjects
        self.Objects =[]
        self.mobs = []
        self.window = Tk()
        self.window.title('Levelbuilder')
        self.window.minsize(600,400)
        self.window.maxsize(1280,720)
        #PrepareMap
        self.map = Frame(self.window)
        self.map.grid(row=0, column=0)
        self.gameMap = MapHandler().createMap(width,height)

        self.buttonMap = [[None for _ in range(width)] for _ in range(height)]
        xCo = 0
        yCo = 0
        for x in self.gameMap:
            yCo = 0
            for y in x:
                f = Frame(self.map, height=32, width=32)
                f.pack_propagate(0) # don't shrink
                f.grid(row=yCo, column=xCo)
                self.buttonMap[xCo][yCo] = Button(f, command = self.getFunction(xCo,yCo), height=2, width = 2)
                self.buttonMap[xCo][yCo].bind('<Button-3>', lambda event,xVal=xCo, yVal=yCo: self.setWall(xVal,yVal)) #self.getFunctionSetWall(xCo,yCo))
                self.buttonMap[xCo][yCo].pack(fill=BOTH, expand=1)
                #self.buttonMap[xCo][yCo].grid(row=yCo, column=xCo)
                yCo = yCo + 1
            xCo = xCo + 1
        #select waht to show
        self.radiogroup = Frame(master=self.window)
        self.display = IntVar()
        self.display.set(0)
        self.GameObjects_radiobutton = Radiobutton(master=self.radiogroup,
                                              text='Display GameObjects',
                                              font=('Arial',10),
                                              value='0', variable=self.display,
                                              command=self.updateMap)
        self.GameObjects_radiobutton.select()
        self.GameObjects_radiobutton.grid(row=0, column=0)
        self.Mobs_radiobutton = Radiobutton(master=self.radiogroup,
                                              text='Display Mobs',
                                              font=('Arial',10),
                                              value='1', variable=self.display,
                                              command=self.updateMap)
        self.Mobs_radiobutton.grid(row=0, column=1)
        self.radiogroup.grid(row=1)
        self.updateMap()
        #PrepareSettings
        self.settings = Frame(self.window)
        self.settings.grid(row=0, column=1, sticky=E)

        #Menubar
        self.menubar = Menu(self.window)
        self.menubar.add_command(label="save", command=self.save)
        self.menubar.add_command(label="Quit!", command=self.window.quit)
        self.window.config(menu=self.menubar)

        self.window.mainloop()
    def setWall(self, xCo, yCo):
        #def function():
        self.gameMap[xCo][yCo].isSolid = not self.gameMap[xCo][yCo].isSolid
        self.updateMap()
        #return function

    def getFunction(self,xCo, yCo):
        def function():
            self.openSettings(xCo,yCo)
        return function

    def openSettings(self, x, y):
        print("open settings")
        self.settings.destroy()
        self.settings = Frame(self.window)
        self.settings.grid(row=0, column=1, sticky=E)
        if(self.display.get() == 0):
            def okButtonFunction():
                self.selectedObject[0] = self.settings.name.get()
                self.selectedObject[3] = [cuco.get() for cuco in self.settings.cuCoInput]
                self.setGameObjectAt(x,y, self.selectedObject[0], self.selectedObject[3])
                self.cleanGameObjectsList()
                self.updateMap()
            def selectButtonFunction():
                if(self.settings.name.get() == "Empty"):
                    return
                '''
                def addArgsInput():
                    self.settings.argsInput.append( Entry(self.settings.ParameterInput))
                    self.settings.argsInput[-1].grid(row=len(self.settings.argsInput)+1,columnspan=3)
                def removeArgsInput():
                    self.settings.argsInput[-1].destroy()
                    del self.settings.argsInput[-1]
                self.settings.argsInput = []
                addArgsInput()
                #HeaderArguments
                self.settings.argsInputHeader= Label(self.settings.ParameterInput,text='Arguments', font=('Arial',10))
                self.settings.argsInputHeader.grid(row=0,column = 0)
                self.settings.addArgsButton = Button(self.settings.ParameterInput, text="+", command=addArgsInput)
                self.settings.addArgsButton.grid(row=0,column=1)
                self.settings.removeArgsButton = Button(self.settings.ParameterInput, text="-", command=removeArgsInput)
                self.settings.removeArgsButton.grid(row=0,column=2)
                '''
                #CustomCOde
                def addCuCoInput():
                    self.settings.cuCoInput.append( Entry(self.settings.CuCoInput))
                    self.settings.cuCoInput[-1].grid(row=len(self.settings.cuCoInput)+1,columnspan=3)
                def removeCuCoInput():
                    self.settings.cuCoInput[-1].destroy()
                    del self.settings.cuCoInput[-1]
                self.settings.cuCoInput = []
                addCuCoInput()
                #HeaderArguments
                self.settings.cuCoInputHeader= Label(self.settings.CuCoInput,text='CustomCode', font=('Arial',10))
                self.settings.cuCoInputHeader.grid(row=0,column = 0)
                self.settings.addCuCoButton = Button(self.settings.CuCoInput, text="+", command=addCuCoInput)
                self.settings.addCuCoButton.grid(row=0,column=1)
                self.settings.removeCuCoButton = Button(self.settings.CuCoInput, text="-", command=removeCuCoInput)
                self.settings.removeCuCoButton.grid(row=0,column=2)
                for cuco in self.selectedObject[3]:
                    self.settings.cuCoInput[-1].insert(0, cuco)
                    if(cuco != self.selectedObject[3][-1]):
                        addCuCoInput()

            self.settings.ParameterInput = Frame(self.settings)
            self.settings.ParameterInput.grid(row = 2)
            self.settings.CuCoInput = Frame(self.settings)
            self.settings.CuCoInput.grid(row = 2,column=1)
            self.selectedObject = self.getGameObjectAt(x,y)
            if(self.selectedObject is None):
                self.selectedObject = ["Empty",x,y,[]]
                self.settings.containing = False
            else:
                self.settings.containing = True
            self.settings.name = StringVar()
            self.settings.name.set(self.selectedObject[0])
            self.settings.description = Label(self.settings,text='Choose an Object', font=('Arial',10))
            self.settings.description.grid(row=0)
            self.settings.dropdown_Object = OptionMenu(self.settings, self.settings.name,*self.GameObjects)
            self.settings.dropdown_Object.grid(row=1, column=0)


            self.settings.selectButton = Button(self.settings, text="select", command=selectButtonFunction)
            self.settings.selectButton.grid(row=1, column=1)
            self.settings.okButton = Button(self.settings, text="saveChanges", command=okButtonFunction)
            self.settings.okButton.grid(sticky=SW)
            if(self.settings.containing is True):
                selectButtonFunction()
        else:
            pass
    def getGameObjectAt(self, x,y):
        for gO in self.Objects:
            if(gO[1]== x and gO[2]== y):
                return gO
        return None

    def setGameObjectAt(self, x, y, name, customCodes):
        self.Objects.append([name,x,y,customCodes])
        self.updateMap()

    def cleanGameObjectsList(self):
        for a in range(len(self.Objects)):
             if(isinstance(self.Objects[a][1], Empty)):
                del self.Objects[a]
        '''
        for gO in self.Objects:
            if(isinstance(gO[1], Empty)):
                self.Objects.remove(gO)
        '''

    def updateMap(self):
        xCo = 0
        yCo = 0
        for x in self.buttonMap:
            for y in x:
                if( self.gameMap[xCo][yCo].isSolid is True):
                    self.buttonMap[xCo][yCo].config(bg="black")
                    self.buttonMap[xCo][yCo].config(fg="white")
                else:
                    self.buttonMap[xCo][yCo].config(bg="white")
                    self.buttonMap[xCo][yCo].config(fg="Black")
                yCo = yCo + 1
            yCo = 0
            xCo = xCo + 1
        if self.display.get() == 0:
            for gO in self.Objects:
                try:
                    self.buttonMap[gO[1]][gO[2]].image = PhotoImage(file="resources/" + gO[0]+"default.png")
                    self.buttonMap[gO[1]][gO[2]].config(image=self.buttonMap[gO[1]][gO[2]].image)
                except Exception:
                    self.buttonMap[gO[1]][gO[2]].config(text="G")
        else:
            for mob in self.mobs:
                try:
                    self.buttonMap[mob[1]][mob[2]].image = PhotoImage(file="resources/" + mob[0]+".png")
                    self.buttonMap[mob[1]][mob[2]].config(image=self.buttonMap[mob[1]][mob[2]].image)
                except Exception:
                    self.buttonMap[mob[1]][mob[2]].config(text="M")
    def save(self):
        path = asksaveasfilename()
        print(path)
        resultMap = ""
        xCo = 0
        yCo = 0
        for x in self.gameMap:
            for y in x:
                if( self.gameMap[xCo][yCo].getIsSolid is True):
                    resultMap += "gameMap[" + str(xCo) + "]["+str(yCo)+"] = Wall()\n"
                else:
                    resultMap += "gameMap[" + str(xCo) + "]["+str(yCo)+"] = Ground()\n"
                yCo = yCo + 1
            yCo = 0
            xCo = xCo + 1
        #Items and other Gameobjects
        resultObjects =  ""
        for gO in self.Objects:
            resultObjects += "gameMap["+str(gO[1])+"]["+str(gO[2])+"].setGameObject("+str(gO[0])+"())\n"
            if not (gO[3] is None):
                for CustomCode in gO[3]:
                    resultObjects +="gameMap["+str(gO[1])+"]["+str(gO[2])+"].gameObject."+str(CustomCode)+"\n"
        #mobs
        resultMobs = ""
        for mob in self.mobs:
            if(mob[4] is None): # if there are no special arguments
                resultMobs += "mobs.append("+"mob[0]"+"("+str(mob[1])+", "+str(mob[2])+", "+str(mob[3])+"))\n"
            else:
                resultMobs += "mobs.append("+"mob[0]"+"("+str(mob[1])+", "+str(mob[2])+", "+str(mob[3])+",*"+str(mob[4])+"))\n"
            if not (go[2] is None):
                for CustomCode in go[2]:
                    resultMobs += "mobs[-1]."+str(CustomCode)+"\n"

        template = open('resources/maps/levelTemplate.py', 'r').read()
        updatedFile = template.split("[WallDeclarations]")[0]+ resultMap.replace("\n", "\n    ") + template.split("[WallDeclarations]")[1]
        updatedFile = updatedFile.split("[ObjectDeclarations]")[0]+ resultObjects.replace("\n", "\n    ") + updatedFile.split("[ObjectDeclarations]")[1]
        updatedFile = updatedFile.split("[MobDeclarations]")[0] + resultMobs.replace("\n", "\n    ") + updatedFile.split("[MobDeclarations]")[1]
        open(path,"w").write(updatedFile)

level = Levelbuilder(20,10)