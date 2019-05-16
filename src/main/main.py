from BackgroundSubtraction import Backgroundsub
from BlobDetection import Blobdetection
from datahandling import writetocsv
from datahandling import redim
from datahandling import datacleanse
from analysis import categorize
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sync_videos', 'data', 'sync_1.csv')
# BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),  'test.png')


#Backgroundsub(BASEPATH).savebgs()
#trajectory = Blobdetection(BASEPATH, True).showbd(False)
#writetocsv(trajectory, 'test.csv')
#trajectory2 = Blobdetection(BASEPATH2, True, False).showbd()
#DataHandler().adddimension(trajectory2)
#redim(BASEPATH)
# datacleanse(BASEPATH)
# redim(BASEPATH)
categorize(BASEPATH)


