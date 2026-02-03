# n=int(input("Enter number of times to print name: "))
# a=input("Enter your name: ")

# def printName(n):
#     if n<=0:
#         return
#     print("Name",a)
#     return printName(n-1)

# printName(n)

n=int(input("Enter a number: "))

def print_num(n):
    if n<=0:
        return
    print(n)
    return print_num(n-1)

print_num(n)