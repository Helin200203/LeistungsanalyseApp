import json
from my_classes import Person, Experiment

def main():
    subject_or_supervisor = input("Sind Sie der Tester, der Patient oder handelt es sich hier um beides? (subject/supervisor/beides): ")
    if subject_or_supervisor.lower() == 'supervisor':
        print("Bitte geben Sie die Daten für die Patienten ein:")
        supervisor_first_name = input("Vorname: ")
        supervisor_last_name = input("Nachname: ")
        supervisor_sex = input("Geschlecht (male/female): ")
        supervisor_age = int(input("Alter: "))
        supervisor_max_hr_bpm = int(input("estimate_max_hr: "))
        supervisor = build_person(supervisor_first_name, supervisor_last_name, supervisor_sex, supervisor_age, supervisor_max_hr_bpm )
    elif subject_or_supervisor.lower() == 'subject':
        print("Bitte geben Sie den Namen des testers ein:")
        subject_first_name = input("Vorname: ")
        subject_last_name = input("Nachname: ")
        subject_sex = input("Geschlecht (male/female): ")
        subject_age = int(input("Alter: "))
        subject = build_person(subject_first_name, subject_last_name, subject_sex, subject_age)
    elif subject_or_supervisor.lower() == 'beides':
        print("Bitte geben sie zuerst die daten der Patienten ein und anschließend die des Testers:")
        supervisor_first_name = input("Vorname: ")
        supervisor_last_name = input("Nachname: ")
        supervisor_sex = input("Geschlecht (male/female): ")
        supervisor_age = int(input("Alter: "))
        supervisor_max_hr_bpm = input("estimate_max_hr")
        supervisor = build_person(supervisor_first_name, supervisor_last_name, supervisor_sex, supervisor_age, supervisor_max_hr_bpm )
        
        subject_first_name = input("Vorname: ")
        subject_last_name = input("Nachname: ")
        subject_sex = input("Geschlecht (male/female): ")
        subject_age = int(input("Alter: "))
        subject = build_person(subject_first_name, subject_last_name, subject_sex, subject_age)
    else:
        print("Falsche Eingabe")
        
    
    experiment_name = input("Name des Experiments: ")
    experiment_date = input("Datum des Experiments: ")
    experiment = build_experiment(experiment_name, experiment_date, supervisor, subject)

    print("Experiment-Daten:")
    print(experiment)
  
    with open("experiment.json", "w") as outfile:
        json.dump(experiment.__dict__, outfile, default=lambda o: o.__dict__, indent=4)

    print("Die Experiment-Daten wurden in 'experiment.json' gespeichert.")

if __name__ == "__main__":
    main()
