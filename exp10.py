def selsort(n):

    for i in range(len(n)-1,0,-1):

        max=0

        for j in range(1,i+1):

            if n[j]>n[max]:

                max = j

            temp = n[i]

            n[i] = n[max]

            n[max] = temp

n = [78,25,11,29,75,69,45,67]

selsort(n)

print("Sorted array : ",n)