import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from engine.classes.RenderObject import *
#
# A helper class to handle directions.
#TODO: Sync this direction Vaules with the ones used in the main game
#Files to edit: entitys.py; Game.py
class Direction(object):

	NORTH = 3
	EAST  = 2
	SOUTH = 1
	WEST  = 0

	#
	# Turns a possibly invalid direction into a valid one
	#
	@staticmethod
	def validate(direction):
		return direction % 4


#
# The interface to create a 3D representation of objects in a space.
#
# All interactions with this engine should work with this class.
#
class Engine(object):


	#
	# The three axes (x, y, z) defined as RenderObjects.
	#
	# Helpful for debugging and visualization.
	#
	__axes = (
		# x-axis
		RenderObject(
			[(-1,0,0), (200,0,0)], # vertices
			[(0,1,0)], # edges
			[], # no faces
			[(1,0,0)] # color : red
			),
		# y-axis
		RenderObject(
			[(0,-1,0), (0,200,0)], # vertices
			[(0,1,0)], # edges
			[], # no faces
			[(0,1,0)] # color : green
			),
		# z-axis
		RenderObject(
			[(0,0,-1), (0,0,200)], # vertices
			[(0,1,0)], # edges
			[], # no faces
			[(0,0,1)] # color : blue
			)
		)


	#
	# Constructor for an engine to display 3D objects in space. Create an object
	# of this class to interact with a 3D OpenGL view displayed with pygame.
	#
	# @param display : The size of the window and view. A list of two integers.
	# 				   Default: (800, 600)
	# @param p_map : A 2D-map of RenderObjects to display.
	# 				 Default: [[None]]
	#
	def __init__(self, display = (800, 600),
					   p_map = [[None]]):
		# initialize vars by params
		self.setMap(p_map)
		self.__display = display

		# initialize vars by standards
		self.debug = False


	#
	# This function initializes pygame and OpenGL. Call once before rendering
	# anything.
	#
	def startUp(self):
		pygame.init()
		pygame.display.set_mode(self.__display, DOUBLEBUF|OPENGL)

		# Set projection matrix
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()

		fieldOfView = 45 # degrees
		aspectRatio = self.__display[0] / self.__display[1]
		gluPerspective(fieldOfView, aspectRatio, 0.1, 50.0)

		# things in the back are covered by things in front of them
		glEnable(GL_DEPTH_TEST)

		# enable light - we need light to be able to make the environment look
		# somewhat natural and 3D-understandable
		glEnable(GL_LIGHTING)

		# materials for lighting
		glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
			# change both ambient and diffuse lighting with glColor
		glEnable(GL_COLOR_MATERIAL)

		# enable light source 0
		glEnable(GL_LIGHT0)

		# set up light source 0
		glLight(GL_LIGHT0, GL_AMBIENT, (.1, .1, .1, .1))
		glLight(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
		glLight(GL_LIGHT0, GL_POSITION, (10, 10, 10))


	#
	# This function renders the current map with the RenderObject it contains
	# and sets the camera to the position set by setPlayerPosInfo().
	#
	def render(self):
		# Clear OpenGL
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		# set up model-view matrix
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

		# set Camera position
		pos = self.getPlayerPosInfo()
		self.setCamera3rdPerson(pos[0], pos[1], pos[2])

		# render the objects in the map and ground where needed
		self.renderAllObjects()

		#
		# update is better, but does not work.
		# flip sadly produces an error on closing, but that is acceptable,
		# as the user does not notice this.
		#
		# pygame.display.update()
		pygame.display.flip()


	#
	# The current info of where the player is located in the game.
	# Returns as [x, z, direction]
	#
	def getPlayerPosInfo(self):
		return self.__playerPosInfo


	#
	# Set the player position and it's current viewing-direction.
	#
	# @param x : The x coordinate at which the player currently is.
	# @param z : The z coordinate at which the player currently is.
	# @param direction : The direction in which the player is currently looking.
	# 					 One of the directions specified in class Direction
	#
	def setPlayerPosInfo(self, x, z, direction):
		direction = Direction.validate(direction)
		self.__playerPosInfo = [x, z, direction]


	#
	# Renders the objects in the current map to OpenGL and ground where needed.
	#
	def renderAllObjects(self):
		# Display all RenderObjects and LoadedObjects in the map
		for z in range(len(self.getMap())):
			for x in range(len(self.getMap()[0])):
				obj = self.getMap()[z][x]
				if not obj == None:
					obj.render(x, 0, z)

					if obj.getGroundNecessary(): # render ground under object
												 # if needed
						self.getGround().render(x, -1, z)
				else: # render ground if no object
					self.getGround().render(x, -1, z)

		# in case debug is set to true, display the axis (x, y, z)
		if self.debug:
			for axis in Engine.__axis:
				axis.setRenderAsEdges()
				axis.setGroundNecessary(False)
				axis.render(0, 0, 0)


	#
	# Sets the camera to the correct position depending on where the player is.
	#
	# @param x : The x position at which the player currently is.
	# @param z : The z position at which the player currently is.
	# @param direction : The direction in which the player is currently looking.
	# 					 One of the in class Direction specified directions.
	#
	def setCamera3rdPerson(self, x, z, direction):
		direction = Direction.validate(direction)

		# deltas to the players location to move the camera away
		dY = 5#1.2 #.1
		dBack = 2 #1.2 #.5
		dLookatup = -.1

		# initialize vars
		playerV = [x,0,z] # player position
		eyeV    = playerV[:] # cam position (moving it starts at the player)
		centerV = playerV[:] # lookat point (is player)
		upV     = [0,1,0] # up vector

		centerV[1] += dLookatup

		eyeV[1] += dY

		if direction == Direction.NORTH:
			eyeV[2] += dBack
		elif direction == Direction.EAST:
			eyeV[0] -= dBack
		elif direction == Direction.SOUTH:
			eyeV[2] -= dBack
		elif direction == Direction.WEST:
			eyeV[0] += dBack

		self.setCameraPosition(eyeV, centerV, upV)


	#
	# Moves the camera to the desired absolute position in space.
	#
	# @param eyeV : The coordinates at which the camera should be positioned.
	# 				[x, y, z]
	# @param centerV : The coordinates at which the object the camera should
	# 				   point at is positioned. [x, y, z]
	# @param upV : The up-vector from the camera. Mostly [0, 1, 0]. [x, y, z]
	#
	def setCameraPosition(self, eyeV, centerV, upV):
		gluLookAt(eyeV[0] + .5, eyeV[1] + .5, eyeV[2] + .5,
				  centerV[0] + .5, centerV[1] + .5, centerV[2] + .5,
				  upV[0], upV[1], upV[2])


	#
	# Set the map that is to be rendered by the engine, containing the
	# required RenderObjects and LoadedObjects.
	#
	# @param p_map : A 2D-list containing the required RenderObjects,
	# 				 LoadedObjects and None-s to display the current game's
	# 				 state.
	#
	def setMap(self, p_map):
		self.__map = p_map


	#
	# The currently set map to display the game with
	#
	def getMap(self):
		return self.__map


	#
	# The ground that is currently being used to display under objects that
	# need a ground underneath them because they don't cover the whole field.
	# (RenderObject or LoadedObject)
	#
	def getGround(self):
		return self.__ground


	#
	# Set the ground to be used to display under objects that need a ground
	# underneath them because they don't cover the whole field.
	#
	# @param ground : A RenderObject or LoadedObject to display.
	#
	def setGround(self, ground):
		self.__ground = ground
