import utils.dice_game as dice_game
import utils.user_manager as user_manager


class Menu:

    def main_menu(self):
        while True:
            try:
                print("Welcome to Dice Roll Game!")
                print("1. Register")
                print("2. Log in")
                print("3. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    user_manager.usermanager.register()
                    break
                elif choice == 2:
                    user_manager.usermanager.login()
                    break
                elif choice == 3:
                    print("Thank you for playing")
                    exit(0)
                else:
                    print("Enter a valid input\n")
                    continue

            except ValueError:
                print("Invalid choice\n")
                continue


    def login_menu(self, user_obj):
        while True:
            try:

                print(f"Welcome, {user_obj.name}!")

                print("Log in Menu")
                print("1. Start Game")
                print("2. View Leaderboard")
                print("3. Log out")

                choice = int(input("Enter choice: "))

                if choice == 1:

                    game = dice_game.DiceGame(user_obj)
                    game.play_game()
                    break
                elif choice == 2:
                    break
                    pass
                elif choice == 3:
                    # main_menu()
                    break
                else:
                    print("Enter a Valid Input\n")
            except ValueError:
                print("Invalid choice\n")


menu = Menu()

if __name__ == "__main__":

    menu.main_menu()