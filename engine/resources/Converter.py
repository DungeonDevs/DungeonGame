def main():
	# read file
	ppf = PlyPyFile("block")
	verts, colors, faces = ppf.getData()

	verts = makeVertsPositiveInts(verts)

	verts, colors = minimizeColors(verts, colors)

	verts, faces = moveColorIndexToFace(verts, faces)

	verts, faces = minimizeVerts(verts, faces)

	(leftFaces, rightFaces, bottomFaces,
		topFaces, backFaces, frontFaces) = splitFaces(verts, faces)

	cubesLeft   = cubesFromFaces( verts, "left",   leftFaces   )
	cubesRight  = cubesFromFaces( verts, "right",  rightFaces  )
	cubesBottom = cubesFromFaces( verts, "bottom", bottomFaces )
	cubesTop    = cubesFromFaces( verts, "top",    topFaces    )
	cubesBack   = cubesFromFaces( verts, "back",   backFaces   )
	cubesFront  = cubesFromFaces( verts, "front",  frontFaces  )

	cubes = mergeCubeListsMinimized([
				cubesLeft,
				cubesRight,
				cubesBottom,
				cubesTop,
				cubesBack,
				cubesFront])

	cubes = turnObjectX(cubes)

	ppf.out("cubes = " + str(cubes))
	ppf.out("colors = " + str(colors))

	# write file
	ppf.write()


def turnObjectX(cubes):
	turnedCubes = []
	for cube in cubes:
		turnedCube = []
		turnedCube.append(cube[0])
		turnedCube.append(cube[2])
		turnedCube.append(cube[1])
		turnedCube.append(cube[3])
		turnedCubes.append(turnedCube)

	minz = turnedCubes[0][0]
	maxz = turnedCubes[0][0]
	for cube in turnedCubes:
		if cube[0] < minz:
			minz = cube[0]
		if cube[0] > maxz:
			maxz = cube[0]

	mirroredCubes = []
	for cube in turnedCubes:
		mirroredCube = []
		mirroredCube.append(cube[0])
		mirroredCube.append(cube[1])
		mirroredCube.append(maxz - cube[2])
		mirroredCube.append(cube[3])
		mirroredCubes.append(mirroredCube)

	return mirroredCubes


def mergeCubeListsMinimized(cubeLists):
	allCubes = mergeCubeLists(cubeLists)
	cubes = []

	for i, cube in enumerate(allCubes):
		try:
			iCube = cubes.index(cube)

			# cube exists in minimized list
		except ValueError:
			# cube does not exist in minimized list
			cubes.append(cube)


	return cubes


def mergeCubeLists(cubeLists):
	allCubes = []

	for cubeList in cubeLists:
		for cube in cubeList:
			allCubes.append(cube)

	return allCubes


def cubesFromFaces(verts, typeOfFaces, faces):
	cubes = []

	for face in faces:
		cube = []

		if typeOfFaces == "left":
			cube.append(getX(verts, face))
			cube.append(getMinY(verts, face))
			cube.append(getMinZ(verts, face))
		elif typeOfFaces == "right":
			x = getX(verts, face)
			if x <= 0:
				x += 1
			elif x > 0:
				x -= 1
			cube.append(x)
			cube.append(getMinY(verts, face))
			cube.append(getMinZ(verts, face))
		elif typeOfFaces == "bottom":
			cube.append(getMinX(verts, face))
			cube.append(getY(verts, face))
			cube.append(getMinZ(verts, face))
		elif typeOfFaces == "top":
			y = getY(verts, face)
			if y <= 0:
				y += 1
			elif y > 0:
				y -= 1
			cube.append(getMinX(verts, face))
			cube.append(y)
			cube.append(getMinZ(verts, face))
		elif typeOfFaces == "back":
			cube.append(getMinX(verts, face))
			cube.append(getMinY(verts, face))
			cube.append(getZ(verts, face))
		elif typeOfFaces == "front":
			z = getZ(verts, face)
			if z <= 0:
				z += 1
			elif z > 0:
				z -= 1
			cube.append(getMinX(verts, face))
			cube.append(getMinY(verts, face))
			cube.append(z)

		cube.append(face[4]) # color

		cubes.append(cube)

	return cubes


