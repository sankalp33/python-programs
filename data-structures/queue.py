class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        if self.length() is 0:
            print("Queue Is Empty")
        else:
            print("Queue is not Empty")

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.length() is 0:
            print("Queue is Empty")
        else:
            item=self.items.pop(0)
            print("The removed element is:",item)
    def length(self):
        return len(self.items)

    def display(self):
        if self.isEmpty():
            print("Queue Empty")
        else:
            print(self.items)

queue=Queue()
print("1.Enqueue\n2.Dequeue\n3.Length\n4.Empty Or Not\n5.Display\n6.Exit")
choice=int(input("Enter your choice:"))
while choice<6:
    if choice is 1:
        item=int(input("Enter an element to be inserted into Queue:"))
        queue.enqueue(item)
    if choice is 2:
        queue.dequeue()
    if choice is 3:
        print("Number of elements in queue are:",queue.length())
    if choice is 4:
        queue.isEmpty()
    if choice is 5:
        queue.display()
    choice=int(input("Enter your choice:"))
