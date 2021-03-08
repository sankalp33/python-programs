import array
front=0
back=0

maxsize=5
circularq=array.array('i')

def lengthqueue():
    print("Length of circular queue is ",len(circularq))

def isempty():
    if (len(circularq))==0:
        print("Queue is empty")
    else:
        print("Queue is not empty")

def isfull():
    if (len(circularq)==maxsize):
        print("Queue is full")
    else:
        print("Queue is not full")

def printqueue():
    print(circularq)

def enqueue():
    if((len(circularq))<=maxsize):
        a=int(input("Enter a number"))
        circularq.append(a)
    else:
        print("queue is full")

def dequeue():
    if((len(circularq))==0):
        print("This operation cannot be performed because queue is empty")
    else:
        
        circularq.pop(front)

w=7
while(w!=0):
    z=int(input("\n1.Enqueue\n2.Dequeue\n3.Length\n4.Isempty\n5.Isfull\n6.Print\n7.Stop\nEnter number to perform operations"))
    if z==1:
        enqueue()

    elif z==2:
        dequeue()

    elif z==3:
        lengthqueue()

    elif z==4:
        isempty()

    elif z==5:
        isfull()

    elif z==6:
        printqueue()

    elif z==7:
        w=0

    else:
        print("Invalid input")
