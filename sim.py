# importing
import random

# the patient
class Patient:
    def __init__(self, name):
        self.name = name

# paul bad
patient = Patient('Paul')

# virus related variables also very long arrays
virusList = ['Ebolavirus', 'Coronavirus', 'Bubonic Plague', 'Tetanus', 'SARS', 'MERS', 'H7N9 Bird Flu', 'H5N1 Bird Flu', 'Marburg Virus', 'HeV', 'NiV', 'Black Fungus', 'Dengue Fever', 'Naegleriasis', 'Rabies']
mortalityRate = [40, 2, 60, 50, 11, 34, 39, 59, 80, 57, 78, 60, 26, 99, 101]
selectedVirus = random.randint(0, len(virusList) - 1)

# the random trio
randomNumber = random.randint(0, 100)
randomNumber2 = random.randint(0, 5)
randomNumber3 = random.randint(0, 100)

# wanted alive NOT dead
timesDied = 0
timesLived = 0

# the lonely variable :(
repetition = random.randint(100000, 1000000)

# statements and printing
print(f'Welcome to my probability simulation. {patient.name} is ill with {virusList[selectedVirus]}. This simulation will repeat {repetition} times.')
print('Calculating...')

# looping
for i in range(repetition):
    if mortalityRate[selectedVirus] <= randomNumber:
        if randomNumber3 > randomNumber2:
            timesLived += 1
    else:
            timesDied += 1
    randomNumber = random.randint(0, 100)
    randomNumber2 = random.randint(0, 5)
    randomNumber3 = random.randint(0, 100)

# final print
print(f'{patient.name} lives {timesLived} times, and  dies {timesDied} times in the simulation. {patient.name} survives around {round(timesLived/(timesLived + timesDied) * 100, 2)}% of the time.')