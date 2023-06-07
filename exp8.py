def search(list,n):  

    for i in range(len(list)): 

        if list[i] == n: 

            return True

    return False 

list = [1, 2, 'goeduhub', 4,'python','machine learning',6]  

n = 'python'  # to be searched

if search(list, n): 

    print("Found at index ",list.index(n)) 

else: 

    print("Not Found")