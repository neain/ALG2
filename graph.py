'''
Created on Feb 12, 2018

@author: Neain
'''
from sys import argv

class UAPriorityGraph():
    def __init__(self, nme):
        self.name = nme
        self.links = []
        self.distance = 99999
        self.visited = False
        
    def addLink(self, lst):
        self.links.append(lst)


def main():
    from sys import argv

    arrayA = []
    nameOfFile = argv[1]
    with open(nameOfFile + '.txt', 'r') as flie:
        for line in flie:
            i = 0
            end = False
            if(i==0):
                nodeName = line[i]
            comma = False
            to = ''
            distance = ''
            
            while True:
                if(i>=len(line)):
                    break
                if (line[i]==','):
                    comma = True
                    i+=1
                if (line[i]=='('):
                    end = True
                    i+=1
                if (line[i]==')'):
                    end = False
                    arrayA.append((nodeName, (to, distance)))
                    to = ''
                    distance = ''
                    comma = False
                if(end):
                    if(comma):
                        distance += line[i]
                    if(not comma):
                        to += line[i]
                    
                i+=1
    djekstras(arrayA)
    
def djekstras(arrayA):
    nodeList = []
    locationInList = {}
    nodeName = arrayA[0][0]
    newNode = UAPriorityGraph(nodeName)
    newNode.addLink(arrayA[0][1])
    i = 1
    j = 0
    while(True):
        if(nodeName==arrayA[i][0]):
            newNode.addLink(arrayA[i][1])
        if(not nodeName==arrayA[i][0]):
            locationInList[nodeName] = j
            j+=1
            nodeList.append(newNode)
            nodeName = arrayA[i][0]
            newNode = UAPriorityGraph(nodeName)
            newNode.addLink(arrayA[i][1])
    
        i+=1
        if(i>=len(arrayA)):
            locationInList[nodeName] = j            
            nodeList.append(newNode)
            break
    startingTheFind(nodeList, locationInList)
    
    
def startingTheFind(nodeList, locationInList):
    
    priority = []
    nodeList[0].distance = 0
    nodeList[0].visited = True
    j = 0
    i = 0
    while True:
        if (i>=len(nodeList[j].links)):
            break
        priority.append(nodeList[j].links[i][0])
        nodeList[locationInList[nodeList[j].links[i][0]]].distance = nodeList[j].links[i][1]
        i+=1
        
    while True:
        while True:
            if(not priority):
                break

            node = priority.pop()
            node = locationInList[node]
            if(not nodeList[node].visited):
                break
        if(not priority):
            break
        nodeList[node].visited = True
        
        i = 0
        
        while True:
            if (i>=len(nodeList[node].links)):
                break
            priority.append(nodeList[node].links[i][0])
            
            distThere = int(nodeList[node].links[i][1]) + int(nodeList[node].distance)
            thereDist = int(nodeList[locationInList[nodeList[node].links[i][0]]].distance)
            
            if(thereDist > distThere):
                nodeList[locationInList[nodeList[node].links[i][0]]].distance = distThere
            i+=1
        
        
        
        
    i = 0
    nameOfFile = 'output'
    with open(nameOfFile + '.txt', 'w') as flie:
        
        while True:
            if(i>=len(nodeList)):
                break
            flie.write("%3s " % (nodeList[i].name))
            i+=1
        flie.write('\n')

        i=0
        while True:
            if(i>=len(nodeList)):
                break
            flie.write("%3s " % (nodeList[i].distance))
            i+=1
        if(len(argv)>1):
            print(nodeList[locationInList[argv[1]]])
            


if __name__ == '__main__':
    main()