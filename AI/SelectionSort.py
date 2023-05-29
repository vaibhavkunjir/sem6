def SelectionSort(arr):
    for i in range(len(arr)):
        min=float('-inf')
        for j in range (i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr


print(SelectionSort([43,54,12,32,21]))