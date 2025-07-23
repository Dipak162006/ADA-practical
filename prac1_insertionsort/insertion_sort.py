def insertion(a):
    size=len(a)

    for i in range(0,size):
        key=a[i]
        j=i-1
        while(j>=0 and a[j]>key):

            a[j+1]=a[j]
            j-=1

        a[j+1]=key
    
    return a

arr=[4,7,2,3,1]

print(insertion(arr))

        