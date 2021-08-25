from climate import get_weather


class Player:
    def __init__(self, name, inv_cap, fill):
        self.name = name
        self.inv_cap = inv_cap
        self.fill = fill

        actions = ['plant']

    def plant(self, seed, plant_list):
        plant_list.append(Plant('veg', 0, 180, 0, 1000, 10, 10, 10, 10))
        

class Plant:
    def __init__(self, name, age, max_age, size, max_size, growth_rate, water_need, max_prod, prod_age):
        self.name = name
        self.age = age
        self.max_age = max_age
        self.size = size
        self.max_size = max_size
        self.growth_rate = growth_rate
        self.water_need = water_need
        self.max_prod = max_prod
        self.alive = True

        self.prod_amount = 0
        self.prod_age = prod_age
        produce = self.name + " produce"

    def die(self):
        print('DEAD')
        self.alive = False

class Menu:
    def __init__(self, title, options):
        self.title = title
        self. options = options

player = Player('Player', 200, 100)

day = 1
year = 0
year_length = 360

play = True


abc = 'abcdefghijklmnopqrstuvwxyz'
main = Menu('MAIN', ['plant'])
game_state = 'MAIN'

#veg = Plant('Veg', 175, 180, 0, 1000, 10, 10, 10, 10) 
plant_list = []

while play == True:
    if game_state == 'MAIN':
        print(f'day: {day}\nyear: {year}')
        #print(veg.age)
        # input list
        action = input(main.options)

        if action == 'plant':
            player.plant(None, plant_list)

        print(plant_list)
        day += 1
        for plant in plant_list:
            plant.age += 1
            if plant.age >= plant.max_age:
                plant.die()
        if day == year_length:
            day = 1
            year += 1
            
