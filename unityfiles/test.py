
from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 4567, LoggingNamespace) as socketIO:
    print("connected")
    socketIO.emit('updateMap', {"map":"hello"})
    print("emmitted")

#socket = SocketIO('localhost', 4567, transports=['websocket'])
