a=[]
def append():
    b=int(input("Enter an integer"))
    a.append(b)
    
def bubblesort(a):
    size=len(a)
    for i in range(size):
        for j in range(size-1-i):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    print("Sorted list is:",a)

w=7
while(w!=0):
    z=int(input("Enter your choice:\n1.append\n2.Length\n3.Print\n4.bubblesort\n5.Stop\n"))
    if(z==1):
        append()
    elif(z==2):
        print("length is:",len(a))
    elif(z==3):
        print("\nlist is:",a)
    elif(z==4):
        bubblesort(a)
    elif(z==5):
        w=0
    else:
        print("Invalid choice")    
    

    
