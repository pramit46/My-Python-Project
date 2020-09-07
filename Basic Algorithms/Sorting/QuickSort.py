def quicksort(arr,low,high):
    if(low<high):      
        pindex=partition(arr,low,high)
        quicksort(arr,low,pindex-1)
        quicksort(arr,pindex+1,high)
              
def partition(arr,low,high):
    pivot=arr[high]
    pindex=low
    for i in range(low,high):
        if(arr[i]<=pivot):
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex=pindex+1
            
    arr[high],arr[pindex]=arr[pindex],arr[high]
    return pindex

def main():
    arr=[1,3,33,3,43,4,5,4,4,56,5,100,99]
    low=0
    high=len(arr)-1
    quicksort(arr,low,high)
    for i in range(len(arr)):
        print(arr[i])
        
if __name__ == "__main__": main()
