import copy


class Base(object):
    base_prop = {'a': 1}

    def __str__(self):
        return 'Base@%s: %s' % (id(self), self.base_prop)


class Sub(Base):
    base_prop = copy.deepcopy(Base.base_prop)
    base_prop['b'] = 2

    def __str__(self):
        return 'Sub@%s: %s' % (id(self), self.base_prop)


if __name__ == '__main__':
    print '=====Base====='
    b = Base()
    print b

    print '=====Sub====='
    s = Sub()
    print s

    print '=====Base====='
    b = Base()
    print b
