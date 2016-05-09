#! /usr/bin/env python

###
# To run : ./bomberman.py
###

import operator
import sys


W = '\033[93mW\033[0m'  # wall
E = '\033[91mE\033[0m'  # enemy
O = '0'
X = '\033[92mX\033[0m'


GAME_MAP_1 = [
    [O, O, O, O, O],
    [O, E, O, O, O],
    [O, O, O, W, E],
    [O, O, O, O, O],
    [O, O, E, O, O]
]

GAME_MAP_2 = [
    [O, O, O, O, O],
    [O, O, E, O, O],
    [O, O, O, W, O],
    [O, O, O, O, E],
    [O, O, E, O, O]
]


def _update_damamge_for_key(damages, key):
    if key in damages:
            damages[key] = damages[key] + 1
    else:
        damages[key] = 1


def _update_damages(game_map, damages, enemy_r, enemy_c):
    # left
    for l_c in reversed(xrange(enemy_c)):
        if game_map[enemy_r][l_c] == W:
            break
        _update_damamge_for_key(damages, '%d:%d' % (enemy_r, l_c))
    # right
    for l_c in xrange(enemy_c + 1, len(game_map[enemy_r])):
        if game_map[enemy_r][l_c] == W:
            break
        _update_damamge_for_key(damages, '%d:%d' % (enemy_r, l_c))
    # up
    for u_r in reversed(xrange(enemy_r)):
        if game_map[u_r][enemy_c] == W:
            break
        _update_damamge_for_key(damages, '%d:%d' % (u_r, enemy_c))
    # down
    for d_r in xrange(enemy_r + 1, len(game_map)):
        if game_map[d_r][enemy_c] == W:
            break
        _update_damamge_for_key(damages, '%d:%d' % (d_r, enemy_c))


def bomber(game_map):
    damages = {}
    for r in xrange(len(game_map)):
        for c in xrange(len(game_map[r])):
            if game_map[r][c] == E:
                _update_damages(game_map, damages, r, c)
    return max(damages.iteritems(), key=operator.itemgetter(1))


def _print_map(game_map, result):
    """ Pretty print the map.
    """
    answer = [int(x) for x in result[0].split(':')]
    game_map[answer[0]][answer[1]] = X
    for r in xrange(len(game_map)):
        for c in xrange(len(game_map[r])):
            sys.stdout.write(game_map[r][c] + ' ')
        sys.stdout.write('\n')


if __name__ == '__main__':
    result = bomber(GAME_MAP_1)
    print '\nPlace bomb at %s to get %d' % (result[0], result[1])
    _print_map(GAME_MAP_1, result)

    result = bomber(GAME_MAP_2)
    print '\nPlace bomb at %s to get %d' % (result[0], result[1])
    _print_map(GAME_MAP_2, result)
