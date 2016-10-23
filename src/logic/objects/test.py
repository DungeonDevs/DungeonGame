import astar
walls = [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
def grid_neighbors( height, width ):
    def func( coord ):
        neighbor_list = [ ( coord[ 0 ], coord[ 1 ] + 1),
                          ( coord[ 0 ], coord[ 1 ] - 1),
                          ( coord[ 0 ] + 1, coord[ 1 ]),
                          ( coord[ 0 ] - 1, coord[ 1 ])]

        return [ c for c in neighbor_list
                 if c != coord
                 and c[0] >= 0 and c[0] < width
                 and c[1] >= 0 and c[1] < height
                 and not walls[c[0]][c[1]] == 1]

    return func

finder = astar.pathfinder(neighbors=grid_neighbors(len(walls), len(walls[0])))

print (finder( (0,3), (4,3)) )
