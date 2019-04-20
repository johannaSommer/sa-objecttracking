from backgroundsub import Backgroundsub
from blobdetection import Blobdetection
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'SYNC', 'sync_2_2bgs.wmv')

filelist = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex'))


#for x in filelist:
#    Blobdetection(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex', x), False).showbdimg()
#Backgroundsub(BASEPATH).savebgs()
blobdec = Blobdetection(BASEPATH, True).showbd()


