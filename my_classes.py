from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, sex, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self._birthdate = birthdate
        
def age(self):
        today = datetime.today()
        birthdate = datetime.strptime(self._birthdate, "%Y-%m-%d")
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def full_name(self):
        return f"{self.first_name} {self.last_name}"c

class Subject(Person):
    def __init__(self, first_name, last_name, birthdate):
        super().__init__(first_name, last_name, self, birthdate)

class Examiner(Person):
    def __init__(self, first_name, last_name, birthdate, field_of_study):
        super().__init__(first_name, last_name, birthdate)
        self.field_of_study = field_of_study
class Experiment:
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def to_dict(self):
        return {
            "name": self.experiment_name,
            "date": self.date,
            "examiner": self.examiner.__dict__,
            "subject": self.subject.__dict__
        }
