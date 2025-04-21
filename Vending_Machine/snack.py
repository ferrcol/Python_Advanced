class Snack:
    count_snacks = 0

    def __init__(self, name="", price=0.0):
        Snack.count_snacks +=1
        self.id_snack = Snack.count_snacks
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Snack: id={self.id_snack}, name= {self.name}, price= {self.price}"
    
    def write_snack(self):
        return f"{self.id_snack},{self.name},{self.price}"