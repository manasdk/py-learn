#! /usr/bin/env python

import argparse


class QueenPlacer(object):
	"""
	Solves for all possible solutions for the given board size and as many
	queens.
	e.g.
	8 queens - 92 solutions
	4 queens - 2 solutions
	"""

	def __init__(self, board_size):
		self.board_size = board_size
		self.queen_locations = [None for _ in xrange(self.board_size)]
		self.solution_count = 0

	def place_queens(self):
		idx = 0
		self._do_place_queen(idx)
		if self.solution_count == 0:
			print 'No solution'

	def _do_place_queen(self, idx):
		if idx >= self.board_size:
			self.solution_count += 1
			self._print_solution()
			return True
		for i in xrange(self.board_size):
			if self._is_safe(idx, i):
				self.queen_locations[idx] = (idx, i)
				self._do_place_queen(idx + 1)
			self.queen_locations[idx] = None
		return False

	def _is_safe(self, x, y):
		test_loc = '%d:%d' % (x, y)
		blocked = set()
		for location in self.queen_locations:
			if location is None:
				continue
			# block row and column
			for i in xrange(self.board_size):
				blocked.add('%d:%d' % (location[0], i))
				blocked.add('%d:%d' % (i, location[1]))
			
			# block left diag
			m = 1
			c = location[1] - location[0]
			for x_ld in xrange(0, self.board_size):
				y_ld = m * x_ld + c
				if y_ld < self.board_size and y_ld > -1:
					blocked.add('%d:%d' % (x_ld, y_ld))
			
			# block right diag
			m = -1
			c = location[0] + location[1]
			for x_rd in xrange(0, self.board_size):
				y_rd = m * x_rd + c
				if y_rd < self.board_size and y_rd > -1:
					blocked.add('%d:%d' % (x_rd, y_rd))
		return test_loc not in blocked

	def _print_solution(self):
		print self.solution_count, '->', self.queen_locations


def main(args_):
	queen_placer = QueenPlacer(args_.n)
	queen_placer.place_queens()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, required=True)
    args_ = parser.parse_args()
    main(args_)
