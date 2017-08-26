import csv


############### CONSTANTS ##################

header_db = ['Facebook_ID','Name', 'Owner_ID', 'Childs_ID', 'Current_state']
db_folder = '../data/'
db_name = 'db.csv'

#States
initializing_state = 'init'


users = [[]]

example_child1 = [1234, 'Guilherme', 1236, 0, initializing_state]
example_child2 = [1235, 'Joao', 1236, 0, initializing_state]
example_father = [1236, 'Pedro', 0, [1234,1235], initializing_state]
example_child_alone = [1237, 'Leonardo', 0, 0, initializing_state]
examples = [example_child1, example_child2, example_father, example_child_alone]


############## CLASSES ##############

class Data_base:

	def __init__(self, name):
		self.file_name = name


	def create(self):
		with open(db_folder + db_name, 'w') as arq:
			arqCsv = csv.writer(arq)
			arqCsv.writerow(header_db)
			for user in examples:
				arqCsv.writerow(user)


	def update(self):
		with open(db_folder + db_name, 'w') as arq:
			arqCsv = csv.writer(arq)
			arqCsv.writerow(header_db)
			for user in users:
				arqCsv.writerow(user)

	def read(self):
		with open(db_folder + db_name, 'r') as arq:
			arqCsv = csv.reader(arq)
			arqCsv.next()
			for user in arqCsv:
				users.append(user)


############# FUNCTIONS #############

############# MAIN ##############

db = Data_base(db_folder + db_name)
db.read()

print users

