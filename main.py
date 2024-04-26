import json
import my_classes as mc

# Funktion zur Abfrage von Personendaten



# Hauptfunktion
def main():
    # Experiment-Informationen
    experiment_name = input("Name des Experiments: ")
    date = input("Datum (dd.mm.yyyy): ")

    print(f"Geben Sie die Informationen für Subjekt ein:")
    first_name = input("Vorname: ")
    last_name = input("Nachname: ")
    sex = input("Geschlecht (male/female): ")
    birthdate = input("Birthdate: ")
    study_area = input("study area: ")

    subject = mc.Subject(first_name, last_name, birthdate, study_area, sex)

    print(f"Geben Sie die Informationen für Supervisor ein:")
    first_name = input("Vorname: ")
    last_name = input("Nachname: ")
    Kürzel = input("Kürzel: ")

    supervisor = mc.Supervisor(first_name, last_name, Kürzel)

    # Erstellen und Drucken des Experiment-Dictionary
    experiment = mc.Experiment(experiment_name, date, supervisor.__dict__, subject.__dict__)
    print("\nExperiment-Details:")
    print(experiment)
    mc.Experiment.save(experiment, "experiment.json")

if __name__ == "__main__":
    main()