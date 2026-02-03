#sum of n numbers using recursion

n=int(input("Enter a number: "))

def sum_n(n):
    if n<=0:
        return 0
    return n+sum_n(n-1)

print("Sum is:",sum_n(n))

