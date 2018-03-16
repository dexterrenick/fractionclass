#!/usr/bin/env python3
"""
Fraction class
@Dexter Renick
@Version 2018-08-02
"""

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n
"Reduction function"



class Fraction():
    """ A fraction class for basic mathematical operations
    """

    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    """Creates an object called myfraction representing the fraction
    """

    def show(self):
        print(self.num,"/",self.den)
    """The default implementation for this method is to return the instance address string
    """

    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    """To override many other methods for new Fraction class
    """

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    """Reduces fractions
    """

    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
        """
        Subtracts one fraction from the other using a similar process
        to addition.
        """

    def __mul__(self, otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __truediv__(self, otherfraction):
        newnum = self.num*otherfraction.den
        newden = self.den*otherfraction.num
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)


    """"True division" returns a full result of the division
    (as opposed to "floor division" which returns an int
    result). Use the "invert and multiply" strategy.
    """

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den





def main():
    print("Testing the Fraction class")
    tests_passed = 0

    try:
        f1 = Fraction(5,1)
        tests_passed += 1
        print("Test passed: successfully created Fraction object.")
    except:
        print("Test failed: couldn't create Fraction object.")

    try:
        if f1.getNum() == 5 and f1.getDen() == 1:
            print("Test passed: getNum() and getDen() successful")
            tests_passed +=1
        else:
            print("Test failed: getNum() and getDem() incorrectly implemented")
    except:
        print("Test failed: getNum() and getDen() not working")

    try:
        if f1.__str__() == "5/1":
            print("Test passed: string representation correct")
            tests_passed += 1
        else:
            print("Test failed: __str__ found but incorrect result.")
    except:
        print("Test failed. No string representation.")

    try:
        f2 = Fraction(-2,3)
        f3 = Fraction(1,4)
    except:
        print("Couldn't create other fractions")

    try:
        if str(f1-f2) == "17/3":
            print("Test passed: 5/1 - -2/3 = 17/3")
            tests_passed += 1
        else:
            print("Test failed: subtraction found, but incorrect result")
    except:
        print("Test failed: __sub__ method not found")

    try:
        if str(f1 * f2) == "-10/3":
            print("Test passed: 5/1 * -2/3 = -10/3")
            tests_passed += 1
        else:
            print("Test failed: multiplication found, but incorrect result")
    except:
        print("Test failed: __mul__ method not found")

    try:
        if str(f1 / f2) == "-15/2":
            print("Test passed: 5/1 / -2/3 = 15/-2")
            tests_passed += 1
        else:
            print("Test failed: division found, but incorrect result")
    except:
        print("Test failed: __truediv__ method not found")

    try:
        if Fraction(1,2) == Fraction(5,10):
            print("Test passed: 1/2 = 5/10")
            tests_passed += 1
        else:
            print("Test failed: __eq__ found, but incorrect result")
    except:
        print("Test failed: __eq__ comparison not found")

    print("Tests passed = " + str(tests_passed) + "/7")

if __name__ == "__main__":
    main()
