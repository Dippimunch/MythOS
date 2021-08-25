class Location:
    def __init__(self, name, size, population):
        self.name = name
        self.size = size
        self.population = population
        self.list = []

    def census(self):
        censusList = []
        for p in range(len(self.list)):
            censusList.append(self.list[p].name)
        print(censusList)
    
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.inventory = []

    def move(self, target, speed):
        current = self.location
        # distance and speed
        self.location = target

class Language:
    def __init__(self, name, consonants, vowels, base, words, features={}):
        self.consonants = consonants
        self.vowels = vowels
        self.base = base
        self.words = words
        
        # Features *kwargs? How to reduce space
        # https://wals.info/feature

        # AREA
        # Phonology
        # ID/NAME/VALUE
        # {id: {feature: 'x', value: 'y'}}
        # featurization
        
