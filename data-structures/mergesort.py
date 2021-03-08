def mergeSort(alist):
    if(len(alist)<1):
        print("Please enter values")
    else:
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
def append():
    b=int(input("Enter an integer"))
    alist.append(b)
alist = []
w=7
while(w!=0):
    z=int(input("Enter your choice:\n1.append\n2.Length\n3.Print\n4.mergesort\n5.Stop\n"))
    if(z==1):
        append()
    elif(z==2):
        print("length is:",len(alist))
    elif(z==3):
        print("\nlist is:",alist)
    elif(z==4):
        mergeSort(alist)
    elif(z==5):
        w=0
    else:
        print("Invalid choice")
