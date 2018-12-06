"""
This module can be used to find the shortest
path between two points on a map.

To use the pathfinder first call the method pathfnder with the neighbors of your trust
(for the game this is gamemapNeighbors)
>>> finder = pathfinder(gamemapNeighbors)
>>> finder( (0,0), (1,1) )
(2, [(0, 0), (0, 1), (1, 1)])

The function can be cutomized via passing in functions to handle  your
particular implementation:
>>> finder = pathfinder( distance=absoluteDistance,
...                      cost=fixedCost(2),
...                      neighbors=gridNeighbors(10,10) );

"""

import math

'''
Calculate the distance between two points using the manhattan formula.
@param: start - the starting point
@param: end - the end point
'''
def manhattanDistance( start, end ):
    return abs( start[ 0 ] - end[ 0 ] ) + abs( start[ 1 ] + end[ 1 ] )

'''
Calculate the distance between two points using simple geometry.
@param: start - the starting point
@param: end - the end point
'''
def absoluteDistance( start, end ):
    return math.sqrt( ( start[0] - end[0] )**2 + ( start[1] - end[1] )**2 )

"""
Returns a fixed value for every input.
"""
def fixedCost( cost ):
    def func( a, b ):
        return cost
    return func

"""
Calculates neighbors for a simple grid where
a movement can be made up, down, left, or right.
@param: height - The height of the grid
@param: width - The width of the grid
"""
def gridNeighbors( height, width ):

    def func( coord ):
        neighbor_list = [ ( coord[ 0 ], coord[ 1 ] + 1),
                          ( coord[ 0 ], coord[ 1 ] - 1),
                          ( coord[ 0 ] + 1, coord[ 1 ]),
                          ( coord[ 0 ] - 1, coord[ 1 ])]

        return [ c for c in neighbor_list
                 if c != coord
                 and c[0] >= 0 and c[0] < width
                 and c[1] >= 0 and c[1] < height ]

    return func
"""
Returns a function that return the shortest path between 2 points.
@param: distance - Callable that returns the estimated distance
                        between two nodes.
@param: cost     - Callable that returns the cost to traverse
                        between two given nodes.
"""
def pathfinder( neighbors,
                distance=absoluteDistance,
                cost=fixedCost( 1 ) ):

    def reconstructPath( pastPlace, currentPlace ):
        if currentPlace in pastPlace:
            p = reconstructPath( pastPlace, pastPlace[ currentPlace ] )
            p.append( currentPlace )
            return p
        else:
            return [ currentPlace ]

    def func( start, end):
        openSet = set( [ start ] )
        closedSet = set()
        pastPlace = {}

        gScore = { start : 0 }
        fScore = { start : cost( start, end ) }

        while len( openSet ) != 0:
            current = min( openSet, key=lambda c: fScore[c] )

            if current == end:
                return reconstructPath( pastPlace, end )#gScore[ current ], reconstructPath( pastPlace, end )

            openSet.discard( current )
            closedSet.add( current )
            for neighbor in neighbors( current ):
                tentativeScore = gScore[ current ] + cost( current, neighbor )

                if neighbor in closedSet and ( neighbor in gScore and tentativeScore >= gScore[ neighbor ] ):
                    continue

                if neighbor not in openSet or ( neighbor in gScore and tentativeScore < gScore[ neighbor ] ):
                    pastPlace[ neighbor ] = current
                    gScore[ neighbor ] = tentativeScore
                    fScore[ neighbor ] = tentativeScore + distance( neighbor, end )

                    if neighbor not in openSet:
                        openSet.add( neighbor )

        return [] #None, []
    return func
'''
A function specificly designed for the game that only sees a field as a neighbor if it is not solid.
@param: height - te height of the gamemap
'''
def gamemapNeighbors( gameMap ):
        height = len(gameMap[0])
        width  = len(gameMap)
        def func( coord ):
            neighbor_list = [ ( coord[ 0 ], coord[ 1 ] + 1),
                            ( coord[ 0 ], coord[ 1 ] - 1),
                            ( coord[ 0 ] + 1, coord[ 1 ]),
                            ( coord[ 0 ] - 1, coord[ 1 ])]
            return [ c for c in neighbor_list
                    if c != coord
                    and c[0] >= 0 and c[0] < width
                    and c[1] >= 0 and c[1] < height
                    and not gameMap[c[0]][c[1]].getIsSolid()]
        return func