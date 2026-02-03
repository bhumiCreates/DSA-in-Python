arr=list(map(int, input("Enter elements: ").split()))
n = len(arr)

for i in range(n):
    count = 0
    if arr[i] == -1:
        continue
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            count += 1
            arr[j] = -1  # mark visited

    if count > 1:
        print(f"{arr[i]} appears {count} times")

