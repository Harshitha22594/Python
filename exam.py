

# Q4. Online Exam System (EdTech Domain)
# Design an Exam class.
# Methods to think about:
# • start exam (object method)
# • submit exam (object method)
# • calculate score (object method)
# • update pass marks (class method)


class exam:
    pass_mark = 50
    duration = "120 mins"
    attempted = 0 
    unattempted = 0
    total_questions = 100


    def __init__(self, student_name, correct, incorrect):
        self.student_name = student_name
        self.correct_questions = correct
        self.incorrect_questions = incorrect

    def start_exam(self):
        print(f"Exam started for {self.student_name}. Duration: {self.duration}")

    def submit_exam(self, attempted, unattempted):
        self.attempted = attempted
        self.unattempted = unattempted
        print(f"Exam submitted for {self.student_name}. Attempted: {self.attempted}, Unattempted: {self.unattempted}")

    def calculate_score(self):
        score = self.correct_questions * 1 - self.incorrect_questions * 0.25
        print(self.student_name, "score:",score)
        if score >= self.pass_mark:
            print(f"{self.student_name} has passed the exam.")
        else:
            print(f"{self.student_name} has failed the exam.")
    
    @classmethod 
    def update_pass_mark(cls, new_pass_mark):
        cls.pass_mark = new_pass_mark
        print("Updated pass mark to", cls.pass_mark)

e1 = exam("Harshitha", 80, 20)
e1.start_exam()
e1.submit_exam(90, 10)
e1.calculate_score()
e1.update_pass_mark(55)
e2 = exam("Pragna", 60, 30)
e2.start_exam()
e2.submit_exam(80, 20)
e2.calculate_score()
