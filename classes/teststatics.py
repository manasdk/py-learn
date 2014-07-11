class TestStatics(object):
    static_1 = None
    static_2 = 'ClassStatic-2'
    static_3 = 'ClassStatic-3'

    def __init__(self, v1, v2):
        self.static_1 = v1
        self.static_2 = v2

    def __str__(self):
        return 'static_1 : {}, static_2 : {}, static_3 : {}'.format(self.static_1, self.static_2, self.static_3)

    @classmethod
    def update_class_statics(cls, update_value='ClassStatic-3-updated'):
        cls.static_3 = update_value

    def print_class_statics(self):
        print 'static_1 : {}, static_2 : {}, static_3 : {}'.format(TestStatics.static_1, TestStatics.static_2, TestStatics.static_3)


if __name__ == '__main__':
    print '===== ts1 ====='
    ts1 = TestStatics('ts1_v1','ts1_v2')
    print ts1
    ts1.print_class_statics()

    print '===== ts2-1 ====='
    TestStatics.update_class_statics()
    ts2 = TestStatics('ts2_v1','ts2_v2')
    print ts2
    ts2.print_class_statics()

    print '===== ts2-2 ====='
    TestStatics.update_class_statics('ClassStatic-3-updated-2')
    print ts2
    ts2.print_class_statics()
