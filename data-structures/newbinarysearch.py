class Node:
    def __init__(self,info):

        self.info = info 
        self.left = None 
        self.right = None 
        self.level = None 

    def __str__(self):

        return str(self.info) 


class searchtree:
    def __init__(self): 

        self.root = None


    def create(self,val):  

        if self.root == None:

            self.root = Node(val)

        else:

            current = self.root

            while 1:

                     if val < current.info:

                       if current.left:
                          current = current.left
                       else:
                          current.left = Node(val)
                          break;      

                     elif val > current.info:
                     
                        if current.right:
                           current = current.right
                        else:
                           current.right = Node(val)
                           break;      

                     else:
                        break

    def inorder(self,node):
                    
               if node is not None:
                  
                  self.inorder(node.left)
                  print (node.info)
                  self.inorder(node.right)


    def preorder(self,node):
                
               if node is not None:
                  
                  print (node.info)
                  self.preorder(node.left)
                  self.preorder(node.right)


    def postorder(self,node):
                
               if node is not None:
                  
                  self.postorder(node.left)
                  self.postorder(node.right)
                  print (node.info)

                            
tree = searchtree()     
arr = [8,3,1,6,4,7,10,14,13]
for i in arr:
    tree.create(i)

print ('Inorder Traversal')
tree.inorder(tree.root) 
print ('Preorder Traversal')
tree.preorder(tree.root) 
print('Postorder Traversal')
tree.postorder(tree.root) 

