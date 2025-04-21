from mouse import Mouse
from monitor import Monitor
from keyboard import Keyboard
from computer import Computer
from order import Order


print(" PC Store ")

# First Order
keyboard1 = Keyboard("Corsair", "USB")
mouse1 = Mouse("HP", "USB")
monitor1 = Monitor("LG",24)
computer1 = Computer("HP", monitor1, keyboard1, mouse1)

keyboard2 = Keyboard("Dell", "Bluetooth")
mouse2 = Mouse("Genius", "USB")
monitor2 = Monitor("Dell",32)
computer2 = Computer("Dell", monitor2, keyboard2, mouse2)

computers1 = [computer1, computer2]
order1 = Order(computers1)

print(order1)

