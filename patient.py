
# # Q2. Hospital Patient Management (Healthcare Domain)
# # Design a Patient class.
# # Methods to think about:
# # • admit patient (object method)
# # • discharge patient (object method)
# # • calculate bill (object method)
# # • update consultation fee (class method)

# class patient:
#     hospital_name = "City Hospital"
#     consultation_fee = 500
#     loc = "Hyderabad"

#     def __init__(self, name, age, admited_date, discharge_date,bill=0):
#         self.name = name
#         self.age = age
#         self.admited_date = admited_date
#         self.discharge_date = discharge_date
#         self.bill = bill
#     def admit_patient(self):
#         print("pateint:", self.name, "admitted on", self.admited_date)
#     def discharge_patient(self):
#         print("pateint:", self.name, "discharged on", self.discharge_date)
#     def calculate_bill(self,days):
#         self.bill = days * self.consultation_fee
#         print("Total bill for", self.name, "is", self.bill)
#     @classmethod
#     def update_consultation_fee(cls, new_fee):
#         cls.consultation_fee = new_fee

# p1 = patient("Harshitha", 21, "2023-10-01", "2023-10-10")
# p1.admit_patient()
# p1.discharge_patient()
# p1.calculate_bill(10)
# p1.update_consultation_fee(600)
# print("Updated consultation fee:", p1.consultation_fee)
# p2 = patient("Pragna", 23, "2023-11-01", "2023-11-05")
# p2.admit_patient()
# p2.discharge_patient()
# p2.calculate_bill(5)


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
    
    def cancle_order(self):
        print(f"Order {self.order_id} cancelled by {self.cus_name}.")

    def calculate_total_price(self, item1_price, item2_price, item3_price, item4_price, item5_price):
        self.total_price = sum(self.items) + (sum(self.items) * self.tax / 100)
        print(f"Total price for order {self.order_id} is {self.total_price}")
        