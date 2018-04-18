'''
Created on Feb 8, 2018

@author: Neain
'''
import time

def main():
    startTime = time.time()
    print(startTime) 
    timedStuff()
    finishTime = time.time() - startTime
    print(finishTime)
    
    
def timedStuff():
    arrayA = []
    nameOfFile = 'randomlyCreatedNumbers(s)'
    with open(nameOfFile + '.txt', 'r') as flie:
        for line in flie:
            arrayA.append(int(line))
            
    quickSort(arrayA, 0, len(arrayA)-1)
            
    with open('PythonSorted' + nameOfFile+ '.txt', 'w') as flie:
        for item in arrayA:
            flie.write("%s\n" % item)

def quickSort(arrayA, low, high):
    if(low<high):
        pi = partition(arrayA, low, high)
        
        quickSort(arrayA, low, pi - 1)
        quickSort(arrayA, pi+1, high)
    
    
def partition(arrayA, low, high):
    pivot = arrayA[high]
    
    i=(low-1)
    
    j = low
    while (j<=high-1):
        if(arrayA[j] <= pivot):
            i+=1
            swap(arrayA, i, j)
        j+=1
    swap(arrayA, i+1, high)
    return (i+1)


def swap(arrayA, i, j):
    freq = arrayA[i]
    arrayA[i] = arrayA[j]
    arrayA[j] = freq

if __name__ == '__main__':
    main()