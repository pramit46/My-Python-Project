def partition(low, high, arr):
    PPivot=arr[high]
    i=low-1
    
    for j in range(low,high):
        if(arr[j]<=PPivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
    
def quicksort(low,high, arr):
    if(low<high):
        QPivot=partition(low,high,arr)
        quicksort(low,QPivot-1, arr)
        quicksort(QPivot,high, arr)    
    return arr
    
    
arr=[10, 40, 30, 50, 80, 40, 20, 70]
high=len(arr)-1
low=0
arr=quicksort(low,high,arr)
for x in range(len(arr)):
    print(arr[x])
