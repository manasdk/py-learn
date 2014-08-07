#! /usr/bin/python

SHARED = 10


def _get_default_value():
    print '_get_default_value called.'
    global SHARED
    return SHARED


def func(a=_get_default_value()):
    global SHARED
    print 'a = %s & SHARED = %s' % (a, SHARED)


def main():
    print 'main called.'
    global SHARED
    func()
    SHARED += 1
    func()


if __name__ == '__main__':
    main()
