from main.BlobDetection import Blobdetection
import os


def test_blobdecimgcount():
    PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testing', 'testdata', 'BlobTest.jpg')
    bd = Blobdetection(PATH, False, False)
    keypoints = bd.showbdimg()
    assert len(keypoints) == 16
