import os
import utils.user as user
import menu


class UserManager:

	def __init__(self):



		self.content = []  #this list will contain player objects
		self.info = []  #temporary storage for processing


		# entire block is for initializing files
		if not os.path.exists("utils/data"):  #if no data folder, make files & folder
			os.makedirs("utils/data")
			file = open("utils/data/users.txt", "w")

		with open("utils/data/users.txt") as file:
			if not file.read():
				pass  # if empty, do not read accounts

			else:  # else read
				self.load_users()




	def load_users(self):

		with open("utils/data/users.txt") as file:
			name_and_pass = str.split(file.read().strip(), "\n")  # returns a list, excluding unncecessary newlines and spaces

			for i in name_and_pass:
				self.info.append(str.split(i, ", "))

			for name, password in self.info:
				self.content.append(user.User(name, password))


	def save_users(self, username, password):

		with open("utils/data/users.txt", "a") as file:
			file.write(f"{username}, {password}\n")
			file.close()
			usermanager.load_users()


	def register(self):
		while True:
			username = input("Input your username (at least 4 characters), or leave blank to return: ")

			if not username:
				menu.menu.main_menu()
				break

			if len(username) < 4:
				print("Please use a name with 4 or more characters.")
				continue

			if username in map(lambda x: x.name, usermanager.content):
				print("Username already exists, please try again.")
				continue

			password = input("Input your password (at least 8 characters), or leave blank to return: ")

			if not password:
				menu.menu.main_menu()
				break

			if len(password) < 8:
				print("Please use a password with 8 or more characters.")
				continue


			usermanager.save_users(username, password)
			print("Registration successful.\n")

			menu.menu.main_menu()

	def login(self):
		pass




usermanager = UserManager()


def main():
	usermanager.load_users()




if __name__ == "__main__":
	main()