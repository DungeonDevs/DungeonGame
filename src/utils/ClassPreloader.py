from engine.classes.LoadedObject import *
class ClassLoader():
    def __init__(self, defaultData=LoadedObject("engine.resources.block", 16)):
        self.files = dict()
        self.defaultData = defaultData

    def load(self, path, size):
        try:
            self.files[path] = LoadedObject(path, size)
        except:
            self.files[path] = self.defaultData
        return self.files[path]

    #returns die Datein die unter dem Pfad eingetragen ist. Sollte der Pfad noch nicht geladen sein wird er geladen. Wenn keine Datei gefunden wird wird die Standarddatei geladen
    def getFile(self, path, size):
        if(path in self.files):
            return self.files.get(path)
        else:
            return self.load(path, size)

    #löscht alle geladenen Datein aus dem Ram
    def clean(self):
        self.files.clear()

    #@deplaced
    #laedt den angegebenen Pfad neu
    def __reload(self, path,size):
        self.load(path,size)

    #@deplaced
    #blocking - laedt alle Datein neu ACHTUNG! Bei vielen Bildern kann dies lange dauern! Sollte dies der Fall sein nutze die Async Methode!
    def __reloadAllSync(self):
        for path in self.files:
	        self.load(paths)

    #@deplaced
    #non-blocking - laedt alle Datein neu
    def __reloadAllAsync(self):
        from threading import Thread
        self.__relaodAllAsyncExecutor = Thread()
        self.__reloadAllAsyncExecutor = Thread(target=self.__reloadAllAsyncExecutor).start()

    #@deplaced
    def __reloadAllAsyncExecutor(self):
        for path in self.files:
	        self.load(path)