from service import Service
from snack import Snack

class SnacksMachine:
    def __init__(self):
        self.service = Service()
        self.products = []

    def snacks_machine(self):
        exit = False
        print("  Vending Machine  ")
        self.service.show_snacks()
        while not exit:
            try:
                choise = self.show_menu()
                exit = self.run_choise(choise)

            except Exception as e:
                print(f"Error: {e}")

    def show_menu(self):
        print(f'''Menu:
        1 . Buy snack
        2 . Show receipt
        3 . Add new snack
        4 . Show all snacks
        5 . Exit''')
        return int(input("Choose an option: "))

    def run_choise(self , choise):
        if choise == 1:
            self.buy_snack()
        elif choise == 2:
            self.show_receipt()
        elif choise == 3:
            self.add_snack()
        elif choise == 4:
            self.service.show_snacks()
        elif choise == 5:
            print("Exit the program")
            return True
        else:
            print(f"Invalid option: {choise}")
        return False
    
    def buy_snack(self):
        id_snack = int(input("Which snack do you want? (id) "))
        snacks = self.service.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.products.append(snack)
            print(f"Item added: {snack}")
        else:
            print(f"Item no founded: {id_snack}")

    def show_receipt(self):
        if not self.products:
            print("No items in the receipt")
            return
        total = sum(snack.price for snack in self.products)
        print("Vending Machine receipt")
        for product in self.products:
            print(f"  -  {product.name} - ${product.price:.2f}")
        print(f"  Total: {total:.2f}")

    def add_snack(self):
        name = input("Snack name: ")
        price = float(input("Snack price: "))
        new_snack = Snack(name,price)
        self.service.add_snack(new_snack)
        print("New item added.")

#main
if __name__ == "__main__":
    snaks_machine = SnacksMachine()
    snaks_machine.snacks_machine()




