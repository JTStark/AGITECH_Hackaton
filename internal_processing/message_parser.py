from server import *

db = Data_base(db_folder + db_name)
operacao = {}

receive_message(1234, saldo)
print(db.users)

def receive_message(userId, message):
	status = db.get_user_state(userId)
	if(status == 'init'):
		if(message == 'transferencia'):	
			db.set_user_state(userId, 'transf1')
			operacao['op'] = 'transferencia'
			return 'Quanto quer mandar?'
		elif(message == 'saldo'):
			db.set_user_state(userId, 'saldo1')
			operacao['op'] = 'saldo'
		elif(message == 'extrato'):
			db.set_user_state(userId, 'extrato1')
			operacao['op'] = 'extrato'
			return 'Qual o período que deseja ver?'
		elif(message == 'pagar boleto'):
			db.set_user_state(userId, 'boleto1')
			operacao['op'] = 'boleto'
			return 'Digite o código do boleto que quer pagar.'
		else:
			db.set_user_state(userId, 'receber1')
			operacao['op'] = 'receber'
			return 'Quanto quer pedir para o responsável?'
	elif(status == 'transf1'):
		db.set_user_state(userId, 'transf2')
		operacao['valor'] = message
		return 'Mandar para quem?'
	elif(status == 'transf2'):
		db.set_user_state(userId, 'transf3')
		operacao['destino'] = message
	elif(status == 'extrato1'):
		db.set_user_state(userId, 'extrato2')
		operacao['periodo'] = message
	elif(status == 'boleto1'):
		db.set_user_state(userId, 'boleto2')
		operacao['codigo'] = message
	elif(status == 'receber1'):
		db.set_user_state(userId, 'receber2')
		operacao['valor'] = message
	elif(status in ['saldo1', 'receber2', 'boleto2', 'transf3', 'extrato2']):
		return operacao


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