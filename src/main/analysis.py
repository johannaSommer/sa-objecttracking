import math


def determine_speed(og_file, new_file):
    file = open(og_file)
    og = file.readlines()
    file = open(new_file)
    new = file.readlines()
    f = open(new_file, "w")
    f.write("")
    f = open(new_file, "a")
    k = 0
    while k < len(og):
        strip = og[k].strip("\n")
        if strip == ';;':
            og[k] = [0, 0, 0]
        else:
            strip = og[k].strip("\n")
            split = strip.split(';')
            if split[2] == '':
                og[k] = [split[0], split[1], 0]
            elif split[0] == '' and split[1] == '':
                og[k] = [0, 0, split[2]]
            else:
                og[k] = [split[0], split[1], split[2]]
        k += 1
    counter = 0
    for ind, row in enumerate(og):
        if row[1] != 0 and row[2] != 0:
            if counter > 1:
                distance = math.sqrt(abs(int(row[2]) - int(og[ind-2][2]))**2 + abs(int(row[1]) - int(og[ind-2][1]))**2)
                distance_conv = distance * 0.0067
                # returns m/s
                speed = distance_conv / 0.032
                strip = new[ind].strip('\n')
                f.write(strip + ';' + str(int(speed)))
                f.write('\n')
            else:
                counter += 1
                f.write(new[ind])
        else:
            counter = 0
            f.write(new[ind])


def categorize(fileloc):
    print('herrerehehere')
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
        if ind > 1:
            current = int(row[2]) - int(exi[ind-1][2])
            if direction != math.copysign(1, current):
                direction = math.copysign(1, current)
                counter += 1
            f.write(str(row[0]) + " ; " + str(row[1]) + " ; " + str(row[2]) + ';' + str(counter))
            f.write("\n")
    print(counter)
