def leftShift(A):
    first = A[0]
    for i in range(1,len(A)):
        A[i-1] = A[i]
    A[len(A)-1] = first

def rightShift(A):
    last = A[len(A)-1]
    for i in range(0, len(A)):
        A[i] = A[i-1]
        print(i)
    print(i)
    A[0]= last


def SecondSmall(A):
    min1 = A[0]
    min2 = A[1]
    for i in range(2, len(A)):
        if min2 < min1:
            min2, min1 = min1, min2
        #if min2 is less that we need to reassign min1 and min2
        elif A[i] < min1:
            min2 = min1
            min1 = A[i]
        elif  A[i] < min2:
            min2 = A[i]
    return min2



A = [1,2,3,4]
print("The Array:")
print(A)
print(SecondSmall(A))
#leftShift(A)
#print("Shifted Array:")
#print(A)
rightShift(A)
print("Shifted Array:")
print(A)



