def reversebubble(a):

    size=len(a)

    for i in range(size-1,0,-1):
        for j in range(i):
            if(a[j+1]<a[j]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            
    return a

arr=[4,7,3,8,6]
print(reversebubble(arr))