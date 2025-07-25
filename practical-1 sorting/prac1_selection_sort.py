def selection(a):
    size=len(a)

    for i in range(0,size):

        min=i
        j=i+1

        for j in range(i+1,size):
            
            if(a[j]<a[min]):
                min=j
        
        temp=a[i]
        a[i]=a[min]
        a[min]=temp

    return a

arr=[7,4,6,2,9]
print(selection(arr)) 