def getX(verts, face):
	return verts[face[0]][0]


def getY(verts, face):
	return verts[face[0]][1]


def getZ(verts, face):
	return verts[face[0]][2]


def getMinX(verts, face):
	minx = getX(verts, face) # set startpoint
	for iVert in face[:4]: # don't loop through color
		if verts[iVert][0] < minx:
			minx = verts[iVert][0]
	return minx


def getMinY(verts, face):
	miny = getY(verts, face) # set startpoint
	for iVert in face[:4]: # don't loop through color
		if verts[iVert][1] < miny:
			miny = verts[iVert][1]
	return miny


def getMinZ(verts, face):
	minz = getZ(verts, face) # set startpoint
	for iVert in face[:4]: # don't loop through color
		if verts[iVert][2] < minz:
			minz = verts[iVert][2]
	return minz


def splitFaces(verts, faces):
	totalNumFaces = len(faces)

	# set all to one more than possible
	firstBottomTopFace = totalNumFaces
	firstBackFrontFace = totalNumFaces

	for i, face in enumerate(faces):
		if (verts[face[0]][1] ==
			verts[face[1]][1] ==
			verts[face[2]][1] ==
			verts[face[3]][1]):
			# bottom/top
			if i < firstBottomTopFace:
				firstBottomTopFace = i
		elif (verts[face[0]][2] ==
			verts[face[1]][2] ==
			verts[face[2]][2] ==
			verts[face[3]][2]):
			# back/front
			if i < firstBackFrontFace:
				firstBackFrontFace = i

	numLeftRightFaces = firstBottomTopFace
	numBottomTopFaces = firstBackFrontFace - firstBottomTopFace
	numBackFrontFaces = totalNumFaces - firstBackFrontFace

	firstLeftFace   = 0
	firstRightFace  = int(numLeftRightFaces / 2)
	firstBottomFace = numLeftRightFaces
	firstTopFace    = numLeftRightFaces + int(numBottomTopFaces / 2)
	firstBackFace   = numLeftRightFaces + numBottomTopFaces
	firstFrontFace  = (numLeftRightFaces + numBottomTopFaces +
						int(numBackFrontFaces / 2))

	oneAfterLastLeftFace   = firstRightFace
	oneAfterLastRightFace  = firstBottomFace
	oneAfterLastBottomFace = firstTopFace
	oneAfterLastTopFace    = firstBackFace
	oneAfterLastBackFace   = firstFrontFace
	oneAfterLastFrontFace  = totalNumFaces

	leftFaces   = faces[ firstLeftFace   : oneAfterLastLeftFace   ]
	rightFaces  = faces[ firstRightFace  : oneAfterLastRightFace  ]
	bottomFaces = faces[ firstBottomFace : oneAfterLastBottomFace ]
	topFaces    = faces[ firstTopFace    : oneAfterLastTopFace    ]
	backFaces   = faces[ firstBackFace   : oneAfterLastBackFace   ]
	frontFaces  = faces[ firstFrontFace  : oneAfterLastFrontFace  ]

	return leftFaces, rightFaces, bottomFaces, topFaces, backFaces, frontFaces


