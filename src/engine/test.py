#from input import key, Input
#InputManager = Input()
#if(InputManager.getInput() == key.left):
#print("left")
from engine import *
import time

ngn = engine()
print("initialised")
ngn.render([[ 0 for _ in range(5)] for _ in range(5)],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0]],0)
print("rendered")
time.sleep(2)
ngn.render([[ 0 for _ in range(5)] for _ in range(5)],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0]],0)