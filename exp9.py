def binarySearch(arr,beg,end,item):  

    if end >= beg:  

        mid = int((beg+end)/2)  

        if arr[mid] == item :  

            return mid+1  

        elif arr[mid] < item :   

            return binarySearch(arr,mid+1,end,item)  

        else:   

            return binarySearch(arr,beg,mid-1,item)  

    return -1  

a=input("Enter elements :")

b=a.split(",")

arr=[]

for i in b:

    arr.append(int(i))

arr.sort()

print("Sorted list:",arr)

item = int(input("Enter the item which you want to search:"))  

location = -1;   

location = binarySearch(arr,0,len(arr),item);  

if location != -1:   

    print("Item found at location: %d" %(location))  

else:   

    print("Item not found") 