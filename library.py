
# Q3. Library Book System (Education Domain)
# Design a LibraryBook class.
# Methods to think about:
# • issue book (object method)
# • return book (object method)
# • calculate fine (object method)
# • update fine per day (class method

class library:
    fine_per_day = 2 

    def __init__(self, title, author, issued_to=None, issue_date=None):
        self.title = title
        self.author = author
        self.issued_to = issued_to
        self.issue_date = issue_date
        

    def issue_book(self):
        print(f"Book '{self.title}' issued to {self.issued_to} on {self.issue_date}.")

    def return_book(self, days):
        print(f"Book '{self.title}' returned after {days} days.")
        

    def calculate_fine(self, days):
        if days > 30:
            fine = (days - 30) * self.fine_per_day
            print(f"Fine is {fine}")
        else:
            print("No fine, book returned on time.")
        

    @classmethod
    def update_fine_per_day(cls, new_fine):
        cls.fine_per_day = new_fine
        print("Updated fine per day to", cls.fine_per_day)
    
l1 = library("The Great Gatsby", "F. Scott Fitzgerald", "Harshitha", "2023-10-01")
l1.issue_book()
l1.return_book(35)
l1.calculate_fine(35)
l1.update_fine_per_day(2.5)
l2 = library("To Kill a Mockingbird", "Harper Lee", "Pragna", "2023-11-01")
l2.issue_book()
l2.return_book(44)
l2.calculate_fine(44)

