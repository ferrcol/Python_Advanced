class Monitor:
    count_monitors = 0

    def __init__(self, brand, size):
        Monitor.count_monitors += 1
        self.id_monitor = Monitor.count_monitors
        self.brand = brand
        self.size = size

    def __str__(self):
        return (f"ID: {self.id_monitor}, Brand: {self.brand}, Size: {self.size}")
    

if __name__ == "__main__":
    monitor1 = Monitor("Dell", 24)
    monitor2 = Monitor("LG", 15)
    print(monitor1)
    print(monitor2)