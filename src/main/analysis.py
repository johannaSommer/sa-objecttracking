import math


def determine_speed(og_file, new_file):
    print('hello')

def categorize(fileloc):
    file = open(fileloc)
    exi = file.readlines()
    f = open(fileloc, "w")
    f.write("")
    f = open(fileloc, "a")
    k = 0
    while k < len(exi):
        exi[k] = exi[k].strip('\n')
        exi[k] = exi[k].split(';')
        k += 1
    # only z axis (exi[k][2]) relevant for movement
    counter = 1
    direction = None
    for ind, row in enumerate(exi):
        if ind == 0:
            f.write(str(row[0]) + " ; " + str(row[1]) + " ; " + str(row[2]) + ';' + str(counter))
            f.write("\n")
        if ind == 1:
            f.write(str(row[0]) + " ; " + str(row[1]) + " ; " + str(row[2]) + ';' + str(counter))
            f.write("\n")
            direction = math.copysign(1, int(row[2]) - int(exi[0][2]))
        if ind > 0:
            current = int(row[2]) - int(exi[ind-1][2])
            if direction != math.copysign(1, current):
                direction = math.copysign(1, current)
                counter += 1
            f.write(str(row[0]) + " ; " + str(row[1]) + " ; " + str(row[2]) + ';' + str(counter))
            f.write("\n")
    print(counter)