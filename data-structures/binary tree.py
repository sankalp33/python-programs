class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self):
        newNode=int(input("enter the element to insert on RIGHT"))
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self):
        newNode=int(input("enter the element to insert on left "))
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left

        def delete(self,key):
              if self.size > 1:
                 nodeToRemove = self._get(key,self.root)
                 if nodeToRemove:
                     self.remove(nodeToRemove)
                     self.size = self.size-1
                 else:
                     raise KeyError('Error, key not in tree')
              elif self.size == 1 and self.root.key == key:
                 self.root = None
                 self.size = self.size - 1
              else:
                 raise KeyError('Error, key not in tree')

        def __delitem__(self,key):
           self.delete(key)


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())
            

def testTree():
    
    printTree(myTree)       

n=7
a=int(input("enter root:"))
myTree=BinaryTree(a)
print("now",a,"is the root")
while(n!=0):
    d=int(input("1.root 2.insertleft  3. insertright 4.print 5.stop\n"))
    if(d==1):
              root()
    elif(d==2):
              myTree.insertLeft()
    elif(d==3):
             myTree.insertRight()
    elif(d==4):
            testTree()
    elif(d==5):
              n=0
    else:
          print("invalid choice")
