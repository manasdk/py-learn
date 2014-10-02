#! /usr/bin/python

import time


def _update_dict_for():
    d1 = {str(x): x for x in xrange(500000)}
    d2 = {str(x): x for x in xrange(10000, 90000)}
    for x in d2:
        if x in d1:
            d1[x] = d2[x]


def _update_dict_filter():
    d1 = {str(x): x for x in xrange(500000)}
    d2 = {str(x): x for x in xrange(10000, 90000)}
    d1.update({x: d2[x] for x in filter(lambda k: k in d1, d2)})


def main():
    start_time = time.time()
    _update_dict_for()
    print '_update_dict_for    : %s sec.' % (time.time() - start_time)
    start_time = time.time()
    _update_dict_filter()
    print '_update_dict_filter : %s sec.' % (time.time() - start_time)


if __name__ == '__main__':
    main()
