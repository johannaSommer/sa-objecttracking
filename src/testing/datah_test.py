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
    file = open('testdata/sync_1_norm.csv')
    testdata = file.readlines()
    correct = True
    for x in testdata:
        temp = x.split(';')
        if len(temp) != 3:
            correct = False
    assert correct


def test_redim():
    file = open('testdata/sync_1_norm.csv')
    testdata = file.readlines()
    correct = True
    for x in testdata:
        temp = x.split(';')
        if int(temp[0]) > 1920 or int(temp[0]) < 0:
            correct = False
        if int(temp[1]) > 1080 or int(temp[1]) < 0:
            correct = False
        if int(temp[2]) > 0 or int(temp[2]) < -1920:
            correct = False
    assert correct
