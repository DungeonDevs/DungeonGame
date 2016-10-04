from pyhooked import Hook, KeyboardEvent, MouseEvent
import threading
from enum import Enum

class Input():
    def __init__(self):
        self.hook = hookWrapper()
    def getInput(self):
        self.hook.setInputCallback(self.get)
        self.input = None
        self.hook.openInput()
        print("waiting")
        while self.input is None:
            pass
        return self.input

    def get(self, x):
        self.input = x

#an Enum with all inputkeys which shall call the self.callback function
class key(Enum):
        left = 0
        right = 1
        up = 2
        down = 3
#loccally used class - DO NOT USE!
class hookWrapper():
    '''
    @param callback: the callback to be called with the pressed key from of the keyEnum.
    @param startNow: says whether the input should start immediately
    '''
    def __init__(self, callback=None, startNow= True):
        self.open = startNow
        #if no callback is given on instantiation, the callback is set to an empty function
        if(callback is None):
            self._inputCallback = hookWrapper.__dump
        else:
            self._inputCallback = callback

        self.hk = Hook() #instantiates a new Input
        self.hk.handler = self.handleEvents #sets the eventhandeler to the handleEvent function

        self.thread = threading.Thread(target=self.hk.hook) # creates a new thread for the Input so the Input wouldn´t block the main code
        self.thread.daemon = True
        self.thread.start()

    @staticmethod
    def __dump(x):
        pass
    #@param callback: the _inputCallback is set to this param
    def setInputCallback(self, callback):
        self._inputCallback = callback
    #starts listening to input
    def openInput(self):
        self.open = True
    #stops listening to input
    def closeInput(self):
        self.open = False
    #calls the callback and closes the Input
    #for internal use only
    def __callInputCallback(self, data, closeInput=True):
        if closeInput:
            self.closeInput()
        self._inputCallback(data)
    #function handelling the inputs given by the pyhooked library
    def handleEvents(self, args):
        #print("got Input")
        if(self.open):
            if isinstance(args, KeyboardEvent):
                #print(args.key_code)
                if args.current_key == 'Left': #and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key
                    self.__callInputCallback(key.left)
                elif args.current_key == 'Right':
                    self.__callInputCallback(key.right)
                elif args.current_key == 'Up': #and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key
                    self.__callInputCallback(key.up)
                elif args.current_key == 'Down':
                    self.__callInputCallback(key.down)