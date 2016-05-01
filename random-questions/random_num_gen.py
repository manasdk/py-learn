#! /usr/bin/env python

import argparse
import random
import os.path


def main(args_):
	file_path = os.path.join(os.path.expanduser(args_.p), '%s.txt' % args_.n)
	max_int_32_bit = pow(2, 32)	
	with open(file_path, 'w') as f:
		for i in xrange(1, args_.n):
			f.write(str(random.randint(0, max_int_32_bit)))
			f.write('\n')
	print 'Saved %d numbers in %s.' % (args_.n, file_path)


# To generate 1M numbers
# ./random_num_gen.py -n 1000000 -p "~/tmp/"
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', type=int, required=True)
	parser.add_argument('-p', type=str, required=True)
	args_ = parser.parse_args()
	main(args_)