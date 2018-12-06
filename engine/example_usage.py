from engine.Engine import Engine, Direction
from engine.classes.RenderObject import RenderObject
from engine.classes.LoadedObject import LoadedObject

import pygame

# -------------------------------------------
# create a ground
ground = RenderObject.createOneColorCube((150/255, 75/255, 0))

# -------------------------------------------
# create three cubes

cube1 = RenderObject()
cube1.setGroundNecessary(False)
cube1.setRenderAsEdges()

cube2 = RenderObject()
cube2.setGroundNecessary(False)
cube2.setRenderAsEdges()

cube3 = RenderObject()
cube3.setGroundNecessary(False)
cube3.setRenderAsEdges()

# -------------------------------------------
# create object from file
loadedObj = LoadedObject("engine.resources.block", 16)
loadedObj.setOffsets((.5, 0, -.5))
# loadedObj.setScale(2)

# -------------------------------------------
# create engine object
engine = Engine((600, 400))
# engine.debug = True # to show axis

# -------------------------------------------
# set ground
engine.setGround(ground)

# -------------------------------------------
# start engine
engine.startUp()

# -------------------------------------------
# create map
my_map = (
	(None, None, None, cube1, cube2, cube3),
	(loadedObj, None, None, None, None, None)
	)

# -------------------------------------------
# render map
engine.setMap(my_map)
engine.setPlayerPosInfo(0, 1, Direction.EAST)
engine.render()

# -------------------------------------------
# keep program alive until close-event
while True:
	# TODO: give engine this functionality
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	pygame.time.wait(1000)
