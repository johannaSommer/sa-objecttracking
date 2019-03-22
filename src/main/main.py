from backgroundsub import Backgroundsub
from blobdetection import Blobdetection
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'backsubbed', 'snip1_7__1552679299.96.wmv')

filelist = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex'))


#for x in filelist:
#    Blobdetection(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex', x), False).showbdimg()

#Backgroundsub(BASEPATH).applybgs()
blobdec = Blobdetection(BASEPATH, True).showbd()


