from importlib import import_module
x = import_module("resources.maps.level0")
#import resources.maps.level0 as x
print(x.getLevel())