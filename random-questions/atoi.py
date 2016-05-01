#! /usr/bin/env python

import argparse

##
# Coz every self respecting software engg better know how to do this one.
# Also, know don't ever write this in a real production environment.
##

def atoi(int_in_str):
	res = 0
	zero = ord("0")
	int_in_str_len = len(int_in_str)
	# can also use a reversed string.
	for idx, c in enumerate(int_in_str):
		# since this is python int -> long will be automatically handled by the
		# interpretter.
		# subtracting zero is important to remove the extra offset.
		res += pow(10, int_in_str_len - idx - 1) * (ord(c) - zero)
	print type(res), res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=str, required=True)
    args_ = parser.parse_args()
    atoi(args_.n)
