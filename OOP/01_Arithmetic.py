class Arithmetic:
    def __init__(self, ope1, ope2):
        self.ope1 = ope1
        self.ope2 = ope2

    def addition(self):
        result = self.ope1 + self.ope2
        print(f"Addition result: {result}")

    def subtraction(self):
        result = self.ope1 - self.ope2
        print(f"Subtraction result: {result}")

    def multiplication(self):
        result = self.ope1 * self.ope2
        print(f"Multiplication result: {result}")

    def division(self):
        if self.ope2 == 0:
            print("Cannot divide by zero.")
        else:
            result = self.ope1 / self.ope2
            print(f"Division result: {result}")

# main
if __name__ == "__main__":
    print(" Arithmetic Class Example in Python ")
    #First object
    arithmetic1 = Arithmetic(8,3)
    arithmetic1.addition()
    arithmetic1.multiplication()

    #Second object
    arithmetic2 = Arithmetic(2,0)
    arithmetic2.division()   





