# my_classes.py

from datetime import datetime
import json

class Person:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        __dict__ = {"first_name":self.first_name,"last_name": self.last_name,"sex":self.sex,"age":self.age}

    def save(self, filename):
        # Speichert die Attribute der Person als JSON-Datei
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    def estimate_max_hr(self):
        return 220 - self.age

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

