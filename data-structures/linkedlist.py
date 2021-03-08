class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def prepending(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        print('New node inserted at head position')
        self.size+=1
            
    def appending (self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
             self.tail.next=newnode
             self.tail=newnode
        print('New node inserted at tail position')
        self.size+=1

    def delhead(self):
        if self.head==None:
            print('Linkedlist is empty')
        else:
            value=self.head.data
            print("Deleted Node is",value)
            self.head=self.head.next
            self.size-=1
    def deltail(self):
         if self.head==None:
            print('Linkedlist is empty')
         else:
            try:
                curr=self.head
                while curr.next!=None:
                    prev=curr
                    curr=curr.next
                value=curr.data
                prev.next=None
                print("Deleted ",value)
                self.tail=prev
                self.size-=1
            except:
                print('Linkedlist is empty')
    def search(self):
        a=int(input("enter a no to search"))
        ptr=self.head
        while ptr!=None:
                if(ptr.data==a):
                    print("data found")
                    break
                else:
                    d=0
                ptr=ptr.next
        if(d==0):
            print("element not found")
        
    def display(self):
        ptr=self.head
        while ptr!=None:
            print(ptr.data)
            ptr=ptr.next

    def length(self):
        print("Length is",self.size)
x=Linkedlist()
print("0.length\n1.Prepend\n2.Append\n3.Del From Head\n4.Del From Tail\n5.Display\n6.Search")
c=int(input("Enter Your choice:"))
while(c<7):
    if c==0:
        x.length()
    if c==1:
        value=int(input("Enter Value to be inserted:"))
        x.prepending(value)
    if c==2:
        value=int(input("Enter Value to be inserted:"))
        x.appending(value)
    if c==3:
        x.delhead()
    if c==4:
        x.deltail()
    if c==5:
        x.display()
    if c==6:
        x.search()
    c=int(input("Enter Your choice:"))
