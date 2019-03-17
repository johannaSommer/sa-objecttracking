from backgroundsub import Backgroundsub
from blobdetection import Blobdetection
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex', 'snip1_1__1552678767.17.jpg')

filelist = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex'))

#TODO UNTIL FRIDAY:

#for x in filelist:
#    Blobdetection(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex', x), False).showbdimg()

#backsub = Backgroundsub(BASEPATH).savebgs()
#blobdec = Blobdetection(BASEPATH, False).showbdimg()

