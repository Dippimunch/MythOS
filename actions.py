actions = ['create', 'consume', 'convert', 'declare', 'demand', 'apply']
modifiers = ['or else', 'all', 'most', 'many', 'few']
things = []

class Thing:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
conversion = {'water' : {'cold' : 2}}

water = Thing('water', 100)
energy = 1000

def apply(subject, method, amount):
    # need some kind of table to check conversion values

    cost = conversion[subject.name][method] * amount
    # TODO: self.reagent
    #subject.energy -= cost
    subject.amount += amount

def status(subject):
    print('%s: %i' % (subject.name, subject.amount))


status(water)
#for thing in range(things)_:
    #apply('water', 'cold', 10)
apply(water, 'cold', 10)
status(water)
