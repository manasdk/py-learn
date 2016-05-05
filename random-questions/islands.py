#! /usr/bin/env python

import copy
import traceback


ISLAND_MAP_0 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


ISLAND_MAP_1 = [
    [0, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 1]
]

ISLAND_MAP_2 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0]
]

ISLAND_MAP_NONE = []

ISLAND_MAP_SOLID = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]


def _get_neighbours(island_map, x, y):
    # compute at most 8 neighbors
    return [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x+1, y), (x-1, y+1)]


def _fill_water(island_map, x, y):
    # validate bounds
    if x < 0 or x >= len(island_map) or y < 0 or y >= len(island_map[x]):
        return False
    if island_map[x][y] == 0:
        return False
    # mark as water tile to avoid recomputation
    island_map[x][y] = 0
    # maybe check for 1?
    neighbors = _get_neighbours(island_map, x, y)
    for neighbor in neighbors:
        _fill_water(island_map, neighbor[0], neighbor[1])
    return True


def find_islands(island_map):
    island_count = 0
    if len(island_map) == 0:
        raise ValueError('Empty Map.')
    for x in xrange(len(island_map)):
        for y in xrange(len(island_map[x])):
            if _fill_water(island_map, x, y):
                island_count += 1
    return island_count


if __name__ == '__main__':
    print 'ISLAND_MAP_0 :', find_islands(island_map=copy.deepcopy(ISLAND_MAP_0))
    print 'ISLAND_MAP_1 :', find_islands(island_map=copy.deepcopy(ISLAND_MAP_1))
    print 'ISLAND_MAP_2 :', find_islands(island_map=copy.deepcopy(ISLAND_MAP_2))
    try:
        print 'ISLAND_MAP_NONE : <Expect raise>'
        find_islands(island_map=copy.deepcopy(ISLAND_MAP_NONE))
    except:
        traceback.print_exc()
    print 'ISLAND_MAP_SOLID :', find_islands(island_map=copy.deepcopy(ISLAND_MAP_SOLID))
