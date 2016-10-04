from socketIO_client import SocketIO
print("gestartet")
socketIO = SocketIO('localhost', port=4567, transports='websocket',E)
print("connected")
socketIO.emit('updateMap', {"map":"hallo"})
print("emmitted")
