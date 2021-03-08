alist=()
def partition(arr,low,high):
    i = ( low-1 )         
    pivot = arr[high]     
    for j in range(low,high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
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
            quickSort(alist,0,len(alist1)-1)
    elif(d==5):
              n=0
    else:
          print("invalid choice")  
