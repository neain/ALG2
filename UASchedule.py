'''
-- --------------------------------------------------------
-- #@name Norman Brumm
-- #@date 2 February 2018
-- #@assign Problem Set 1
-- ----------------------------------------

@author: Norman Brumm
'''

import os.path



class UACourse():
    def __init__(self, courseList):
        
        self.info = {courseList[0]:[courseList[1],courseList[2],courseList[3],courseList[4]]}
        
    def add(self, courseList):
        self.info[courseList[0]] = courseList[1],courseList[2],courseList[3],courseList[4]
        
    def get(self, courseNum):
        return(self.info[courseNum])
    
    def getAll(self):
        return (self.info)
    
    def update(self, courseList):
        newDic = {courseList[0]:[courseList[1],courseList[2],courseList[3],courseList[4]]}
        self.info.update(newDic)    
        
    def deleteItem(self, courseNum):
        del self.info[courseNum]
    
def ListAll():
    print()
    ColumnNames()
    diction = courses.getAll(courses)
    for x0 in diction:
        if(diction[x0]):
            print('%-15s %-19s %-23s %-13s %-11s' % (x0,diction[x0][0],diction[x0][1],diction[x0][2],diction[x0][3]))
        
def ColumnNames():
    print('Course Number   Course Name         Instructor              Building      Room Number')

    
def ReviewCourse():
    courseNum = input('Enter Course Number: ')
    arrayList = courses.get(courses, courseNum)
    print() 
    ColumnNames()
    print('%-15s %-19s %-23s %-13s %-11s' % (courseNum, arrayList[0], arrayList[1], arrayList[2], arrayList[3]))
    print()
    
def AddCourse():
    courseList = []
    courseList.append(input("Course Number: "))
    courseList.append(input("Course Name: "))
    courseList.append(input("Instructor Name: "))
    courseList.append(input("Building: "))
    courseList.append(input("Room Number: "))
    courses.add(courses, courseList)
    
def AddNewCourse():
    courseList = []
    courseList.append(input("Course Number: "))
    courseList.append(input("Course Name: "))
    courseList.append(input("Instructor Name: "))
    courseList.append(input("Building: "))
    courseList.append(input("Room Number: "))
    courses.__init__(courses, courseList)
    
def ModifyCourse():
    courseList = []
    courseList.append(input("Course Number: "))
    courseList.append(input("Course Name: "))
    courseList.append(input("Instructor Name: "))
    courseList.append(input("Building: "))
    courseList.append(input("Room Number: "))
    courses.update(courses, courseList)
        
def RemoveCourse():
    courseNum = input('Enter a Course Number to remove it: ')
    courses.deleteItem(courses, courseNum)
    
def Exit():
    flie = open('courses.txt', 'w')
    diction = courses.getAll(courses)
    for x0 in diction:
        tbr = x0+','+diction[x0][0]+','+diction[x0][1]+','+diction[x0][2]+','+diction[x0][3] + '\n'
        flie.write(tbr)

    
    flie.close()
    print('File Saved and Exiting Program')
    
    
def main():
    if(os.path.isfile('courses.txt')):
        if(not os.stat('courses.txt').st_size == 0):
            flie = open('courses.txt', 'r+')
            currentLine = flie.readline().split(",")
            courses.__init__(courses,[currentLine[0],currentLine[1],currentLine[2],currentLine[3],currentLine[4].rstrip('\n')])
            for line in flie:
                if(not line.isspace()):
                    currentLine = line.split(",")
                    courses.add(courses,[currentLine[0],currentLine[1],currentLine[2],currentLine[3],currentLine[4].rstrip('\n')])
            
            usedFile()
            flie.close()
            return
        else:
            newFile()
    else:
        newFile()
    
def usedFile():
    FileExists()
    while(True):
        option1 = int(input(""))
        if(option1==1):
            ListAll()
            FileExists()
        if(option1==2):
            ReviewCourse()
            FileExists()
        if(option1==3):
            AddCourse()
            FileExists()
        if(option1==4):
            ModifyCourse()
            FileExists()
        if(option1==5):
            RemoveCourse()
            FileExists()
        if(option1==6):
            Exit()
            break

def newFile():
    noFile()
    while(True):
        option1 = int(input(""))
        if(option1==3):
            AddNewCourse()
            usedFile()
            break
        if(option1==6):
            Exit()
            break
        else:
            NoneFound()
    
def noFile():
    print('No courses exist at this time. Please add courses before trying to do anything else')
    print('Options available are:')
    print('1. List all available Courses           :  No courses found, please enter a new course')
    print('2. Review information about a course    :  No courses found, please enter a new course')
    print('3. Add a new course')
    print('4. Modify a specific course             :  No courses found, please enter a new course')
    print('5. Remove a specific course             :  No courses found, please enter a new course')
    print('6. Exit the program')

def NoneFound():
    print('No courses found, please enter a new course')
    
def FileExists():
    print('Options available are:')
    print('1. List all available Courses')
    print('2. Review information about a course')
    print('3. Add a new course')
    print('4. Modify a specific course')
    print('5. Remove a specific course')
    print('6. Exit the program')
    
if __name__ == '__main__':  #__main__ is when this program gets run
    courses = UACourse
    main()
    
    
    
            