import random


class Entity:

    def roll_dice(self):  #for inheritance
        self.dice = random.randint(1, 6)


        """
        user and cpu inherits methods and others in entity
        
                 Entity
                    |
                    |
        _________________________
        |                       |
        |                       |
        v                       v
       User                    CPU

        
        """



class User(Entity):

    def __init__(self, name, password):
        self.name = name
        self.password = password

        self.dice = 0

        self.score = Scores()  #score object, it has both best of 3 and normal scores


class CPU(Entity):

    def __init__(self):
        self.name = "CPU"
        self.dice = 0
        self.best_of_3 = BestOf3()  #unlike the player object, this only has the best of 3 component




class Scores:

    def __init__(self):
        self.total_score = 0
        self.stages_won = 0

        self.best_of_3 = BestOf3()


    """
    Visual representation of scores class
    
                    Scores
                        |
                        |
    ___________________________________________
    |                   |                     |
    |                   |                     |
    v                   v                     v
    total_score     stages won            best_of_3
                                              |
                                       ______________
                                       |            |
                                       v            v
                                      wins         score
    
    
    """

class BestOf3:

    def __init__(self):
        self.wins = 0
        self.score = 0


