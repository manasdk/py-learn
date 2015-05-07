from gittle import Gittle

repo_path = '/Users/manas/tmp/munim'
repo_url = 'git://github.com/manasdk/munim'

repo = Gittle.clone(repo_url, repo_path)
