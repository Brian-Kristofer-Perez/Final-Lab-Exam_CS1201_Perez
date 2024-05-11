import os
import utils.user as user


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
			name_and_pass = str.split(file.read().strip(), "\n")  # returns a list

			for i in name_and_pass:
				self.info.append(str.split(i, ", "))

			for name, password in self.info:
				self.content.append(user.User(name, password))


	def save_users(self):
		pass

	def validate_username(self, username):

		if len(username) < 4:
			return 1

	def validate_password(self, password):
		pass

	def register(self):
		pass

	def login(self):
		pass




usermanager = UserManager()


def main():
	usermanager.load_users()




if __name__ == "__main__":
	main()