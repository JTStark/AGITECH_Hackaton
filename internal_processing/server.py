import csv
import ast

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


	def create(self):
		with open(self.file_name, 'w') as arq:
			arqCsv = csv.writer(arq)
			arqCsv.writerow(header_db)
			for user in examples:
				arqCsv.writerow(user)


	def update(self):
		with open(self.file_name, 'w') as arq:
			arqCsv = csv.writer(arq)
			arqCsv.writerow(header_db)
			for user in users:
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



############# FUNCTIONS #############

def get_user_by_id(db, user_id):

	user_found = False
	db_length = len(db.users)
	init = 0
	position = db_length/2

	while not user_found:

		user = db.create_user(position)
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

def get_parent(db, child_id):

	try:
		child_user = get_user_by_id(db, child_id)
	except:
		raise NameError('Child ID not found: ' + str(child_id))

	try:
		return get_user_by_id(db, child_user.owner_ID)
	except:
		raise NameError('Child ID has no owner: ' + str(child_id))

def get_children(db, owner_ID):
	try:
		owner_user = get_user_by_id(db, owner_ID)
	except:
		raise NameError('Owner ID not found: ' + str(owner_id))

	
	children_list = owner_user.childs_ID
	if children_list == []:
		raise NameError('Owner ID has no children: ' + str(owner_user.facebook_ID))
	return [get_user_by_id(db, owner_ID_iterate) for owner_ID_iterate in children_list]
	

def check_relationship(db, child, parent):
	pass

############# MAIN ##############

db = Data_base(db_folder + db_name)
db.read()

print get_children(db, 1236)[0].name

