from backgroundsub import Backgroundsub
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'original', 'snip2_1.mp4')

backsub = Backgroundsub(BASEPATH).savebgs()
