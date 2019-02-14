def gcdIter(a, b):
    
    for i in range(min(a,b),0,-1):
        if not a%i and not b%i:
            return i


print(gcdIter(12,12))

def gcdRecur(a,b):

    if b == 0:
        return a

    else:
        return gcdRecur(b, a % b)


print(gcdRecur(12,12))