from BackgroundSubtraction import Backgroundsub
from BlobDetection import Blobdetection
from DataHandler import DataHandler
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sync_videos', 'snips', 'sync_2_6.mp4')
BASEPATH2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'SYNC', 'backsub', 'sync_2_8bgs.wmv')

# qfilelist = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex'))


#for x in filelist:
#Blobdetection(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex', x), False).showbdimg()
Backgroundsub(BASEPATH).savebgs()
#trajectory = Blobdetection(BASEPATH, True, False).showbd()
#DataHandler().writetocsv(trajectory, True)
#trajectory2 = Blobdetection(BASEPATH2, True, False).showbd()
#DataHandler().adddimension(trajectory2)


