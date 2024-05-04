# test.py

from datetime import date
from my_classes import Subject, Person  # Daten der my_classes.py importieren

def main():
    # Erstelle ein Subject mit dem Namen "Max" und setze die Attribute
    max_subject = Subject("Max", "Mustermann", birthdate=date(1990, 5, 15),
                          study_area="Informatik", sex="männlich", email="max@example.com")

    # Aktualisiere die E-Mail-Adresse
    person = Person("Max", "Mustermann")

    max_subject.update_email()
    person.put()

if __name__ == "__main__":
    main()
