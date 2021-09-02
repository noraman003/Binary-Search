def binary_search(arr,key):
 li=0
 ui=len(arr)-1
 while li<=ui:
     mid=(li+ui)//2
     if arr[mid]==key:
         return mid
     elif arr[mid]>key:
         ui=mid - 1
     elif arr[mid]<key:
         li=mid+1
 return 'Not Found'

array=[]
n=int(input("Enter the number of elements for list:"))

for i in range(n):
     array.append(int(input("Enter the value of array[%d](by ascending order):"%i)))
print("Your list is:",array)
key=int(input("Enter the value you want to search: "))
result=binary_search(array,key)
print("Result is :",result)
