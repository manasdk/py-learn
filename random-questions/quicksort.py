#! /usr/bin/env python

import argparse
import os.path


"""
This impl is instructional. If you need something efficient then use list.sort
which is orders of magnitude faster than this impl.
"""

class QuickSorter(object):

    def __init__(self, nums):
        """This will do an in-place sort and modify the original list.
        """
        self.sortee = nums

    def sort(self):
        self._quicksort(
            0,
            len(self.sortee) - 1,
            self._pick_pivot_index(0, len(self.sortee) - 1))
        return self.sortee

    def _quicksort(self, l_idx, r_idx, p_idx):

        l = l_idx
        r = r_idx
        pivot = self.sortee[p_idx]
        while l < r:
            if self.sortee[l] > pivot:
                x = self.sortee.pop(l)
                # pivot moved 1 to the left
                p_idx -= 1
                if p_idx + 1 == len(self.sortee):
                    self.sortee.append(x)
                else:
                    # place x at the pivot idx
                    self.sortee.insert(p_idx + 1, x)
                # we can also skip the last
                r -= 1
            else:
                l += 1

        left_r_idx = p_idx - 1
        if left_r_idx > l_idx:
            self._quicksort(l_idx, left_r_idx, self._pick_pivot_index(l_idx, left_r_idx))

        right_l_idx = p_idx + 1
        if right_l_idx < r_idx:
            self._quicksort(right_l_idx, r_idx, self._pick_pivot_index(right_l_idx, r_idx))

    def _pick_pivot_index(self, l_idx, r_idx):
        # use r_idx as the pivot index. Its just a working choice for now.
        return r_idx


def read_nums(args_):
    if args_.nums:
        return args_.nums
    elif args_.numfile:
        nums = []
        with open(os.path.expanduser(args_.numfile), 'r') as f:
            for num in f:
                nums.append(int(num))
        return nums
    return []


def validate_sort(nums):
    for idx, num in enumerate(nums):
        if idx == 0:
            continue
        if nums[idx] < nums[idx-1]:
            raise ValueError('Expected ascending order.')


def main(args_):
    print '[Start] reading'
    nums = read_nums(args_)
    print '[End] reading'
    if len(nums) < 20:
        print nums
    print '[Start] sorting %d numbers' % len(nums)
    quicksorter = QuickSorter(nums)
    nums = quicksorter.sort()
    print '[End] sorting'
    if len(nums) <= 20:
        print nums
    else:
        validate_sort(nums)


#
# Run with 
# ./quicksort.py -n 9 7 5 11 12 2 14 3 10 6
#            OR
# ./quicksort.py --numfile ~/tmp/100000.txt
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument('-n','--nums', nargs='+', type=int)
    g.add_argument('-f','--numfile', type=str)
    args_ = parser.parse_args()
    main(args_)
