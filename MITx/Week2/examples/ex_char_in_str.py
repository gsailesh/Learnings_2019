def isIn(char, aStr):

    length = len(aStr)
    begin = 0; end = length

    while begin < end:
        
        if length % 2 == 0:
            mid = length // 2 - 1
        else:
            mid = length // 2

        if char == aStr[mid]:
            return True
        elif isIn(char, aStr[:mid]):
            return True
        else:
            return isIn(char, aStr[mid+1:])
    
    return False