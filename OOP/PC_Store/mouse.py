from input_device import InputDevice

class Mouse(InputDevice):
    count_mice = 0

    def __init__(self, brand, input_type):
        Mouse.count_mice += 1
        self.id_mouse = Mouse.count_mice
        self.brand = brand
        self.input_type = input_type

    def __str__(self):
        return (f"ID: {self.id_mouse}, Brand: {self.brand}, Input type: {self.input_type}")
    

if __name__ == "__main__":
    mouse1 = Mouse("Corsair", "Bluetooth")
    mouse2 = Mouse("LogiTech", "USB")
    print(mouse1)
    print(mouse2)