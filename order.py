# Q5. E-Commerce Order System (Retail Domain)
# Design an Order class.
# Methods to think about:
# • place order (object method)
# • cancel order (object method)
# • calculate total price (object method)
# • update tax percentage (class method)

class order:
    tax = 5

    def __init__(self, order_id, cus_name, items):
        self.order_id = order_id
        self.cus_name = cus_name
        self.items = items
        self.total_price = 0

    def place_order(self):
        print(f"Order {self.order_id} placed by {self.cus_name}. Items: {self.items}")

    def cancel_order(self):
        print(f"Order {self.order_id} cancelled by {self.cus_name}.")

    def calculate_total_price(self, prices):
        self.total_price = sum(prices) + (sum(prices) * self.tax / 100)
        print(f"Total price for order {self.order_id} is {self.total_price}")
    def update_tax_percentage(cls, new_tax):
        cls.tax = new_tax
        print("Updated tax percentage to", cls.tax)


o1 = order(1, "Harshitha", ["item1", "item2", "item3"])
o1.place_order()
o1.calculate_total_price([100, 200, 300])
o1.cancel_order()
o1.update_tax_percentage(10)
o2 = order(2, "Pragna", ["item4", "item5"])
o2.place_order()
o2.calculate_total_price([400, 500])

