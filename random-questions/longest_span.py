#! /usr/bin/env python

import argparse

# Longest span of same sum between 2 arrays

def sub_sum(arr, idx_l, idx_r):
    s = sum(arr[idx_l:idx_r + 1])
    return s


def switch_polarities(idx_l_inc, idx_r_dec):
    if idx_l_inc == 1:
        return 0, -1
    return 1, 0


def main(args_):

    if len(args_.b1) != len(args_.b2):
        raise ValueError('b1 and b2 have different lengths.')

    n = len(args_.b1)

    span_idx_l = 0
    span_idx_r = n - 1

    b1_sum = sub_sum(args_.b1, span_idx_l, span_idx_r) # n
    b2_sum = sub_sum(args_.b2, span_idx_l, span_idx_r) # n
    idx_l_inc = 1
    idx_r_dec = 0

    while b1_sum != b2_sum and span_idx_l < span_idx_r:
        lower_sum = b1_sum if b1_sum < b2_sum else b2_sum
        b1_sum = sub_sum(args_.b1, span_idx_l + idx_l_inc, span_idx_r + idx_r_dec)
        b2_sum = sub_sum(args_.b2, span_idx_l + idx_l_inc, span_idx_r + idx_r_dec)
        if b1_sum < lower_sum or b2_sum < lower_sum:
            idx_l_inc, idx_r_dec = switch_polarities(idx_l_inc, idx_r_dec)
            b1_sum = sub_sum(args_.b1, span_idx_l + idx_l_inc, span_idx_r + idx_r_dec)
            b2_sum = sub_sum(args_.b2, span_idx_l + idx_l_inc, span_idx_r + idx_r_dec)
        span_idx_l = span_idx_l + idx_l_inc
        span_idx_r = span_idx_r + idx_r_dec

    print 'span edges (%d, %d) of length %s and sum %s' % (span_idx_l, span_idx_r, abs(span_idx_r - span_idx_l + 1), b1_sum)
    print args_.b1[span_idx_l : span_idx_r + 1]
    print args_.b2[span_idx_l : span_idx_r + 1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--b1', nargs='+', type=int, required=True)
    parser.add_argument('--b2', nargs='+', type=int, required=True)
    args_ = parser.parse_args()
    main(args_)
