def binarysearch(arr,low,high,key):
  
     while(low<=high):
        mid=(low+high)//2
        
        if(arr[mid]==key):
           return mid
        elif(key<arr[mid]):
            high=mid-1
        else:
            low=mid+1

     return -1

def recursivebisearch(arr,low,high,key):
  
     if(low<=high):
         mid=(low+high)//2
         if(arr[mid]==key):
            print(f"element found at index : {mid}.")
         elif(key<arr[mid]):
            recursivebisearch(arr,low,mid-1,key)
         else:
            recursivebisearch(arr,mid+1,high,key)
     else:
         print ("element not found.")
     

arr=[11,34,44,56,78,88,89,92,95]
key=56  
position=binarysearch(arr,0,len(arr)-1,key)
if(position==-1):
    print("element not found.")
else:
     print(f"key is founded at index :{position}.")


key=100
recursivebisearch(arr,0,len(arr)-1,key)
