import os
import sys
import time
sys.path.insert(0, os.getcwd())

import tasks


if __name__ == '__main__':
    for i in xrange(10):
        r = tasks.add.delay(4, 4)
        while not r.successful():
            time.sleep(0.1)
        print r.result
