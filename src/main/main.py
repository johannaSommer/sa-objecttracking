from backgroundsub import Backgroundsub
from blobdetection import Blobdetection
import os

BASEPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos_march', 'snips', 'framex', 'snip1_1__1552678745.92.jpg')

# backsub = Backgroundsub(BASEPATH).savebgs()
# blobdec = Blobdetection.showbd(BASEPATH)
blobdec = Blobdetection(BASEPATH, False).showbdimg()

