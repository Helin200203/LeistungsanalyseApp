import json
from datetime import datetime
from my_classes import Subject, Examiner, Experiment
import my_functions
def datetime_converter(o):
    if isinstance(o, datetime):
        return o.isoformat() 
    
def main():
    print("Willkommen im Experiment-Tool!")
    if input("Möchten Sie ein Experiment erstellen? (y/n): ") == "y":    
        print("Bitte geben Sie zuerst die Daten des Supervisors ein:")
        supervisor_first_name = input("Vorname: ")
        supervisor_last_name = input("Nachname: ")
        supervisor_sex = input("Geschlecht (male/female): ")
        birthdate = input("Geburtsdatum (YYYY-MM-DD): ")
        field_of_study = input("Fachgebiet: ")
        supervisor = Examiner(supervisor_first_name, supervisor_last_name, supervisor_sex, birthdate, field_of_study)

        
        print("Bitte geben Sie jetzt die Daten des Subjects ein:")
        subject_first_name = input("Vorname: ")
        subject_last_name = input("Nachname: ")
        subject_sex = input("Geschlecht (male/female): ")
        birthdate = input("Geburtsdatum (YYYY-MM-DD): ")
        subject = Subject(subject_first_name, subject_last_name, subject_sex, birthdate)
    else:
        print("Falsche Eingabe")
        
        return

    experiment_name = input("Name des Experiments: ")
    experiment_date = input("Datum des Experiments (YYYY-MM-DD): ")
    experiment = Experiment(experiment_name, experiment_date, supervisor, subject)

    with open("experiment.json", "w") as outfile:
        json.dump(experiment.to_dict(), outfile, indent=4, default=datetime_converter)

    print("Die Experiment-Daten wurden in 'experiment.json' gespeichert.")

if __name__ == "__main__":
    main()
