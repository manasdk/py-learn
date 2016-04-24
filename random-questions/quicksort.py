#! /usr/bin/env python

import argparse
import time


class QuickSorter(object):

    def __init__(self, nums):
        """This will do an in-place sort and modify the original list.
        """
        self.sortee = nums

    def sort(self):
        self._divide_n_conquer(
            0,
            len(self.sortee) - 1,
            self._pick_pivot_index(0, len(self.sortee) - 1))
        return self.sortee

    def _divide_n_conquer(self, l_idx, r_idx, p_idx):

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
            self._divide_n_conquer(l_idx, left_r_idx, self._pick_pivot_index(l_idx, left_r_idx))

        right_l_idx = p_idx + 1
        if right_l_idx < r_idx:
            self._divide_n_conquer(right_l_idx, r_idx, self._pick_pivot_index(right_l_idx, r_idx))

    def _pick_pivot_index(self, l_idx, r_idx):
        # use r_idx as the pivot index. Its just a working choice for now.
        return r_idx


def main(args_):
    print args_.nums
    start  = time.time()
    quicksorter = QuickSorter(args_.nums)
    end  = time.time()
    print quicksorter.sort()
    print 'Sorted in %ds' % (end - start)


#
# Run with ./quicksort.py -n 9 7 5 11 12 2 14 3 10 6
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--nums', nargs='+', type=int, required=True)
    args_ = parser.parse_args()
    main(args_)
