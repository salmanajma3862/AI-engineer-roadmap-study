class student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        

student1 = student("Jin", "Computer Science", 3.5, False)
student2 = student("Kelly", "Business", 3.7, True)

print(student2.is_on_probation)