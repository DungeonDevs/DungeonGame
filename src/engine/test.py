#from input import key, Input
#InputManager = Input()
#if(InputManager.getInput() == key.left):
#print("left")
from engine import *
import time

ngn = engine()
t1 = time.time()
ngn.render([[ 0 for _ in range(5)] for _ in range(5)])
t2 = time.time()
print(t2 - t1)