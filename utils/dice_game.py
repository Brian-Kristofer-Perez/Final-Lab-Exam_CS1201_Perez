
import utils.user as user
import utils.menu as menu
import os
from datetime import datetime



class DiceGame:


    def __init__(self, current_user):
        self.player = current_user  #load the player object
        self.opponent = user.CPU()

        self.rankings = []


        if not os.path.exists("utils/data"):  # if no data folder, make files & folder
            os.makedirs("utils/data")
            with open("utils/data/rankings.txt", "w") as file:  #create a data folder with ranking file
                file.close()

        if not os.path.exists("utils/data/rankings.txt"):
            with open("utils/data/rankings.txt", "w") as file:  #if data folder exists but not file, create a ranking file
                file.close()

        with open("utils/data/rankings.txt") as file:
            if not file.read():
                pass

            else:
                self.read_rankings()  #read ranking and add them to list






    def read_rankings(self):

        with open("utils/data/rankings.txt", "r") as file:

            unread_rankings = str.split(file.read().strip(), "\n")

            for i in unread_rankings:

                self.rankings.append(str.split(i, ": "))


    def show_top_scores(self):

        with open("utils/data/rankings.txt") as file:
            if not file.read():
                print("Empty leaderboard. Play a game to add a record!")

            else:

                self.rankings.sort(key=lambda x: int(x[1]), reverse=True)  #sort rankings by score

                count = 1

                for i in self.rankings[:10]:  #pick out only the top 10 best among all scores in the file
                    print(f"{count}. {i[0]}: Points - {i[1]}, Stages - {i[2]}")

                    count += 1


    def save_scores(self):
        with open("utils/data/rankings.txt", "a") as file:

            # save file with date
            file.write(f"{self.player.name}: {self.player.score.total_score}: {self.player.score.stages_won}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

            # add to list
            self.rankings.append(str.split(f"{self.player.name}, {self.player.score.total_score}, {self.player.score.stages_won}", ", "))

            file.close()

            # reset all player scores after saving
            self.player.score.total_score = 0
            self.player.score.stages_won = 0

            print("Scores saved to local leaderboard.")


    def play_game(self):

        while True:  #the actual gameplay


            """The main flow goes something like this:
            
                While True:
                    1. roll dice
                    2. compare dice
                    3. check if player won or lost
                    
                    repeat 1-3 until someone gets 3 wins 
                    
                    4a. if player gets 3 wins, give option to go again or leave and save results
                    4b. if not, then go back to menu
            
            
            """

            self.player.roll_dice()
            self.opponent.roll_dice()

            print(f"{self.player.name} rolled: {self.player.dice}")
            print(f"{self.opponent.name} rolled: {self.opponent.dice}")

            self.compare_dice()

            if self.player.score.best_of_3.score == 3:  #if you win a stage!

                self.win()  #win!

                next_stage = self.menu()  #give option to go for another stage

                if next_stage:
                    continue

                if not next_stage:
                    self.save_scores()
                    menu.menu.login_menu(self.player)



            if self.opponent.best_of_3.score == 3:  # if you lose a stage
                self.lose()
                break



    def compare_dice(self):

        if self.player.dice > self.opponent.dice:  # won

            self.player.score.best_of_3.score += 1
            self.player.score.total_score += 1

            print(f"You won this round, {self.player.name}!")


        elif self.player.dice < self.opponent.dice:  # lost

            self.opponent.best_of_3.score += 1

            print(f"{self.opponent.name} won this round!")

        else:

            print("It's a tie!")



    def win(self):

        self.player.score.best_of_3.score = 0  # reset in-game scores
        self.opponent.best_of_3.score = 0

        self.player.score.stages_won += 1  # add the wins and points
        self.player.score.total_score += 3

        print(f"You won this stage, {self.player.name}!")  # win message!
        print(f"Total points: {self.player.score.total_score}, Stages won: {self.player.score.stages_won}\n")


    def lose(self):

        print("Game over. You didn't win any stages.")

        self.player.score.best_of_3.score = 0  #reset scores
        self.opponent.best_of_3.score = 0

        self.player.score.total_score = 0  #reset wins
        self.player.score.stages_won = 0


    def menu(self):

        while True:
            try:
                choice = int(input("Do you want to continue to the next stage? (1: Yes, 2: No): "))

                if choice == 1:
                    return True

                if choice == 2:
                    return False

                else:
                    print("Input a valid number!")
                    continue

            except ValueError:

                print("Input a valid number!")
                continue

