import json
from my_classes import Person, Experiment
from my_functions import build_person, build_experiment

def test():

  
    supervisor = build_person("Helin", "Hussein", "female", 21, "estimate_max_hr")
    subject= build_person("Helium", "stickstoff", "male", 41)
    
    experiment=build_experiment("Belastungsekg", "12.03.2024", supervisor, subject)

    with open("experiment_test.json", "w") as outfile:
        json.dump(experiment.__dict__, outfile, default=lambda o: o.__dict__, indent=4)

    print("Test ist abgeschlossen. Daten wurden in 'experiment_test.json' gespeichert.")

if __name__ == "__main__":
    test()
