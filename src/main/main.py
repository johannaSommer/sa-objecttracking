from backgroundsub import Backgroundsub
from frameex import Frameex
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'snip2_1.mp4')

backsub = Backgroundsub(BASEPATH).savebgs()
Frameex(backsub).extract(30)
