#! /usr/bin/env python

import argparse
import datetime


def get_next_quarter(dt):
    dt_format = '%m-%d-%y'
    d = datetime.datetime.strptime(dt, dt_format)
    c_q = (1 + (d.month - 1) / 3)
    n_q = (c_q * 3) + 1 if c_q < 4 else 1
    n_y = d.year if n_q > 1 else d.year + 1
    print datetime.date(n_y, n_q, 1).strftime(dt_format)


def main(_args):
    get_next_quarter(_args.date)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('date')
    args = parser.parse_args()
    main(args)
