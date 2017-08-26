import csv
import ast
import json

############### CONSTANTS ##################

header_db = ['Facebook_ID','Name', 'Owner_ID', 'Childs_ID', 'Current_state']
db_folder = '../data/'
db_name = 'db.csv'

#Errors
user_id_not_found = 'user id not found'

#States
initializing_state = 'init'

example_child1 = [1234, 'Guilherme', 1236, [], initializing_state]
example_child2 = [1235, 'Joao', 1236, [], initializing_state]
example_father = [1236, 'Pedro', 0, [1234,1235], initializing_state]
example_child_alone = [1238, 'Leonardo', 0, [], initializing_state]
examples = [example_child1, example_child2, example_father, example_child_alone]

json_example = '{\"Facebook_ID\":1232,\"name\":\"Augusto\",\"owner_ID\":333,\"childs_ID\":\"[]\", \"current_state\":\"init\"}'
json_example_children = '{\"Facebook_ID\":1231,\"name\":\"Fernando\",\"owner_ID\":0,\"childs_ID\":\"[]\", \"current_state\":\"init\"}'


############## CLASSES ##############

class User:

	def __init__(self, facebook_ID, name, owner_ID, childs_ID, current_state):
		self.facebook_ID = int(facebook_ID)
		self.name = name
		self.owner_ID = int(owner_ID)
		if childs_ID == '[]':
			self.childs_ID = []
		else:
			childs_ID = childs_ID.split('[')[1]
			childs_ID = childs_ID.split(']')[0]
			childs_ID_splited = childs_ID.split(',')
			self.childs_ID = []
			for ID in childs_ID_splited:
				self.childs_ID.append(int(ID))
		self.current_state = current_state



class Data_base:

	users = [[]]
	file_name = ''

	def __init__(self, name):
		self.file_name = name
		self.read()


	def create(self, users):
		with open(self.file_name, 'w') as arq:
			arqCsv = csv.writer(arq)
			arqCsv.writerow(header_db)
			for user in users:
				arqCsv.writerow(user)


	def update(self):
		with open(self.file_name, 'w') as arq:
			arqCsv = csv.writer(arq)
			arqCsv.writerow(header_db)
			for user in self.users:
				arqCsv.writerow(user)

	def read(self):
		with open(self.file_name, 'r') as arq:
			arqCsv = csv.reader(arq)
			arqCsv.next()
			for user in arqCsv:
				self.users.append(user)
			self.users.pop(0)

	def create_user(self, index):
		user = self.users[index]
		return User(user[0], user[1], user[2], user[3], user[4])

	def get_user_by_id(self, user_id):

		user_found = False
		db_length = len(self.users)
		init = 0
		position = db_length/2

		while not user_found:

			user = self.create_user(position)
			#print user
			if user.facebook_ID == user_id:
				user_found = user
			else:

				if db_length == init + 1 or db_length == init:
					raise NameError('User ID not found: ' + str(user_id))

				if user.facebook_ID > user_id:
					db_length = position
					position = init + (position - init)/2
					
					
				else:
					init = position
					position += (db_length - position)/2

		return user_found

	def get_parent(self, child_id):

		try:
			child_user = self.get_user_by_id(child_id)
		except:
			raise NameError('Child ID not found: ' + str(child_id))

		try:
			return self.get_user_by_id(child_user.owner_ID)
		except:
			raise NameError('Child ID has no owner: ' + str(child_id))

	def get_childs(self, owner_ID):
		try:
			owner_user = self.get_user_by_id(owner_ID)
		except:
			raise NameError('Owner ID not found: ' + str(owner_ID))

		
		children_list = owner_user.childs_ID
		if children_list == []:
			raise NameError('Owner ID has no children: ' + str(owner_user.facebook_ID))
		return [get_user_by_id(owner_ID_iterate) for owner_ID_iterate in children_list]

	def get_child_by_name(self, owner_ID, name):
		childs = self.get_childs(owner_ID)
		for child in childs:
			if child.name == name:
				return child
		raise NameError('The ID: ' + str(owner_ID) + ' has no children with name: ' + name)

	def parse_user_to_list(self, user):
		return [user.facebook_ID, user.name, user.owner_ID, user.childs_ID, user.current_state]

	def add_user_to_db(self, new_user):
		user_found = False
		db_length = len(self.users)
		init = 0
		position = db_length/2
		user_id = int(new_user.facebook_ID)

		user = self.create_user(0)
		if user_id < int(user.facebook_ID):
			self.users.insert(0, self.parse_user_to_list(new_user))
			return

		while True:

			print position
			user = self.create_user(position)
			#print user
			if int(user.facebook_ID) == user_id:
				raise NameError('User ID already exists: ' + str(user_id))
			else:

				if db_length == init or db_length == init +1:
					self.users.insert(position+1, self.parse_user_to_list(new_user))
					return

				if int(user.facebook_ID) > user_id:
					db_length = position
					position = init + (position - init)/2
					
					
				else:
					init = position
					if len(self.users) - position == 1:
						self.users.append(self.parse_user_to_list(new_user))
						return
					position += (db_length - position)/2
					


	def user_exists(self, user_ID):

		try:
			a = self.get_user_by_id(user_ID)
			return True
		except:
			return False

	#Data is JSON
	def add_user(self, user_data):
		data = json.loads(user_data)
		user = User(data['Facebook_ID'], data['name'], data['owner_ID'], str(data['childs_ID']), initializing_state)
		self.add_user_to_db(user)

	def update_user(self, user_update):
		user_found = False
		db_length = len(self.users)
		init = 0
		position = db_length/2
		user_id = user_update.facebook_ID

		while True:

			user = self.create_user(position)
			#print self.users
			#print user
			if user.facebook_ID == user_id:
				db.users[position] = self.parse_user_to_list(user)
				return
			else:

				if db_length == init + 1 or db_length == init:
					raise NameError('User ID not found: ' + str(user_id))

				if user.facebook_ID > user_id:
					db_length = position
					position = init + (position - init)/2
					
					
				else:
					init = position
					position += (db_length - position)/2


	def add_children(self, father_ID, child_data):
		child_json = json.loads(child_data)
		child = User(child_json['Facebook_ID'], child_json['name'], father_ID, '[]', initializing_state)
		father = self.get_user_by_id(father_ID)


		if self.user_exists(child.facebook_ID):
			child.owner_ID = father_ID
			father.childs_ID.append(child.facebook_ID)
			self.update_user(child)
			self.update_user(father)
		else:
			self.add_user_to_db(child)
			print 'n'


############# MAIN ##############

db = Data_base(db_folder + db_name)

print db.users

db.add_children(1238, json_example_children)

print db.users

