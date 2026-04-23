arr = [5,3,22,54,21,33,65,89,78,32,7,12,10]
n=len(arr)

def bubbleSort(arr,n):
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

bubbleSort(arr,n)
print(arr)
