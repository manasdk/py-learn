#!/usr/bin/env python2.7

import os
import sys

def loadmodule(module_path, module_name):
    module_dir = os.path.abspath(os.path.dirname(sys.argv[1]))
    sys.path.append(module_dir)
    m = __import__(module_name)
    ftory = getattr(m, 'get_plugin')
    plugin = ftory()
    print(plugin)    

if __name__ == '__main__':
    loadmodule(sys.argv[1], sys.argv[2])
    sys.exit(1)
