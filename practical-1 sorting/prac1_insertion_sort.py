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

arr=[]
size=int(input("enter sizze of array:-"))

for i in range(size):
    arr+=input("enter number :-")

print(insertion(arr))

        