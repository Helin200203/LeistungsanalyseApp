import json
from datetime import datetime
from my_classes import Subject, Examiner, Experiment

def datetime_converter(o):
    if isinstance(o, datetime):
        return o.isoformat()  # ISO 8601 Format

def main():
    try:
        # Erstellen einer Instanz von Subject
        subject = Subject("Jane", "Smith", "female", "1995-05-05", "jane@example.com")

        # Aktualisieren der E-Mail des Subjects
        subject.update_email("jane.new@example.com")

        # Erstellen einer Instanz von Examiner
        examiner = Examiner("Dr. Alice", "Johnson", "female", "1985-08-15", "Physics")

        # Erstellen einer Instanz von Experiment
        experiment = Experiment("Experiment 1", "2022-01-01", examiner, subject)

        # Umwandeln des Experiments in ein Dictionary
        experiment_dict = experiment.to_dict()

        # Ausgabe des Experiment-Dictionarys unter Verwendung des datetime_converters
        print(json.dumps(experiment_dict, indent=4, default=datetime_converter))
    except ValueError as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()