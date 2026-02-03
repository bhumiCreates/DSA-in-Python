arr = list(map(int, input("Enter array elements: ").split()))  #input array elements

def reverse_array(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + reverse_array(arr[:-1])

print(reverse_array(arr))
