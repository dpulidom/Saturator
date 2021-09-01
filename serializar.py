import socket
import pickle

s = socket.socket()
data = [1, 2 ,3 ,4]
objectBytes = pickle.dumps(data)
s.connect(("localhost", 2016))
s.send(objectBytes)
s.close()
