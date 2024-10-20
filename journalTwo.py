import numpy as np
import sys

def main():
    flo= float(input("please enter a floating point number."))
    flo2= float(input("please enter another floating point number."))
    print("The sum of these numbers is ")
    print(flo+flo2)
    print(type(flo+flo2))
    integ1=int(input("please enter an integer"))
    integ2= int(input("please enter another integer"))
    print("The difference between these numbers is ")
    print(integ1-integ2)
    print(type(integ1-integ2))
    print("the product of the first floating point number and the first integer is")
    print(flo*integ1)
    print(type(flo*integ1))
if __name__ == "__main__":
    main()
    
