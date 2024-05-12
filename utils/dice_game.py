
import utils.user as user
import utils.menu as menu
import os



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
                self.read_rankings()


    def show_top_scores(self):

        with open("utils/data/rankings.txt") as file:
            if not file.read():
                print("Empty leaderboard. Play a game to add a record!")

            else:

                self.rankings.sort(key=lambda x: int(x[1]), reverse=True)

                for i in self.rankings[:10]:
                    print(f"{i[0]}: Points - {i[1]}, Stages - {i[2]}")


    def read_rankings(self):

        with open("utils/data/rankings.txt", "r") as file:

            unread_rankings = str.split(file.read().strip(), "\n")

            for i in unread_rankings:

                self.rankings.append(str.split(i, ": "))


    def save_scores(self):
        with open("utils/data/rankings.txt", "a") as file:

            file.write(f"{self.player.name}: {self.player.score.total_score}: {self.player.score.stages_won}")

            self.rankings.append(str.split(f"{self.player.name}, {self.player.score.total_score}, {self.player.score.stages_won}", ", "))

            file.close()

            print("Scores saved to local leadeerboard.")


    def play_game(self):

        while True:  #the actual gameplay


            """The main flow goes something like this:
            
                While True:
                    1. roll dice
                    2. compare dice
                    3. compare dice
                    4. check if player won or lost the stage
                    
                    4a. if player won, give option to go again
                    4b. if not, then go back to menu
            
            
            """

            self.player.roll_dice()
            self.opponent.roll_dice()

            print(f"{self.player.name} rolled: {self.player.dice}")
            print(f"{self.opponent.name} rolled: {self.opponent.dice}")

            self.compare_dice()

            if self.player.score.best_of_3.score == 3:  #if you win a stage!

                self.win()

                next_stage = self.menu()

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

