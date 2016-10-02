class textLoader():
    def __init__(self, defaultData = ''):
        self.files = dict()
        self.defaultData = defaultData

    def load(self, path):
        try:
            data = open(path,"r")
            self.files[path] = data.read()
        except:
            data = open(self.defaultData,"r")
            self.files[path] = data.read()
        return self.files[path]

    #returnd die Datein die unter dem Pfad eingetragen ist. Sollte der Pfad noch nicht geladen sein wird er geladen. Wenn keine Datei gefunden wird wird die Standarddatei geladen
    def getFile(self, path):
        if(path in self.files):
            return self.files.get(path)
        else:
            return self.load(path)

    #löscht alle geladenen Datein aus dem Ram
    def clean(self):
        self.files.clear()

    #laedt den angegebenen Pfad neu
    def reload(self, path):
        self.load(path)

    #blocking - laedt alle Datein neu ACHTUNG! Bei vielen Bildern kann dies lange dauern! Sollte dies der Fall sein nutze die Async Methode!
    def reloadAllSync(self):
        for path in self.files:
            self.load(path)

    #non-blocking - laedt alle Datein neu
    def reloadAllAsync(self):
        from threading import Thread
        self.__relaodAllAsyncExecutor = Thread()
        self.__reloadAllAsyncExecutor = Thread(target=self.__reloadAllAsyncExecutor).start()

    def __reloadAllAsyncExecutor(self):
        for path in self.files:
            self.load(path)