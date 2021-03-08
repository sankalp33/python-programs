def binarySearch(list1,n):
      lb=0
      ub=len(list1)-1
      while(lb<=ub):
          mid=int((lb+ub)/2)
          if list1[mid]==n:
              return mid
          elif n<list1[mid]:
              ub=mid-1
          else:
              lb=mid+1
      return -1
list1=list()
choice1='y'
while choice1 is 'y':
    li=int(input('Enter items to be added in the list: '))
    list1.append(li)
    choice1=input('\n Do you want to add some more items: y/n: ')
    

print('List= ',list1)
choice='y'
while choice is 'y':
    n=int(input('Enter the element you are searching for: '))
    i=binarySearch(list1,n)
    if i==-1:
        print('Element not found ')
    else:
        print('Location of the element in the list is= ',i)
    choice=input('\n Do you want to continue: y/n: ')

