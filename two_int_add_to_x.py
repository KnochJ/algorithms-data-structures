def sumOfTwoElements(A,x):
    n=len(A)
    lo = 0
    hi = n-1
    while(lo<hi):
        if(A[lo] + A[hi] == x):
            return True
        elif(A[lo] + A[hi] > x):
            hi = hi-1
        else:
            lo=lo+1
    return False


A = [1, 4 ,5 , 6, 9]
x = 7

print("the result is: ")
if(sumOfTwoElements(A,x) == True):
    print("True!")
else:
    print("PATHETIC!")
            
