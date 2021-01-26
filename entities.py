class Location:
    def __init__(self, name, size, population):
        self.name = name
        self.size = size
        self.population = population
        self.list = []

    def census(self):
        censusList = []
        for p in range(len(self.list)):
            censusList.append(p)
        print(censusList)
    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inventory = []
        
class Language:
    def __init__(self, name, consonants, vowels, dictionary):
        self.consonants = consonants
        self.vowels = vowels
        self.dictionary = dictionary
