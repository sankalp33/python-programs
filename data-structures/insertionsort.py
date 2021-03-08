a=[]
def append():
    b=int(input("Enter an integer"))
    a.append(b)
def insertionsort():
    for i in range(1,len(a)):
        j=i
        while(j>0 and a[j-1]>a[j]):
            a[j],a[j-1]=a[j-1],a[j]
            j-=1
    print("sorted list:",a)
w=7
while(w!=0):
    z=int(input("Enter your choice:\n1.append\n2.Length\n3.Print\n4.insertionsort\n5.Stop\n"))
    if(z==1):
        append()
    elif(z==2):
        print("length is:",len(a))
    elif(z==3):
        print("\nlist is:",a)
    elif(z==4):
        insertionsort()
    elif(z==5):
        w=0
    else:
        print("Invalid choice")
