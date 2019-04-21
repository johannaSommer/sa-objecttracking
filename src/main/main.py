from BackgroundSubtraction import Backgroundsub
from BlobDetection import Blobdetection
from DataHandler import DataHandler
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'SYNC', 'backsub', 'sync_1_2bgs.wmv')

filelist = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex'))


#for x in filelist:
#    Blobdetection(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex', x), False).showbdimg()
#Backgroundsub(BASEPATH).savebgs()
trajectory = Blobdetection(BASEPATH, True, False).showbd()
DataHandler().writetocsv(trajectory, True)


