import random


class Entity:

    def roll_dice(self):  #for inheritance
        self.dice = random.randint(1, 6)



class User(Entity):

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.dice = 0

        self.score = Scores()


class CPU(Entity):

    def __init__(self):
        self.name = "CPU"
        self.dice = 0
        self.best_of_3 = BestOf3()




class Scores:

    def __init__(self):
        self.total_score = 0
        self.stages_won = 0

        self.best_of_3 = BestOf3()


class BestOf3:

    def __init__(self):
        self.wins = 0
        self.score = 0


