#! /usr/bin/env python

import argparse


def main(args_):
	sums = {}
	sum_ = 0
	for idx, n in enumerate(args_.nums):
		sum_ += n
		# Assume we are looking for the sum 5.
		# Current sum_ is 12
		# Previously we have seen 7
		# Therefore the sum 5 exists in this array.
		if (sum_ - args_.sum) in sums:
			print 'found sum %d' % args_.sum, args_.nums[sums[sum_ - args_.sum] + 1:idx+1]
			return True
		elif sum_ == args_.sum:
			print 'found sum %d' % args_.sum, args_.nums[0:idx+1]
			return True
		else:
			sums[sum_] = idx
	return False

##
# ./sub_array_sum.py -s 0 -n 1 -2 3 -7 5 6
# ./sub_array_sum.py -s 15 -n 1 -2 3 7 5 6
# ./sub_array_sum.py -s -6 -n 1 -3 3 -7 -5 6
##
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nums', nargs='+', type=int, required=True)
    parser.add_argument('-s', '--sum', type=int, required=True)
    args_ = parser.parse_args()
    main(args_)
