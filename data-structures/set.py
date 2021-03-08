set1=[]
def append():
    a=0
    while(a!=1):
        n=int(input("Enter number to append:"))
        for i in range(len(set1)):
            if(set1[i]==n):
                print("This number already exists")
            else:
                set1.append(n)
        j=input("Do you want to continue y/n")
        if j=='n':
            a=1
    print(set1)
append()
