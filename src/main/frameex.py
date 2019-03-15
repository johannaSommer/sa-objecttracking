import cv2 as cv

class Frameex:
    def __init__(self, fileloc):
        self.infile = fileloc[:-1]
        self.cap = cv.VideoCapture(fileloc)

    def extract(self, frameskip):
        count = 0
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            if count % frameskip == 0:
                #TODO img doesnt save yet
                cv.imwrite(self.infile + "__" + str(count) + ".bmp", frame)
