# my_classes.py

from datetime import datetime
import json

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def save(self, filename):
        # Speichert die Attribute der Person als JSON-Datei
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

class Subject(Person):
    def __init__(self, first_name, last_name, birthdate, study_area, sex):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.study_area = study_area
        self._birthdate = birthdate  # Verstecktes Attribut für das Geburtsdatum

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

