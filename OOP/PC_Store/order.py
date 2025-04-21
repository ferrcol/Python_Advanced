class Order:

    count_orders = 0

    def __init__(self, computers):
        Order.count_orders += 1
        self.id_order = Order.count_orders
        self.computers = computers

    def add_computers(self, computer):
        self.computers.append(computer)

    def __str__(self):
        computers_str = ""
        for computer in self.computers:
            computers_str += "\n" + computer.__str__()

        return f"Order {self.id_order} Computers: {computers_str}"
