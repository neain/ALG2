'''
-- --------------------------------------------------------
-- #@name Norman Brumm
-- #@date 13 March 2018
-- #@assign Problem Set 3
-- ----------------------------------------

@author: Norman Brumm
'''
class null():
    def __init__(self):
        self.stntName = "nill"
        self.stntID = 0
        self.color = "black"
        self.parent = self
        self.right = self
        self.left = self
        
    def nilRefix(self):
        self.parent = self
        self.right = self
        self.left = self

class UAStudent():
    def addNew(self, name, idea, nill):
        self.stntName = name
        self.stntID = idea
        self.color = "red"
        self.parent = nill
        self.right = nill
        self.left = nill

class UARedBlackTree():
    def __init__(self, nill):
        self.root = nill
        self.nill = nill
        self.size = 0
        

    def findAndSetParent(self, roots, z):
        if(z.stntID > roots.stntID):
            if(roots.right==self.nill):
                roots.right = z
                z.parent = roots
            else:
                self.findAndSetParent(roots.right, z)
                
        else:
            if(roots.left==self.nill):
                roots.left = z
                z.parent = roots
            else:
                self.findAndSetParent(roots.left, z)
            
    def rightRotate(self, rrz):
        p = rrz.parent
        l = rrz.left
        cr = rrz.left.right
        
        if(rrz==self.root):
            self.root = rrz.left
        if(not p==self.nill):
            if(rrz==p.left):
                p.left = rrz.left
            else:
                p.right = rrz.left
        l.parent = p
        
        rrz.parent = l
        l.right = rrz
        
        rrz.left = cr
        cr.parent = rrz
        
        self.nill.nilRefix()
        
    
    def leftRotate(self, lrz):
        p = lrz.parent
        r = lrz.right
        cr = lrz.right.left
        
        if(lrz==self.root):
            self.root = lrz.right
        
        if(not p==self.nill):
            if(lrz==p.left):
                p.left = lrz.right
            else:
                p.right = lrz.right
        r.parent = p
        
        lrz.parent = r
        r.left = lrz
        
        lrz.right = cr
        cr.parent = lrz
        
        self.nill.nilRefix()
            
            
    def checkRotate(self, z):
        if(z.parent.color == "black" or z.color == "black"):
            return
        else:
                    
            if(z.parent == z.parent.parent.left):
                if(z.parent.parent.right.color == "red"):
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    z.parent.parent.right.color = "black"
                    self.checkRotate(z.parent.parent)
                else: 
                    if(z == z.parent.left):
                        z.parent.color = "black"
                        z.parent.parent.color = "red"
                        self.rightRotate(z.parent.parent)
                        self.checkRotate(z.parent.parent)
                    else:
                        self.leftRotate(z.parent)
                        self.checkRotate(z)
            else:
                if(z.parent.parent.left.color == "red"):
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    z.parent.parent.left.color = "black"
                    self.checkRotate(z.parent.parent)
                else: 
                    if(z == z.parent.left):
                        self.rightRotate(z.parent)
                        self.checkRotate(z)

                    else:
                        z.parent.color = "black"
                        z.parent.parent.color = "red"
                        self.leftRotate(z.parent.parent)
                        self.checkRotate(z.parent.parent)
                    
                    
                
        
            
        
    def insert(self, z):
        self.size +=1
        if(self.root==self.nill):
            self.root = z
            z.parent = self.nill
        else:
            self.findAndSetParent(self.root, z)
            self.checkRotate(z)
            
        self.nill.nilRefix()
            
        self.root.color = "black"
        
    def countRed(self, roots):
        num = 0
        if(not (roots.left == self.nill)):
            num += self.countRed(roots.left)
        if(not (roots.right == self.nill)):
            num += self.countRed(roots.right)
        if(roots.color == "red"):
            num += 1
        return num
        
    def count_red_Nodes(self):
        return self.countRed(self.root)
    
    def getStnt(self, roots, idea):
        if(roots.stntID == idea):
            return roots
        if(roots.stntID<idea):
            if(roots.right == self.nill):
                return null
            return self.getStnt(roots.right, idea)
        else:
            if(roots.left==self.nill):
                return null
            return self.getStnt(roots.left, idea)
    
    def get(self, idea):
        return self.getStnt(self.root, idea)
        
    
    def size(self):
        return self.size
        
        


def main(fileName, tree, nill):
    tree.root = nill
    with open(fileName) as flie:
        for line in flie:
            cl = line.split(",") ##cl stands for current line
            stnt = UAStudent()
            stnt.addNew(cl[1], int(cl[0]), nill)
            tree.insert(stnt)
            
    node1 = tree.root.right.right.right.right.right
    print()
    print()
    print(node1.stntName)
    print(node1.stntID)
    print(node1.color)
    

if __name__ == '__main__':
    nill = null()
    from sys import argv

    idList = argv[1]
    tree = UARedBlackTree(nill)
    main(idList, tree, nill)
    