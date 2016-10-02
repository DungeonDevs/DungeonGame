from src.logic.main import TestEngine
from src.logic.maps.Map import Map


layout = Map(10, 10)
printer = TestEngine.Printer()
printer.display(layout.gameMap)