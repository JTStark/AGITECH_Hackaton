status = 'transf0'
operacao = {}

def receive_message(userId, message):
	if(status == 'init'):
		if(message == 'transferencia'):	
			status = 'tranf1'
			operacao['op'] = 'transferencia'
			return 'Quanto quer mandar?'
		elif(message == 'saldo'):
			status = 'saldo'
			operacao['op'] = 'saldo'
		elif(message == 'extrato'):
			status = 'extrato1'
			operacao['op'] = 'extrato'
			return 'Qual o período que deseja ver?'
		elif(message == 'pagar boleto'):
			status = 'boleto1'
			operacao['op'] = 'boleto'
			return 'Digite o código do boleto que quer pagar.'
		else:
			status = 'receber1'
			operacao['op'] = 'receber'
			return 'Quanto quer pedir para o responsável?'
	elif(status == 'transf1'):
		status = 'transf2'
		operacao['valor'] = message
		return 'Mandar para quem?'
	elif(status == 'transf2'):
		status = 'transf3'
		operacao['destino'] = message



Extrato
Qual o período que deseja ver?
	Op1: Hoje
	Op2: Essa semana
	Op3: Mes

Saldo

Receber
Quanto quer pedir para o responsável?

Pagar boleto
Digite o código do boleto que quer pagar

Transfeência
Quanto quer mandar?
Mandar para quem?
	Ops: mostrar cada dependente