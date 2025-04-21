from input_device import InputDevice

class Keyboard(InputDevice):
    count_keyboards = 0

    def __init__(self, brand, input_type):
        Keyboard.count_keyboards += 1
        self.id_keyboard = Keyboard.count_keyboards
        self.brand = brand
        self.input_type = input_type

    def __str__(self):
        return (f"ID: {self.id_keyboard}, Brand: {self.brand}, Input type: {self.input_type}")
    

if __name__ == "__main__":
    keyboard1 = Keyboard("IBM", "RS232")
    keyboard2 = Keyboard("HP", "USB")
    print(keyboard1)
    print(keyboard2)