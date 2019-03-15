from backgroundsub import Backgroundsub
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'video_march', 'snips', 'snip1_3.mp4')

Backgroundsub(BASEPATH).savebgs()
