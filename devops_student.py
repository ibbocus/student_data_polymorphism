from student_data import Student


class Devops(Student):
    def __init__(self, first_name, last_name, stream): # This adds an attribute "stream" to the devops sub class.
        self.first_name = first_name
        self.last_name = last_name
        self.stream = stream

    def roll_call(self):
        print(f"I am a {self.stream} Student")
        # This is the same method as the parent class, however it has slightly changed functionality


# Code demo
s = Student("Ib", "Bocus")
d = Devops("Ib", "Bocus", "Devops")

s.roll_call()
d.roll_call()
