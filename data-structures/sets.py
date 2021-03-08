set1=set()
set2={8,9}
ans='yes'
while(ans=='yes'):
    p=int(input("Enter number to insert in set1:"))
    set1.add(p)
    ans=input("Do you want to continue")
print('set1= ',set1)
print('set2= ',set2)
print('\nUnion= ',set1.union(set2))
print('Intersection= ',set1 & set2)
print('Difference(set1-set2)= ',set1.difference(set2))
print('Difference(set2-set1)= ',set2.difference(set1))
print('Symmetric Difference= ',set1^set2)
print('Subset test= ',set1<=set2)
print('Superset test= ',set1>=set2)
