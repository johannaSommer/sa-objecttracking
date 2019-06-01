import time
from main.datahandling import writetocsv
import cv2 as cv


def test_writecsv():
    filename = str(time.time()) + '.csv'
    trajectory = [
        [
            [cv.KeyPoint(1, 2, 3,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1)],
            [cv.KeyPoint(3, 2, 1,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1)]
        ]
        , 11]
    writetocsv(trajectory, filename)
    file = open(filename)
    result = file.readlines()
    testfile = open('testdata/TestData.csv')
    expected = testfile.readlines()
    assert result == expected


def test_datacleanse():

    assert 0


def test_redim():
    assert 0
