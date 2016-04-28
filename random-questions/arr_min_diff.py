#! /usr/bin/env python

import argparse

# Minimum difference between 2 elements in an array.


def main(args_):
    nums = sorted(args_.nums)

    num1 = None
    num2 = None
    min_diff = None

    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i + 1])
        if min_diff is None:
            min_diff = diff
            num1 = nums[i]
            num2 = nums[i + 1]
        elif diff < min_diff:
            min_diff = diff
            num1 = nums[i]
            num2 = nums[i + 1]

    print 'Minimum difference is %d between %d and %d' % (min_diff, num1, num2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--nums', nargs='+', type=int, required=True)
    args_ = parser.parse_args()
    main(args_)
