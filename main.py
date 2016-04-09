import os
import sys

def getFiles():

        path = input("Enter closed-world-checked folder path: ")
        up_one_level = os.path.dirname(path)
        os.chdir(up_one_level)
        if not os.path.exists('closed-world-checked-out'):
            os.makedirs('closed-world-checked-out')
        for idx,filename in enumerate(os.listdir(path)):
            print("filename: " + (filename) + "\tindex: " + str(idx))
            f = open('closed-world-checked/' + filename,'r')
            if not (filename.endswith('b')):
                callAlgo(f,filename)

def callAlgo(file,fname):
    lineArray = file.readlines()
    totalSize = 0
    K = 512000
    newArray = []
    for lines in lineArray:
        time = float(lines.partition('\t')[0])
        size = int(lines.partition('\t')[2].replace('\n',''))
        if(size < 0):
            totalSize = totalSize + abs(size)
            if(totalSize >= K):
                newArray.append(str(time) + '\t' + str(totalSize * -1))
                totalSize = 0
        else:
            newArray.append(str(time) + '\t' + str(size))
    finalStr = '\n'.join(newArray)
    writeToFile(finalStr,fname)


def writeToFile(final, filename):
    toFile = open('closed-world-checked-out/' + filename, 'w+')
    toFile.write(final)

getFiles()
