import json
from datetime import datetime
from my_classes import Subject, Examiner, Experiment

def main():
    subject_or_supervisor = input("Sind Sie der subject, der Psupervisor oder handelt es sich hier um beides? (subject/supervisor/beides): ")
    if subject_or_supervisor.lower() == 'supervisor':
        print("Bitte geben Sie die Daten für des Supervisors ein:")
        supervisor_first_name = input("Vorname: ")
        supervisor_last_name = input("Nachname: ")
        supervisor_sex = input("Geschlecht (male/female): ")
        birthdate = input("Geburtsdatum (YYYY-MM-DD): ")
        field_of_study = input("Fachgebiet: ")
        supervisor = Examiner(first_name, last_name, sex, birthdate, field_of_study)
        
    elif subject_or_supervisor.lower() == 'subject':
        print("Bitte geben Sie den Namen des testers ein:")
        subject_first_name = input("Vorname: ")
        subject_last_name = input("Nachname: ")
        subject_sex = input("Geschlecht (male/female): ")
        birthdate = input("Geburtsdatum (YYYY-MM-DD): ")
        subject = Subject(first_name, last_name, sex, birthdate)
        
    elif subject_or_supervisor.lower() == 'beides':
        print("Bitte geben Sie zuerst die Daten des Supervisors ein:")
        supervisor_first_name = input("Vorname: ")
        supervisor_last_name = input("Nachname: ")
        supervisor_sex = input("Geschlecht (male/female): ")
        birthdate = input("Geburtsdatum (YYYY-MM-DD): ")
        field_of_study = input("Fachgebiet: ")
        supervisor = Examiner(first_name, last_name, sex, birthdate, field_of_study)

        
        print("Bitte geben Sie jetzt die Daten des Subjects ein:")
        subject_first_name = input("Vorname: ")
        subject_last_name = input("Nachname: ")
        subject_sex = input("Geschlecht (male/female): ")
        birthdate = input("Geburtsdatum (YYYY-MM-DD): ")
        subject = Subject(first_name, last_name, sex, birthdate)
    else:
        print("Falsche Eingabe")
        
    
    eexperiment_name = input("Name des Experiments: ")
    experiment_date = input("Datum des Experiments (YYYY-MM-DD): ")
    experiment_date = datetime.strptime(experiment_date, "%Y-%m-%d")
    experiment = Experiment(experiment_name, experiment_date, supervisor, subject)

    print("Experiment-Daten:")
    print(vars(experiment))
  
   with open("experiment.json", "w") as outfile:
        json.dump(vars(experiment), outfile, default=lambda o: vars(o), indent=4)

    print("Die Experiment-Daten wurden in 'experiment.json' gespeichert.")

if __name__ == "__main__":
    main()
