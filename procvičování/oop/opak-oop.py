# Objektově orientované programování
# Class

class Graduation():
    def __init__(self, date, optional_subjects):
        self.difficulty = 2
        self.dress_code = "formal"
        self.stress = True
        self.success_rate = "80%"
        self.date = date
        self.subjects = ["PRG", "MAT", "CJL", "AJ"]
        self.optional_subjects = optional_subjects
    
    def examination(self):
        print("Dobrý den, good luck")
    
    def result(self, study_level):
        if study_level > 50:
            print("Gratuluji k úspěšné maturitě")
            self.stress = False
        else:
            print("Smolík, uvidíme se v září")
            self.stress = False
            self.stress = True


my_graduation = Graduation("18.5.2026", None)
print(my_graduation.dress_code)
my_graduation.examination()
my_graduation.result(99)

class University_exam(Graduation):
    def __init__(self, date, exam_type):
        super().__init__(date, None)
        self.dress_code = "variable"
        self.difficulty = [1,2,3,4,10000]
        if exam_type not in ["oral", "writing"]:
            self.exam_type = "error, wrong exam"
        else:
            self.exam_type = exam_type
            


random_uni_exam = University_exam("10.1.2027", "writing")
random_uni_exam.examination()
