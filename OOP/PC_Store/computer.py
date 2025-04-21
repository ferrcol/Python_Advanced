from mouse import Mouse
from keyboard import Keyboard # type: ignore
from monitor import Monitor

class Computer:
    count_computers = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.count_computers += 1
        self.id_computer = Computer.count_computers
        self.name = name
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse

    def __str__(self):
        return (f"Name: {self.name}: id: {self.id_computer}, \n   Monitor: {self.monitor}, \n   Keyboard: {self.keyboard}, \n   Mouse: {self.mouse}")


if __name__ == "__main__":
    keyboard1 = Keyboard("IBM", "RUSB")
    mouse1 = Mouse("Corsair", "Bluetooth")
    monitor1 = Monitor("Dell", 24)
    computer1 = Computer("Dell", monitor1, keyboard1, mouse1)
    print(computer1)