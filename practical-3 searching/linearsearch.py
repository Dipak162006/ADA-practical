def linearsearch(arr,key):
    n=len(arr)

    for i in range(0,n):

        if (arr[i] == key):
          
            return i
    
    return -1

arr=[4,7,3,2,8,6]
key=6
position=linearsearch(arr,key)

if (position == -1):
    print("key not found.")
else:
    print(f"key is founded at position {position}.")