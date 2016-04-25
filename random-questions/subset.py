#! /usr/bin/env python

import argparse
import pprint


def is_subset_sum(nums, sum_):

    # Even if we are dealing with a large list this is likely a good check.
    if sum_ > sum(nums):
        return False

    # the 2D array in which info is stored.
    n_rows = len(nums)
    n_cols = sum_ + 1
    sums = [[False for _ in xrange(n_cols)] for _ in xrange(n_rows)]

    # pre-initialize column 0
    for i in xrange(n_rows):
        sums[i][0] = True

    # Now lets go fill-up the remaining matrix
    for r in xrange(n_rows):
        num = nums[r]
        for c in xrange(1, sum_ + 1):
            if num == c:
                sums[r][c] = True
            else:
                if r > 0:
                    sums[r][c] = sums[r - 1][c]
                    if c >= num:
                        sums[r][c] = sums[r][c]  or sums[r - 1][c - num]
                else:
                    sums[r][c] = False

    # for i in xrange(n_rows):
    #     print nums[i], [str(sums[i][j])[0] for j in xrange(n_cols)]

    return sums[n_rows - 1][sum_]


def main(args_):
    if is_subset_sum(args_.nums, args_.sum):
        print 'There is a subset that sums to %d' % args_.sum
    else:
        print 'Did not find subset that sum upto %d' % args_.sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nums', nargs='+', type=int, required=True)
    parser.add_argument('-s', '--sum', type=int, required=True)
    args_ = parser.parse_args()
    main(args_)