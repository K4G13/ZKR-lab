#log colors
class lc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    G = '\033[92m' #Green
    Y = '\033[93m' #Yellow
    R = '\033[91m' #Red
    N = '\033[0m' #Normal
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from bbs import BBS

x = BBS()
print(x.generate())