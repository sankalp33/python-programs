class stack:
    def __init__(self):
        self.items=[]
        self.size=0
    def push(self):
        i=int(input("Enter data to add to stack:"))
        self.items.append(i)
        self.size+=1

    def pop(self):
        if(self.size==0):
            print("Stack is empty:")
        else:
            print("The popped number from the stack is",self.items.pop())
            self.size-=1
            
    def display(self):
        if(self.size==0):
            print("Stack is empty:")
        else:
            print("Starting from the top the Stack Elements are positioned as:")
            self.i=self.size-1
            while self.i>=0:
                print(self.items[self.i])
                self.i-=1

    def peek(self):
        if(self.size==0):
            print("Stack Is Empty")
        else:
            print("The topmost element in the stack is",self.items[self.size-1])
    def length(self):
        if(self.size==0):
            print("Stack is empty:")
        else:
            print("No of data in stack are",self.size)
s1=stack()
print("Menu\n")
print("1.Push\n2.Pop\n3.Display\n4.Peek\n5.Length\n6.Exit")
choice=int(input("Enter your choice:"))
while choice<=5:
    if(choice==1):
        s1.push()
    elif(choice==2):
        s1.pop()
    elif(choice==3):
        s1.display()
    elif(choice==4):
        s1.peek()
    elif(choice==5):
        s1.length()
    else:
        print("Invalid input")
    choice=int(input("Enter your choice:"))
