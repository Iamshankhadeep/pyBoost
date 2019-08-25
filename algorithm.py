def linearSearch(array,val):
    for i in array:
        if(i==val):
            return True
    return False

def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def partition(arr, low, high): 
    i = (low - 1)         # index of smaller element 
    pivot = arr[high]     
  
    for j in range(low, high):
        if arr[j] <= pivot: 
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1) 
  
 
def quickSort2(arr, low, high): 
    if low < high: 
  
        pi = partition(arr, low, high) 
        quickSort2(arr, low, pi-1) 
        quickSort2(arr, pi + 1, high) 
        


def quickSort(arr):
    quickSort2(arr,0,len(arr)-1)