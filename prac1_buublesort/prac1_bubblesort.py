def bubblesort(a):

    size=len(a)

    for i in range(0,size):
        for j in range(0,size-1-i):

            if(a[j+1]<a[j]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            
    return a

arr=[4,3,7,2,1,9]
print(bubblesort(arr))