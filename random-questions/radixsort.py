#! /usr/bin/env python

import argparse
import os.path


class RadixSorter(object):

    def __init__(self, nums, radix=10):
        """This will do an in-place sort and modify the original list.
        """
        self.sortee = nums
        self.radix = radix

    def sort(self):
    	radix = self.radix
    	done = False
    	while not done:
    		buckets = [list() for i in xrange(self.radix)]
    		for x in self.sortee:
    			buckets[(x % radix) / (radix / self.radix)].append(x)
    		self.sortee = []
    		for b in buckets:
    			self.sortee.extend(b)
    		if len(buckets[0]) == len(self.sortee):
    			done = True
    		else:
    			radix *= self.radix
        return self.sortee


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
    radixsorter = RadixSorter(nums)
    nums = radixsorter.sort()
    print '[End] sorting'
    if len(nums) <= 20:
        print nums
    else:
        validate_sort(nums)


#
# Run with 
# ./radixsort.py -n 9 7 5 11 12 2 14 3 10 6
#            OR
# ./radixsort.py --numfile ~/tmp/100000.txt
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument('-n','--nums', nargs='+', type=int)
    g.add_argument('-f','--numfile', type=str)
    args_ = parser.parse_args()
    main(args_)
