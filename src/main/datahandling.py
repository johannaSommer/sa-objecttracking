
def writetocsv(trajectory, name):
    f = open(name, "w")
    f.write("")
    f = open(name, "a")
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

def adddimension(trajectory):
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

def datacleanse():
    # TODO: to be implemented
    print('hello')

def redim(fileloc):
    file = open(fileloc)
    exi = file.readlines()
    f = open(fileloc, "w")
    f.write("")
    f = open(fileloc, "a")
    k = 0
    print(exi)
    while k < len(exi):
        if exi[k] != '\n' or exi[k] != ';;':
            strip = exi[k].strip("\n")
            split = strip.split(';')
            if split != ['', '', '']:
                if split[2] == '':
                    print(split)
                    f.write(str(int(split[0]) - 315) + " ; " + str(int(split[1]) + 915))
                    f.write("\n")
                else:
                    print(split)
                    f.write(str(int(split[0]) - 315) + " ; " + str(int(split[1]) + 915) + " ; " + str(int(split[2]) - 1920))
                    f.write("\n")
        k += 1