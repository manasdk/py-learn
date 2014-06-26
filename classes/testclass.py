class X(object):

    def do_something(self):
        self.do_something_class()
        print 'Instance did something.'

    @classmethod
    def do_something_class(cls):
        print 'Class did something.'

