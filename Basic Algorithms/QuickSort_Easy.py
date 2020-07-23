def reverse_quicksort(x):
    #if the list has only one item then just return it 
    if len(x) < 2:
        return x
    else:
        pivot = x[len(x)-1]
        #iterate through the array and put those items in the less list which are less than the pivot value
        #in short, for i in the while list, if the value of i is less than pivot value then chose i for the list less
        less = [i for i in x[:len(x)-1] if i <= pivot]
        #iterate through the array and put those items in the greater list which are more than the pivot value
        #in short, for i in the while list, if the value of i is greater than pivot value then chose i for the list greater
        greater = [i for i in x[:len(x)-1] if i > pivot]
        
        #print for better understanding
        print("pivot: "+str(pivot)+"    less: "+str(less)+"    greater: "+str(greater))
        
        #this line sorts it front way
        #return reverse_quicksort(less) + [pivot] + reverse_quicksort(greater)
        #this line sorts it reverse way
        return reverse_quicksort(greater) + [pivot] + reverse_quicksort(less)
        
test_list = [54,26,93,17,77,31,44,55,20]
print(reverse_quicksort(test_list))
