#Merge Sort
def mergeSort(x):
    if (len(x) < 2):
        return x
    else:
        pivot = int(len(x) / 2)
        left = mergeSort(x[:pivot])
        right = mergeSort(x[pivot:])
        return merge(left,right)


def merge(left, right):
    final = []
    while (len(left)!= 0 and len(right) != 0):
        if (left[0] < right[0]):
            final.append(left[0])
            left.remove(left[0])
        else:
            final.append(right[0])
            right.remove(right[0])

    if(len(left)==0 and len(right)>0):
        final+=right
    elif(len(right)==0 and len(left)>0):
        final+=left

    return final


x = [212, 21, 2, 2, 123, 33, 44, 545, 3, 66, 7, 75, 85, 3]
print(mergeSort(x))
