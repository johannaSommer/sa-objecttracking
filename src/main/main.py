from BackgroundSubtraction import Backgroundsub
from BlobDetection import Blobdetection
from datahandling import writetocsv
from datahandling import redim
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sync_videos', 'data', 'test.csv')
# BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),  'test.png')

# qfilelist = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex'))


#for x in filelist:
# Blobdetection(BASEPATH, False).showbdimg()
# Backgroundsub(BASEPATH).savebgs()
#trajectory = Blobdetection(BASEPATH, True).special()
#qwritetocsv(trajectory, False, True)
#trajectory2 = Blobdetection(BASEPATH2, True, False).showbd()
#DataHandler().adddimension(trajectory2)
redim(BASEPATH)


