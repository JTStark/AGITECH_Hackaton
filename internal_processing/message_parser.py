from .server import *
import ast

db = Data_base(db_folder + db_name)

def receive_message(userId, message):
	status = db.get_user_state(userId)
	operacao = ast.literal_eval(db.get_user_dictionary(userId))
	if(('cancelar' in message.split()) or ('cancela' in message.split())):
		db.set_user_dictionary(userId, '{}')
		db.set_user_state(userId, 'escolha')
		return 'Operacao cancelada. O que deseja fazer agora? Digite 1 para transferencia, 2 para saldo, 3 para extrato e 4 para boleto.'
	elif(status == 'init'):
		db.set_user_state(userId, 'escolha')
		return 'Ola! O que gostaria de fazer? Digite \n1 para transferencia, \n2 para saldo, \n3 para extrato, \n4 para boleto e \n5 para receber.'
	elif(status == 'escolha'):
		if(message == '1'):
			print('ELE CHAMOU 1')
			db.set_user_state(userId, 'transf1')
			operacao['op'] = 'transferencia'
			db.set_user_dictionary(userId, str(operacao))
			print('ELE CHAMOU 1')
			return 'Quanto quer mandar?'
		elif(message == '2'):
			print('ELE CHAMOU 2')
			db.set_user_state(userId, 'saldo1')
			operacao['op'] = 'saldo'
			db.set_user_dictionary(userId, str(operacao))
			print('ELE CHAMOU 2')
			balance = user.card.get_balance()
			return 'Seu saldo equivale a R$' + str(balance)	+ '\n\nCaso queira fazer alguma outra operacao, fale comigo!' 
		elif(message == '3'):
			print('ELE CHAMOU 3')
			db.set_user_state(userId, 'extrato1')
			operacao['op'] = 'extrato'
			db.set_user_dictionary(userId, str(operacao))
			print('ELE CHAMOU 3')
			return 'Qual o período que deseja ver? Temos as opções: hoje, semana ou mes.'
		elif(message == '4'):
			print('ELE CHAMOU 4')
			db.set_user_state(userId, 'boleto1')
			operacao['op'] = 'boleto'
			db.set_user_dictionary(userId, str(operacao))
			print('ELE CHAMOU 4')
			return 'Digite o código do boleto que quer pagar.'
		else:
			db.set_user_state(userId, 'receber1')
			operacao['op'] = 'receber'
			db.set_user_dictionary(userId, str(operacao))
			return 'Quanto quer pedir para o responsável?'
	elif(status == 'transf1'):
		if(message is not int):
			return 'Desculpe, acho que você digitou errado. Diga novamente o valor que deseja transferir.'
		db.set_user_state(userId, 'transf2')
		operacao['valor'] = message
		db.set_user_dictionary(userId, str(operacao))
		return 'Mandar para quem?'
	elif(status == 'transf2'):
		try:
			db.get_child_by_name(userId, message)
		except:
			return 'Nome não encontrado. Por gentileza, digite o nome corretamente. Pode ser também que você não tenha dependentes, então use cancelar para parar o procedimento atual.'
		db.set_user_state(userId, 'transf3')
		operacao['destino'] = message
		db.set_user_dictionary(userId, str(operacao))
	elif(status == 'extrato1'):
		if(not(message.lower() in ['hoje', 'semana', 'mes'])):
			return 'A opção que você digitou não existe. Por favor, escolha entre hoje, semana ou mes.'
		db.set_user_state(userId, 'extrato2')
		operacao['periodo'] = message
		db.set_user_dictionary(userId, str(operacao))
	elif(status == 'boleto1'):
		if(message is not int):
			return 'O código esta errado. Pode repetir por favor?'
		db.set_user_state(userId, 'boleto2')
		operacao['codigo'] = message
		db.set_user_dictionary(userId, str(operacao))
	elif(status in ['saldo1', 'receber2', 'boleto2', 'transf3', 'extrato2']):
		db.set_user_dictionary(userId, '{}')
		db.set_user_state(userId, 'escolha')
		user = db.create_user_by_id(userId)
		if(status == 'saldo1'):
			balance = user.card.get_balance()
			return 'Seu saldo equivale a R$' + str(balance)	+ '\n\nCaso queira fazer alguma outra operacao, fale comigo!'
		elif(status == 'transf3'):
			initialize_payment_interface(userId, operacao['valor'])
			json = requests.get('https://www.ic.unicamp.br/~ra158044/')
			user.card.credit(float(operacao['valor']))
		return operacao

print(receive_message(1236, 'Joao'))
#print(db.users)



# Extrato
# Qual o período que deseja ver?
# 	Op1: Hoje
# 	Op2: Essa semana
# 	Op3: Mes

# Saldo

# Receber
# Quanto quer pedir para o responsável?

# Pagar boleto
# Digite o código do boleto que quer pagar

# Transfeência
# Quanto quer mandar?
# Mandar para quem?
# 	Ops: mostrar cada dependente
