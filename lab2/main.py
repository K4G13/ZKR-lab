from bbs import BBS
import test as TEST
import sys

#log colors
class lc:
    G = '\033[92m'  #Green
    Y = '\033[93m'  #Yellow
    R = '\033[91m'  #Red
    N = '\033[0m'   #Normal

dev = False
if len(sys.argv) == 2 and sys.argv[1]=="dev": dev = True

bbs = BBS(3187,7187)
bbs.generate()

if dev:
    print(f"{lc.Y}Parameters:")
    print(f"    p = {bbs.p}")
    print(f"    q = {bbs.q}")
    print(f"    x = {bbs.x}{lc.N}")

TEST.singleBitTest(bbs.bitArray)
TEST.seriesTest(bbs.bitArray)
TEST.longSeriesTest(bbs.bitArray)
TEST.pokerTest(bbs.bitArray)
