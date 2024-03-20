def calc_mean(list_of_measurements : list[int]):
    """ Eine Funktion, die eine Liste von Werten übernimmt und das arithmetische Mittel zurück gibt"""
    mittelwert = sum(list_of_measurements) / len(list_of_measurements)
    return mittelwert
mean = calc_mean(list_of_measurements = [1,2,3])
