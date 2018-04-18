'''
-- --------------------------------------------------------
-- #@name Norman Brumm
-- #@date 17 April 2018
-- #@assign Problem Set 5
-- ----------------------------------------
'''
import os

class printOut():
    def __init__(self, nameOfFile):
        stringFile = nameOfFile + ".txt"
        self.file = open(stringFile, 'w')
    
    def __addLine__(self, line):
        self.file.write(str(line))
        self.file.write('\n')
        
    def __addChars__(self, charString):
        self.file.write(str(charString))
        
    def __newLine__(self):
        self.file.write('\n')
        
    def __closeFile__(self):
        self.file.close()
def wordDistance(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    arrayX = []
    arrayY = []
    for x in range(0, len(w1)+2):
        if(x>1):
            arrayX.append(w1[x-2])
        else:
            arrayX.append("")
    arrayY.append(arrayX)
    
    arrayX = []
    for x in range(0, len(w1)+2):
        if(x<1):
            arrayX.append("")
        if(x==1):
            arrayX.append(0)
        if(x>1):
            arrayX.append(int(arrayX[x-1]+1))
    arrayY.append(arrayX)
    
    for y in range(0, len(w2)):
        arrayX = []
        for x in range(0, len(w1)+2):
            if(x==0):
                arrayX.append(w2[y])
            if(x==1):
                arrayX.append(int(arrayY[y+1][x])+1)
            if(x>1):
                y1 = int(arrayY[y+1][x])
                x1 = int(arrayX[x-1])
                if(y1<x1):
                    arrayX.append(y1+1)
                else:
                    if(x1<y1):
                        arrayX.append(x1+1)
                    else:
                        if(arrayY[0][x]==arrayX[0]):
                            arrayX.append(int(arrayY[y+1][x-1]))
                        else:
                            arrayX.append(int(arrayY[y+1][x-1])+2)
        arrayY.append(arrayX)
        
            
            
    return(arrayY[len(arrayY)-1][len(w1)+1])
def readAndLoadDict(fName):
    hMap = {}
    
    with open(fName, 'r') as flie:
        for line in flie:
            line = line.rstrip().lower()
            
            hMap[line] = len(line)
    return hMap
def getWordsOfSize(tSize, dist):
    rList = []
    for key,value in mapping.items():
        if(value >= (tSize - dist) and value <= (tSize + dist)):
            rList.append(key)
            
    return rList
def findWords(word, dist):
    if(dist>13):
        return -1
    dList = getWordsOfSize(len(word), dist)
    smallest = 100
    smallestWordDist = ''
    
    for i in range(0, len(dList)):
        intj = wordDistance(word, dList[i])
        if(intj<smallest):
            smallestWordDist = dList[i]
            smallest = intj

    lOut = [word, smallestWordDist, smallest]

    if(smallest>2):
        lOut2 = findWords(word, dist+1)
        if(not lOut2 == -1):
            if(lOut[2]>lOut2[2]):
                lOut = lOut2
        
    
    return lOut
def putInRejectFile(lIn):
    fName = lIn[0]
    oWord = lIn[1]
    nWord = lIn[2]
    eDist = lIn[3]
    
    sTring = fName + "," + oWord + "," + nWord + "," + str(eDist)
    wtf.__addLine__(sTring)
def readFileAndFindWords(fName):
    with open(fName, 'r') as flie:
        for line in flie:
            print(fName)
            line = line.rstrip().lower()
            lIn = [fName]
            sTring = ''
            for x in range(0,len(line)):
                if(line[x]==" "):
                    if(not sTring in mapping):
                        lIn.extend(findWords(sTring, 1))
                        print(lIn)
                        putInRejectFile(lIn)
                    lIn = [fName]
                    sTring=''
                else:
                    sTring += line[x]
            if(not sTring in mapping):
                lIn.extend(findWords(sTring, 1))
                putInRejectFile(lIn)
def getDirectory():
    return(os.listdir())

if __name__ == '__main__':
    tFile = getDirectory()
    global mapping
    global wtf
    wtf = printOut("results")
    mapping = readAndLoadDict("vocabulary.txt")
    
    for i in range(0, len(tFile)):
        if(tFile[i].endswith(".txt")):
            readFileAndFindWords(tFile[i])
    
        
    wtf.__closeFile__()