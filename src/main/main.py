from BackgroundSubtraction import Backgroundsub
from BlobDetection import Blobdetection
from datahandling import writetocsv
from datahandling import redim
from datahandling import datacleanse
import os

# BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sync_videos', 'snips', 'sync_2_7.mp4')
# BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),  'test.png')

filelist = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests', 'blobdec_tests_2'))

filelist.sort()
print(filelist)
for x in filelist:
    Blobdetection(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests', 'blobdec_tests_2', x), False, False).showbdimg()
#Backgroundsub(BASEPATH).savebgs()
#trajectory = Blobdetection(BASEPATH, True).showbd(False)
#writetocsv(trajectory, 'test.csv')
#trajectory2 = Blobdetection(BASEPATH2, True, False).showbd()
#DataHandler().adddimension(trajectory2)
#redim(BASEPATH)
# datacleanse(BASEPATH)
# redim(BASEPATH)

