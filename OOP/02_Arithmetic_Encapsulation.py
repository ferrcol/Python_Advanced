class Arithmetic:
    def __init__(self, ope1=None, ope2=None):
        self._ope1 = ope1
        self._ope2 = ope2

    def addition(self):
        result = self._ope1 + self._ope2
        print(f"Addition result: {result}")

    def subtraction(self):
        result = self._ope1 - self._ope2
        print(f"Subtraction result: {result}")

    def multiplication(self):
        result = self._ope1 * self._ope2
        print(f"Multiplication result: {result}")

    def division(self):
        if self._ope2 == 0:
            print("Cannot divide by zero.")
        else:
            result = self._ope1 / self._ope2
            print(f"Division result: {result}")

    # Get/Set methodes for each operand
    def get_ope1(self):
        return self._ope1
    
    def set_ope1(self,ope1):
        self._ope1 = ope1

    def get_ope2(self):
        return self._ope2
    
    def set_ope2(self,ope2):
        self._ope2 = ope2

# main
if __name__ == "__main__":
    print(" Arithmetic Class Example in Python ")
    #First object
    arithmetic1 = Arithmetic(8,3)
    print(f"Value of Operand1: {arithmetic1.get_ope1()}")
    print(f"Value of Operand2: {arithmetic1.get_ope2()}")
    arithmetic1.addition()
    arithmetic1.multiplication()

    print()

    #Second object
    arithmetic2 = Arithmetic(2,0)
    print(f"Value of Operand1: {arithmetic2.get_ope1()}")
    print(f"Value of Operand2: {arithmetic2.get_ope2()}")
    arithmetic2.division()   