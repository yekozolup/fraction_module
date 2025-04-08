import math
# using gcd()
class Fraction:
    def __init__(self, numinator : int, denominator : int):
        """
        Description

        Args:
            numinator (int) : numinator of fraction
            denominator (int) : denominator of fraction
        Return:
            None
        """
        if denominator == 0:
            raise ZeroDivisionError("Denominator is can not be 0")
        GCD = math.gcd(numinator, denominator)
        self.numinator = numinator // GCD
        self.denominator = denominator // GCD

    def __str__(self):
        """
        Return a string values of fraction in format:
        numinator / denominator

        Return:
            str: in format numinator/denominator
        """
        return f"{self.numinator}/{self.denominator}"

    def __add__(self, other):
        """
        Using for plus two object of Fraction

        Return:
            Fraction: description
        """
        return Fraction(self.numinator*other.denominator+other.numinator*self.denominator, self.denominator*other.denominator)
    def __gt__(self, other):
        """

        :return: True if the first items is bigger than second
        """
        return (self.numinator*other.denominator) > (self.denominator*other.numinator)

if __name__ == "__main__":
    f1 = Fraction(4, 8)
    f2 = Fraction(5, 6)
    print(f1 + f2)
    print(f2 > f1)