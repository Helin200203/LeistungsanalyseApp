# my_classes.py

from datetime import datetime
import json
import requests

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def put(self):
        url = f"http://127.0.0.1:5000/person/{self.first_name}"
        data = {
            "name": self.first_name,
         }
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)
        print(response.text)


class Subject(Person):
    def __init__(self, first_name, last_name, birthdate, study_area, sex, email):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.study_area = study_area
        self._birthdate = birthdate
        self.email = email

    def update_email(self):
        url = "http://127.0.0.1:5000/person/"
        data = {
            "name": self.first_name,
            "email": self.email
        }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)
        print(response.text)

    def estimate_max_hr(self):
        # Berechnung der maximalen Herzfrequenz basierend auf dem Alter
        today = datetime.now()
        age = today.year - self._birthdate.year
        return 220 - age
    
class Supervisor(Person):
    def __init__(self, first_name, last_name, Kürzel):
        super().__init__(first_name, last_name)
        self.Kürzel = Kürzel

class Experiment:
    def __init__(self,experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, filename):
        # Speichert die Attribute des Experiments als JSON-Datei
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

