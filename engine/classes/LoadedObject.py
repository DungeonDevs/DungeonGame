from .RenderObject import RenderObject

import importlib

#
# A class to load external objects converted to .py files into the engine and
# render them.
#
# A loadable file has to contain two variables called "cubes" and "colors".
#
# The variable "cubes" is an array of arrays, containing the position of cubes
# that form the object, as well as the index of the color the cube is supposed
# to have.
# cubes = [[x, y, z, c_index], ...]
#
# The variable "colors" is an array of arrays, containing the components that
# make out the different colors needed to display the object. Each component
# has to be in range [0;1].
# colors = [[r, g, b], ...]
#
class LoadedObject(object):


	#
	# The constructor to create a LoadedObject.
	# A LoadedObject is used to load external objects from .py files to display
	# them in the engine.
	#
	# @param filename : The filename (without ending!) and path of the file in
	# 					which the information of the object to load are saved.
	# 					Note: the file will be imported as a python-module, so
	# 					the path has to be written with "."s instead of "/"s or
	# 					"\"s, and the file has to be accessible accordingly.
	# 					The path starts at whatever level the program is being
	# 					executed from.
	# @param scale : The scale in which the cubes specified in the file should
	# 				 be rendered in. The number specifies how many cubes of the
	# 				 object fit into one "normal" 1x1x1 cube in one axis.
	# 				 Default: 64
	# @param offsets : The offset at which the object should be rendered at,
	# 				   relative to the position given.
	# 				   Default: (0, 0, 0)
	#
	def __init__(self, filename, scale = 64, offsets = (0,0,0)):
		self.setScale(scale)
		self.setOffsets(offsets)
		self.setFilename(filename) # calls self.__updateRenderObjects()

		self.setGroundNecessary(True)
		self.setRenderAsEdges(False)


	#
	# Renders this LoadedObject by rendering all RenderObjects created to
	# represent the cubes in the object at offsets relative to the given
	# location.
	#
	# @param x : The x coordinate at which the object should be rendered.
	# @param y : The y coordinate at which the object should be rendered.
	# @param z : The z coordinate at which the object should be rendered.
	#
	def render(self, x, y, z):
		for obj in self.__renderObjects:
			offsets = self.getOffsets()
			pos = [x + offsets[0],
				   y + offsets[1],
				   z + offsets[2]]
			obj.render(pos[0],
					   pos[1],
					   pos[2])


	#
	# Set the filename and path of the file that contains the info for this
	# object. Note: The file will also be read and interpreted on call of this
	# method, so don't use unnecessarily often.
	#
	# Note: the file will be imported as a python-module, so
	# the path has to be written with "."s instead of "/"s or
	# "\"s, and the file has to be accessible accordingly.
	# The path starts at whatever level the program is being
	# executed from.
	#
	# @param filename : The path to and the name of the file (without ending!)
	# 					that contains info to this object.
	#
	def setFilename(self, filename):
		self.__filename = filename
		self.__updateRenderObjects()


	#
	# The path and filename to the file containing info for this object, as
	# set.
	#
	# Note: the file will be imported as a python-module, so
	# the path has to be written with "."s instead of "/"s or
	# "\"s, and the file has to be accessible accordingly.
	# The path starts at whatever level the program is being
	# executed from.
	#
	def getFilename(self):
		return self.__filename


	#
	# Set the scale at which this object should be rendered.
	#
	# The higher the number, the smaller the object. A scale of 1 means that one
	# cube of this object fits into one "normal" 1x1x1 cube. A scale of i.e. 4
	# means that on each axis there are up to four spots for a cube of this
	# object in a "normal" 1x1x1 cube, making a total of 4*4*4=64 cubes.
	#
	# The default value set by the constructor is 64.
	#
	# @param scale : The scale at which cubes of this object should be
	# 				 rendered in.
	#
	def setScale(self, scale):
		self.__scale = scale


	#
	# The scale at which cubes of this object should be rendered in.
	#
	# The higher the number, the smaller the object. A scale of 1 means that one
	# cube of this object fits into one "normal" 1x1x1 cube. A scale of i.e. 4
	# means that on each axis there are up to four spots for a cube of this
	# object in a "normal" 1x1x1 cube, making a total of 4*4*4=64 cubes.
	#
	def getScale(self):
		return self.__scale


	#
	# Set the offset relative to the given position at which this object should
	# be rendered at.
	#
	# The default value set by the constructor is (0,0,0)
	#
	# @param offsets : A vertex to add to each vertex that describes this
	# 				   object so that it is off-set by the given amount.
	# 				   [x, y, z]
	#
	def setOffsets(self, offsets):
		self.__offsets = offsets


	#
	# The offsets relative to the given position at which this object should be
	# rendered at.
	# [x, y, z]
	#
	def getOffsets(self):
		return self.__offsets


	#
	# Set whether the default ground should be displayed under this object.
	# If the object covers the whole ground it should be set to false, otherwise
	# it should be set to true.
	#
	# @param necessary : Whether or not ground is necessary to be rendered.
	#
	def setGroundNecessary(self, necessary):
		self.__groundNecessary = necessary


	#
	# A boolean describing whether or not it is necessary to display ground
	# underneath this object. Usually objects that do not cover the ground
	# underneath them have this as true, if they do cover the ground it is
	# false to save render time.
	#
	def getGroundNecessary(self):
		return self.__groundNecessary


	#
	# Set whether the object should be rendered as edges only, or faces only
	# (default).
	#
	# @param renderAsEdges : A boolean describing whether the object should be
	# 						 rendered as edges only. True is edges, false is
	# 						 faces.
	# 						 Default: false
	#
	def setRenderAsEdges(self, renderAsEdges):
		self.__renderAsEdges = renderAsEdges

		for obj in self.__renderObjects:
			obj.setRenderAsEdges(renderAsEdges)


	#
	# A boolean describing whether this object will be rendered as edges only
	# (true) or faces only (false).
	# Default: false
	#
	def getRenderAsEdges(self):
		return self.__renderAsEdges


	#
	# Load the file specified that contains the info for this object and change
	# the object accordingly.
	#
	def __updateRenderObjects(self):
		cubes  = []
		colors = []

		varfile = importlib.import_module(self.getFilename())

		cubes  = varfile.cubes
		colors = varfile.colors

		# create the RenderObjects needed and add them to the local list
		self.__renderObjects = []
		for cube in cubes:
			c_obj = RenderObject.createOneColorCube(colors[cube[3]])
			c_obj.setScale(self.getScale())
			offsets = [float(cube[0]) / self.getScale(),
					   float(cube[1]) / self.getScale(),
					   float(cube[2]) / self.getScale()]
			c_obj.setOffsets(offsets)

			self.__renderObjects.append(c_obj)
