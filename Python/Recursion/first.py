# i=0
# while i<5:
#     print(i)
#     i+=1


def fun1(i):
    if i==5:
        return
    
    print(i,end=" ")
    fun1(i+1)

fun1(-8)

#Loops are more efficient to use but can't be implemented in every situation.