'''
-- --------------------------------------------------------
-- #@name Norman Brumm
-- #@date 3 April 2018
-- #@assign Problem Set 4
-- ----------------------------------------
Created on Mar 15, 2018
@author: Norman Brumm
'''

def main():
    from sys import argv
    arrayLines = []
    nameOfInputFile = argv[1]
    nameOfOutputFile = argv[2]
    with open(nameOfInputFile + '.txt', 'r') as flie:
        n = 0
        for line in flie:
            if(n==0):
                n = int(line)
                y = 0
            else:
                if(y>=n):
                    break
                i=0
                num = ''
                arrayTempLines = []
                while True:
                    if(i>=len(line)):
                        num = num.rstrip()
                        arrayTempLines.append(int(num))
                        num =''
                        break
                    if(line[i]==' '):
                        arrayTempLines.append(int(num))
                        num =''
                        i+=1
                    else:
                        num += line[i]
                        i+=1
                arrayLines.append(arrayTempLines)
                y+=1
                
    intNextToBeChecked = 1
    
    while(True):
        if(intNextToBeChecked>=n-1):
            break
        intNextToBeChecked+=1
        insertionSort(arrayLines, intNextToBeChecked)
        
    
        
    findMaxValue(arrayLines, nameOfOutputFile)

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
        
class numberStorage():
    def __init__(self):
        self.maxValue = 0
        self.storageArray = []
        self.tempStorage = []
    
    def __add__(self, ArrayA):
        self.tempStorage.append(ArrayA)
        
    def __doneAdding__(self):
        if(not self.tempStorage):
            return
        
        i = 0
        for x in range(0, len(self.tempStorage)):
            i += self.tempStorage[x][3]
            
        if(i>self.maxValue):
            self.storageArray = []
            self.storageArray.append(self.tempStorage)
            self.tempStorage = []
            self.maxValue = i
            return
        
        if(i<self.maxValue):
            self.tempStorage = []
            return
        
        self.storageArray.append(self.tempStorage)
        self.tempStorage = []
        
    def __lenOfMainArray__(self):
        return len(self.storageArray)
    
    def __getItem__(self, i):
        return self.storageArray[i]
    


def findMaxValue(arrayLines, nameOfOutputFile):
    normansCheatyClass = numberStorage()
    
    normansMess(arrayLines, normansCheatyClass)
    
    if(normansCheatyClass.__lenOfMainArray__()>0):
        array2 = normansCheatyClass.__getItem__(0)
        maxValueFound = 0
        for x in range(0, len(array2)):
            maxValueFound += array2[x][3]
        fileOut = printOut(nameOfOutputFile)
        fileOut.__addLine__(maxValueFound)    
        for x in range(0, normansCheatyClass.__lenOfMainArray__()):
            tArray = normansCheatyClass.__getItem__(x)
            for j in range(0, len(tArray)):
                tempString = str(tArray[j][0]) + " "
                fileOut.__addChars__(tempString)
            fileOut.__newLine__()

    return
    
def nextNonConflict(arrayLines, i):
    for x in range(i,len(arrayLines)):
        if(arrayLines[x][1]>=arrayLines[i][2]):
            return x
    return -1

def insertionSort(ArrayA, intNextToBeChecked):
    intB = intNextToBeChecked-1
    intC = intNextToBeChecked       
    while(True):
        if(ArrayA[intC][2]<ArrayA[intB][2]):
            placeholderValueA = ArrayA[intB]
            ArrayA[intB] = ArrayA[intC]
            ArrayA[intC] = placeholderValueA
            if(intB>0):
                intB-=1
                intC-=1
            else:
                break
        else:
            break


def normansMess(arrayLines, normansClass):
    listLists = []
    for x in range(0, len(arrayLines)):
        listLists.append(messOfMesses(arrayLines, x, str(x)))
    
    listLists2 = []   
        
    for x in range(0, len(listLists)):
        listLists2.append(listTangle(listLists[x]))
    
    printNormansMess(listLists2, 0, normansClass)
     
     
def printNormansMess(listList, location, normansClass):
    if(type(listList) is not int):
        for x in range(0, len(listList)):
            printNormansMess(listList[x], location + 1, normansClass)
            if(type(listList[x]) is list):
                if(type(listList[x][0]) is int):
                    normansClass.__add__(listList[x])
        if(location < 3):
            normansClass.__doneAdding__()
    
    
def listTangle(arrayA):
    if(len(arrayA)<2):
        return arrayA
    arrayB = []
    for x in range(1, len(arrayA)):
        arrayB.append([arrayA[0], arrayA[x]])
    return arrayB
        
def messOfMesses(arrayLines, x, location):
    arrayA = []
    arrayA.append(arrayLines[x])
    i = nextNonConflict(arrayLines, x)
    if(i==-1):
        return arrayA
    for z in range(i, len(arrayLines)):
        if(arrayLines[x][2]<=arrayLines[z][1]):
            arrayA.append(messOfMesses(arrayLines, z, location+str(z)))    
    return arrayA


if __name__ == '__main__':
    main()