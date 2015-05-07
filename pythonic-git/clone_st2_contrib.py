import sys
import traceback
from gittle import Gittle, GittleAuth

repo_path = '/Users/manas/tmp/st2-contrib'
repo_url = 'git://github.com/stackstorm/st2-contrib'
key = '/Users/manas/.ssh/id_rsa'

try:
    auth = GittleAuth(pkey=key)
    repo = Gittle.clone(repo_url, repo_path, auth=auth)
except:
    ex_t, ex, tb = sys.exc_info()
    print str(ex)
    print ''.join(traceback.format_tb(tb))
