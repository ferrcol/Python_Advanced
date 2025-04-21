import os.path
from snack import Snack

class Service:
    FILE_NAME = "Vending_Machine/snacks.txt"

    def __init__(self):
        self.snacks = []

        if os.path.isfile(self.FILE_NAME):
            self.snacks = self.get_snacks()
        else:
            self.load_initial_snacks()

    def load_initial_snacks(self):
        initial_snacks= [
            Snack("Cookies",2.5),
            Snack("Candy",1.1),
            Snack("Water",0.8)
        ]
        self.snacks.extend(initial_snacks)
        self.save_snacks(initial_snacks)
    
    def save_snacks(self, snacks):
        try:
            with open(self.FILE_NAME, "a") as file:
                for snack in snacks:
                    file.write(f"{snack.write_snack()}\n")

        except Exception as e:
            print(f"Error for save snacks in file: {e}")
        
    def get_snacks(self):
        snacks = []
        try:
            with open(self.FILE_NAME,"r") as file:
                for line in file:
                    id_snack, name, price = line.strip().split(",") # create a tuple without spaces
                    snack = Snack(name, float(price))
                    snacks.append(snack)

        except Exception as e:
            print(f"Error for read snacks in file: {e}")
        return snacks
    
    def add_snack(self, snack):
        self.snacks.append(snack)
        self.save_snacks([snack])

    def show_snacks(self):
        print(" Snacks in the system")
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks