import math
def checkPowerof2_method1(val,p):
    return True if (p**math.floor(math.log(val,p)))==float(val) else False

x=int(input("Enter some value"))
p=int(input("Enter the number to check the power of: "))

print( checkPowerof2_method1(x,p))
