import cv2 as cv
import numpy as np

class DataHandler:
    def writetocsv(self, trajectory):
        f = open("data.csv", "w")
        f.write("")
        f = open("data.csv", "a")
        counter = 0
        for x in trajectory[0]:
            counter += 1
            if x[1] == counter:
                f.write(str(int(x[0].pt[0])) + " ; " + str(-int(x[0].pt[1])))
                f.write("\n")
            else:
                while counter < x[1]:
                    f.write("\n")
                    counter += 1

    def adddimension(self, trajectory):
        file = open('data.csv')
        exi = file.readlines()
        f = open("data2.csv", "w")
        f.write("")
        f = open("data2.csv", "a")
        counter = 0
        for x in trajectory[0]:
            counter += 1
            if x[1] == counter:
                if exi[counter-1] == '\n':
                    f.write(" ; " + " ; " + str(-int(x[0].pt[0])))
                    f.write("\n")
                else:
                    strip = exi[counter-1].strip("\n")
                    f.write(strip + " ; " + str(-int(x[0].pt[0])))
                    f.write("\n")
            else:
                while counter < x[1]:
                    print(x[1])
                    print(len(exi))
                    print(counter-1)
                    print(exi[counter-1])
                    f.write(exi[counter-1])
                    counter += 1