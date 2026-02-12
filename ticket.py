
# Q7. Railway Ticket Booking (Transport Domain)
# Design a Ticket class.
# Methods to think about:
# • book ticket (object method)
# • cancel ticket (object method)
# • calculate fare (object method)
# • update base fare (class method)

class ticket:
    base_fare = 100

    def __init__(self, ticket_id, passenger_name, journey_distance):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.journey_distance = journey_distance
        self.total_fare = 0

    def book_ticket(self):
        print(f"Ticket {self.ticket_id} booked for {self.passenger_name}. Journey distance: {self.journey_distance} km")

    def cancel_ticket(self):
        print(f"Ticket {self.ticket_id} cancelled by {self.passenger_name}.")
    
    def calculate_fare(self):
        self.total_fare = self.base_fare + (self.journey_distance * 2)
        print(f"Total fare for ticket {self.ticket_id} is {self.total_fare}")

    @classmethod
    def update_base_fare(cls, new_base_fare):
        cls.base_fare = new_base_fare
        print("Updated base fare to", cls.base_fare)

t1 = ticket(1, "Harshitha", 500)
t1.book_ticket()
t1.calculate_fare()
t1.cancel_ticket()
t1.update_base_fare(150)
t2 = ticket(2, "Pragna", 300)
t2.book_ticket()
t2.calculate_fare()