def minimizeVerts(allVerts, faces):
	verts = []
	for i, vert in enumerate(allVerts):
		try:
			iVert = verts.index(vert)

			# vert exists in minimized list
			faces[i // 4][i % 4] = iVert
		except ValueError:
			# vert does not exist in minimized list
			verts.append(vert)
			faces[i // 4][i % 4] = len(verts) - 1

	return verts, faces


def moveColorIndexToFace(verts, faces):
	for iFace, face in enumerate(faces):
		faceVerts = verts[face[0]:face[3]+1]

		color = faceVerts[0][3]
		if not (color ==
				faceVerts[1][3] ==
				faceVerts[2][3] ==
				faceVerts[3][3]):
			print("Error: moveColorIndexToFace() has to be called before " +
					"minimizing verts.")
			quit()

		faces[iFace].append(color) # append color to face

		for iVertSmall, vert in enumerate(faceVerts):
			iVert = iVertSmall + face[0]
			verts[iVert] = verts[iVert][:3] # remove color from vert


	return verts, faces


def minimizeColors(verts, allColors):
	colors = []
	for i, color in enumerate(allColors):
		try:
			iColor = colors.index(color)

			# color exists in minimized list
			verts[i][3] = iColor
		except ValueError:
			# color does not exist in minimized list
			colors.append(color)
			verts[i][3] = len(colors) - 1

	return verts, colors


def makeVertsPositiveInts(verts):
	# if bigger or equal to 0, don't change it
	minx = 0
	miny = 0
	minz = 0
	offsetX = 0
	offsetY = 0
	offsetZ = 0

	for vert in verts:
		if vert[0] < minx:
			minx = vert[0]
		if vert[1] < miny:
			miny = vert[1]
		if vert[2] < minz:
			minz = vert[2]

		if not vert[0] % 1 == 0:
			offsetX = vert[0] // 1
		if not vert[1] % 1 == 0:
			offsetY = vert[0] // 1
		if not vert[2] % 1 == 0:
			offsetZ = vert[0] // 1

	# deltas to change all vert's components by (standard 0)
	dx = offsetX
	dy = offsetY
	dz = offsetZ

	if minx < 0:
		# add minx to all vert's x components
		dx = -minx

	if miny < 0:
		dy = -miny

	if minz < 0:
		dz = -minz

	positiveVerts = []
	for vert in verts:
		vert[0] = int(vert[0] + dx)
		vert[1] = int(vert[1] + dy)
		vert[2] = int(vert[2] + dz)
		positiveVerts.append(vert)

	return positiveVerts


class PlyPyFile(object):

	# standard values
	PATH_FROM = "resources/originals/"
	PATH_TO   = "resources/"
	FILENAME  = "test"

	def __init__(self, filename = FILENAME,
					pathFrom = PATH_FROM,
					pathTo = PATH_TO,
					outToConsole = False):
		self.filename = filename
		self.pathFrom = pathFrom
		self.pathTo = pathTo
		self.outToConsole = outToConsole

		self.output = ""


	def getData(self):
		# open .ply-file read-only
		f_ply = open(self.pathFrom + self.filename + ".ply", 'r')

		# get number of vertices and faces and loop through header
		num_verts = 0
		num_faces = 0
		line = ""
		while line != "end_header\n":
			line = f_ply.readline()
			if line[0:15] == "element vertex ":
				num_verts = int(line[15:])
			if line[0:13] == "element face ":
				num_faces = int(line[13:])

		# append all vertices to verts
		verts = []
		colors = []
		for i in range(num_verts):
			line = f_ply.readline()[:-1].split()

			# split vertices and colors
			vert  = [float(line[0]), float(line[1]), float(line[2]), i]
			color = [int(line[3]) / 255,
						int(line[4]) / 255,
						int(line[5]) / 255]

			verts.append(vert)
			colors.append(color)

		# append all faces to faces
		faces = []
		for i in range(num_faces):
			# convert to array
			face = f_ply.readline()[2:-1].split()
			# convert strings to integers
			for i, v in enumerate(face):
				face[i] = int(v)
			# append to face-list
			faces.append(face)

		return verts, colors, faces


	def out(self, data):
		if self.outToConsole:
			print(data)
		self.output += str(data) + "\n"


	def write(self):
		open(self.pathTo + self.filename + ".py", 'w').write(self.output)
		self.output = ""


main()
