class TestStatics(object):
    static_1 = None 
    static_2 = 'ClassStatic-2'
    static_3 = 'ClassStatic-3'

    def __init__(self, v1, v2):
        self.static_1 = v1
        self.static_2 = v2

    def __str__(self):
        return 'static_1 : {}, static_2 : {}, static_3 : {}'.format(self.static_1, self.static_2, self.static_3)

    def print_class_statics(self):
        print 'static_1 : {}, static_2 : {}, static_3 : {}'.format(TestStatics.static_1, TestStatics.static_2, TestStatics.static_3)


if __name__ == '__main__':
    ts1 = TestStatics('ts1_v1','ts1_v2')
    ts2 = TestStatics('ts2_v1','ts2_v2')
    print ts1
    print ts2
    ts1.print_class_statics()
    ts2.print_class_statics() 
