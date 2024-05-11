
import utils.user as user


class DiceGame:

    def __init__(self, current_user):
        self.player = current_user  #load the player object
        self.opponent = user.CPU()


    def load_scores(self):
        pass

    def save_scores(self):
        pass

    # def play_game(self):
    #
    #     playing = True
    #     while playing:
    #         self.play_game_stage()


    def play_game(self):

        while self.player.score.best_of_3.score != 3 and self.opponent.best_of_3.score != 3:  #this breaks the loop when one of them turns 2

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
                    # save score()
                    break



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

    def show_top_scores(self):
        pass

    def logout(self):
        pass

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

