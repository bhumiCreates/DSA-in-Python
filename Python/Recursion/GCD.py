def gcd(a,b):
    #base case
    if b==0:
        return a
    #recursive
    return gcd(b,a%b)

print(gcd(699,70))