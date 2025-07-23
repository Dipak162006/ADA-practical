def bubblesort(a):

    size=len(a)

    for i in range(0,size):
        for j in range(0,size-1-i):

            if(a[j+1]<a[j]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            
    return a

arr=[]
size=int(input("enter size of array:-"))
for i in range(size):
    arr.append(int(input("enter number :-")))
print(bubblesort(arr))