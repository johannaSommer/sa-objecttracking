from BackgroundSubtraction import Backgroundsub
from BlobDetection import Blobdetection
from datahandling import writetocsv
from datahandling import redim
from datahandling import datacleanse
from analysis import categorize
from analysis import determine_speed
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos', 'data', 'sync_4.csv')
BASEPATH2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos', 'data', 'sync_4_og.csv')

categorize(BASEPATH)
determine_speed(BASEPATH2, BASEPATH)
