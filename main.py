import json
import my_classes as mc

# Funktion zur Abfrage von Personendaten
def ask_for_person_info(role):
    print(f"Geben Sie die Informationen für {role} ein:")
    first_name = input("Vorname: ")
    last_name = input("Nachname: ")
    sex = input("Geschlecht (male/female): ")
    age = int(input("Alter: "))
    return mc.Person(first_name, last_name, sex, age)

# Hauptfunktion
def main():
    # Experiment-Informationen
    experiment_name = input("Name des Experiments: ")
    date = input("Datum (dd.mm.yyyy): ")

    # Informationen zum Supervisor und Versuchsperson
    supervisor = ask_for_person_info("Supervisor")
    subject = ask_for_person_info("Versuchsperson")

    # Erstellen und Drucken des Experiment-Dictionary
    experiment = mc.Experiment(experiment_name, date, supervisor, subject)
    print("\nExperiment-Details:")
    print(experiment)

    # Speichern der Daten in einer JSON-Datei
    with open("experiment_details.json", "w") as outfile:
        json.dump(experiment, outfile)

if __name__ == "__main__":
    main()
