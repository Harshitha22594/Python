
# Q8. Hostel Management System (Accommodation Domain)
# Design a HostelRoom class.
# Methods to think about:
# • allocate room (object method)
# • vacate room (object method)
# • calculate monthly fee (object method)
# • update room rent (class method)

import logging

logging.basicConfig(
    filename = "hostel.log",
    level=logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s')

class hostel:
    room_rent = 1800

    def __init__(self, room_number, room_type, student_name):
        self.room_number = room_number
        self.room_type = room_type
        self.student_name = student_name
        self.allocated = False
        self.monthly_charges = 0

    def allocate_room(self):
        self.allocated = True
        logging.info(f"Room {self.room_number} ({self.room_type}) allocated to {self.student_name}")

    def vacate_room(self):

        if self.allocated:
            self.allocated = False
            logging.info(f"Room {self.room_number} vacated by {self.student_name}")
        else:
            logging.warning(f"Room {self.room_number} was not allocated")

    def calculate_monthly_fee(self, num_months=1):
        self.monthly_charges = self.room_rent * num_months
        logging.info(f"Monthly fee calculated for {self.student_name}: {self.monthly_charges} for {num_months} month(s)")
        return self.monthly_charges

    @classmethod
    def update_room_rent(cls, new_rent):
        cls.room_rent = new_rent
        logging.info(f"Room rent updated to {new_rent}")

h1 = hostel(101, "Single", "Harshitha")
h1.allocate_room()
h1.calculate_monthly_fee(3)
h1.vacate_room()

h2 = hostel(102, "Double", "Pragna")
h2.allocate_room()
h2.calculate_monthly_fee(2)
hostel.update_room_rent(2000)
h3 = hostel(103, "Triple", "Uma")
h3.allocate_room()
h3.calculate_monthly_fee(1)
        