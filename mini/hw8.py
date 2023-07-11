def isSecondBitOn(number):
#there is written to return true of false, but in example it is 1 or 0, so i wrote second function as well.
    return (number >> 2) & 1 == 1
print(isSecondBitOn(6))  
print(isSecondBitOn(10))

#second function,which returns 1 or 0.
def isSecondBitOn(number):
    return int((number >> 2) & 1)
print(isSecondBitOn(6)) 
print(isSecondBitOn(10))  

