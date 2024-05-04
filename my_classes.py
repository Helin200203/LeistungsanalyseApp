from datetime import datetime
import requests 
import json


class Person:
    def __init__(self, first_name, last_name, sex, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        
    def calculate_age(self):
        today = datetime.now()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

    @property
    def age(self):
        return self.calculate_age()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Geschlecht: {self.sex}, Alter: {self.age} Jahre"

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "birthdate": self.birthdate,
            "age": self.age
        }
    
    def put(self):
        url = "http://127.0.0.1:5000/"

    # Define the data you want to send
        data = {
            "name": "TestName"
        }

        # Convert the data to JSON format
        data_json = json.dumps(data)

        # Send a POST request to the API
        response = requests.put(url, data=data_json)

        # Print the response from the server
        print(response.text)  

class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate, email=""):
        super().__init__(first_name, last_name, sex, birthdate)
        self.email = email
        
    def update_email(self, email):
        self.email = email
        url = "http://127.0.0.1:5000/"
        data = {
            "name": "TestName",
            "email": "TestName@mail.at"
        }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)
        print(response.text)
        
    def to_dict(self):
        data = super().to_dict()
        data["email"] = self.email
        return data   
        
class Examiner(Person):
    def __init__(self, first_name, last_name, sex, birthdate, field_of_study):
        super().__init__(first_name, last_name, sex, birthdate)
        self.field_of_study = field_of_study
        
    def to_dict(self):
        data = super().to_dict()
        data["field_of_study"] = self.field_of_study
        return data   
    
class Experiment:
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.supervisor = supervisor
        self.subject = subject


    def to_dict(self):
        return {
            "name": self.experiment_name,
            "date": self.date.strftime("%Y-%m-%d"),
            "supervisor": self.supervisor.to_dict(),
            "subject": self.subject.to_dict()
        }
