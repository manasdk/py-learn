#! /usr/bin/env python

import argparse


class ChangeMaker(object):
    def __init__(self, desired_sum, coins):
        self.sum = desired_sum
        # set to make sure we don't have repeats and list to make it easy to
        # iterate in make_change.
        self.coins = list(set(coins))

    def make_change(self):
        sum_plus_1 = self.sum + 1
        # the 1D table in which we will store the repeated data
        ways = [0 for i in xrange(sum_plus_1)]

        # 1 way to make sum=0 i.e. {}
        ways[0] = 1

        for i in xrange(len(self.coins)):
            coin = self.coins[i]
            for j in xrange(coin, sum_plus_1):
                ways[j] += ways[j - coin]

        return ways[self.sum]


def main(args_):
    changemaker = ChangeMaker(args_.s, args_.coins)
    print changemaker.make_change()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=int, required=True)
    parser.add_argument('--coins', '-c', nargs='+', type=int, required=True)
    args_ = parser.parse_args()
    main(args_)
