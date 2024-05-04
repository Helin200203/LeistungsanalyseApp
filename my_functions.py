
def estimate_max_hr(age_years: int, sex: str) -> int:
    if sex == "male":
        return 223 - 0.9 * age_years
    elif sex == "female":
        return 226 - 1.0 * age_years
    try:
        # Sicherstellen, dass die Eingabe korrekt verarbeitet wird.
        return int(input("Enter maximum heart rate:"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def create_person(first_name: str, last_name: str, sex: str, age: int) -> dict:
    """Erstellt ein Dictionary mit Informationen über eine Person."""
    person_info = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "estimate_max_hr": estimate_max_hr(age, sex)
    }
    return person_info
  

def build_experiment(experiment_name: str, date: str, supervisor: dict, subject: dict) -> dict:
    """Erstellt ein Dictionary mit Informationen über ein Experiment."""
    experiment_info = {
        "experiment_name": experiment_name,
        "date": date,
        "supervisor": supervisor,
        "subject": subject
    }
    return experiment_info