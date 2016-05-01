#! /usr/bin/env python

import argparse


def in_place_reverse(s):
	s_arr = [c for c in s]
	str_len = len(s)
	str_len_minus_1 = str_len - 1
	for i in xrange(str_len / 2):
		s_arr[i], s_arr[str_len_minus_1 - i] = s_arr[str_len_minus_1 - i], s_arr[i]
	return ''.join(s_arr)


def is_palindrome(s):
	s_arr = [c for c in s]
	str_len = len(s)
	str_len_minus_1 = str_len - 1
	for i in xrange(str_len / 2):
		# For case insensitive use
		# if s_arr[i].lower() != s_arr[str_len_minus_1 - i].lower():
		if s_arr[i] != s_arr[str_len_minus_1 - i]:
			return False
	return True


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', type=str, required=True)
	args_ = parser.parse_args()
	print in_place_reverse(args_.s)
	print is_palindrome(args_.s)
