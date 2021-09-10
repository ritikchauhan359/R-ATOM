'''
1.We start with the first element and i=0 index and check if the element present at i+1 
is greater then we swap the elements at index i and i+1.
2.If above is not the case, then no swapping will take place.
3.Now  “ i ” gets incremented and the above 2 steps happen again until the array is exhausted.
4'We will ignore the last index as it is already sorted.
5.Now the largest element will be at the last index of the array.
6.Now we will again set i=0 and continue with the same steps that will eventually place second largest at 
second last place in the array. Now the last 2 indexes of the array are sorted.

'''
l=[]
n=int(input("Enter the size of array"))
for i in range(0,n):
    x=int(input("Enter no."))
    l.append(x)
for i in range(n-1):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print("sorted array",l)

