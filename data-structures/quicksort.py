def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist=[]
def append():
    c=int(input("enter an integer"))
    alist.append(c)
n=7
while(n!=0):
    d=int(input("1.append 2.length 3. print 4.quicksort 5.stop\n"))
    if(d==1):
              append()
    elif(d==2):
              print("length is ",len(alist))
    elif(d==3):
              print("list is ",alist)
    elif(d==4):
            quickSort(alist)
    elif(d==5):
              n=0
    else:
          print("invalid choice")  
