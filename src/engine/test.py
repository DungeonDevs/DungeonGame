'''

import time

def handeler(x):
    print(x)
    time.sleep(1)
    i.setInputCallback(Input.__dump)
    global wait
    wait = False
i = Input(handeler)
print("hi")
wait = True
while(wait):
    print("waiting")
print("ending now")
'''

from input import key, Input

InputManager = Input()
if(InputManager.getInput() == key.left):
    print("left")

