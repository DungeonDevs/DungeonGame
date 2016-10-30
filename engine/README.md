# PyEngine

The Python version of the engine for this game.

It is based on:
- PyOpenGL
- PyGame

Make sure you have these installed to run. (preferably with pip)

## Example usage

This creates a small game. It's a 5x5x5 field surrounded by walls, in which you
can move around freely with a red cube that is supposed to be the player.

	from Engine import Engine, Direction
	from classes.RenderObject import RenderObject

	import pygame

	# create an engine object
	engine = Engine()

	# create a ground object
	ground = RenderObject.createOneColorCube([.5, .5, .5])

	# create a wall object
	wall = RenderObject.createOneColorCube([.2, .2, .2])

	# create a default ground object and add it into engine
	engine.setGround(ground)

	# create a displayable player-object
	playerObj = RenderObject.createOneColorCube([1, 0, 0])
	playerObj.setScale(8)
	playerObj.setOffsets([.5 - float(1)/16, 0, .5 - float(1)/16])

	# create a game_map generator
	def genGameMap(playerX, playerY, playerObj):
		game_map = [
			[wall, wall, wall, wall, wall, wall, wall],
			[wall, None, None, None, None, None, wall],
			[wall, None, None, None, None, None, wall],
			[wall, None, None, None, None, None, wall],
			[wall, None, None, None, None, None, wall],
			[wall, None, None, None, None, None, wall],
			[wall, wall, wall, wall, wall, wall, wall]
			]
		game_map[playerY][playerX] = playerObj
		return game_map

	# create player-pos in middle of field and looking north
	player = [3, 3, Direction.NORTH]

	# create a game map
	game_map = genGameMap(player[0], player[1], playerObj)

	# inform engine of player and game_map
	engine.setMap(game_map)
	engine.setPlayerPosInfo(player[0], player[1], player[2])

	# start engine
	engine.startUp()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					# turn the player to the left
					player[2] = Direction.validate(player[2] - 1)
				if event.key == pygame.K_RIGHT:
					# turn the player to the right
					player[2] = Direction.validate(player[2] + 1)
				if event.key == pygame.K_UP:
					if player[2] == Direction.NORTH:
						player[1] -= 1
					if player[2] == Direction.SOUTH:
						player[1] += 1
					if player[2] == Direction.EAST:
						player[0] += 1
					if player[2] == Direction.WEST:
						player[0] -= 1
				if event.key == pygame.K_DOWN:
					if player[2] == Direction.NORTH:
						player[1] += 1
					if player[2] == Direction.SOUTH:
						player[1] -= 1
					if player[2] == Direction.EAST:
						player[0] -= 1
					if player[2] == Direction.WEST:
						player[0] += 1

				if player[0] < 1:
					player[0] = 1
				elif player[0] > 5:
					player[0] = 5

				if player[1] < 1:
					player[1] = 1
				elif player[1] > 5:
					player[1] = 5

				engine.setPlayerPosInfo(player[0], player[1], player[2])
				engine.setMap(genGameMap(player[0], player[1], playerObj))

		engine.render()

		pygame.time.wait(10)
