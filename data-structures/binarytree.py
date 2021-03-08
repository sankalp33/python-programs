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
        newNode=int(input("Enter element to be inserted to Right:"))
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        print("Successfully inserted to right")
        
    def insertLeft(self):
        newNode=int(input("Enter element to be inserted to left:"))
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left
        print("Successfully inserted to left")

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

    def preorder(tree):
            print(tree.rootid)
            tree.preorder(tree.getLeftChild())
            tree.preorder(tree.getRightChild())
    def postorder(tree):
        if tree != None:
            postorder(tree.getLeftChild())
            postorder(tree.getRightChild())
            print(tree.getRootVal())
    def inorder(tree):
      if tree != None:
          inorder(tree.getLeftChild())
          print(tree.getRootVal())
          inorder(tree.getRightChild())

def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())
            


# test tree

def testTree():
    printTree(myTree)

w=7
a=int(input("Enter root:"))
myTree=BinaryTree(a)
print("Now",a,"is the root")
while(w!=0):
    z=int(input("Enter your choice:\n2.insertleft\n3.insertright\n4.Print\n5.inorder\n6.Preorder\n7.Postorder"))
    if(z==2):
        myTree.insertLeft()
    elif(z==3):
        myTree.insertRight()
    elif(z==4):
        testTree()
    elif(z==5):
        myTree.inorder()
    elif(z==6):
        myTree.preorder()
    elif(z==7):
        myTree.postorder()
    else:
        print("Invalid choice")

        
