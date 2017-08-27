import apiai

CLIENT_ACCESS_TOKEN = '0b41530420854cd3a671a41a46553862'

def parse_message(message):
	conn = apiai.ApiAI('0b41530420854cd3a671a41a46553862')
	request = ai.text_request()
	request.lang = 'pt-BR'    #optional, default value equal en
	request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
	request.query = message
	response = request.getresponse()
	return response


parse_message("transfere")
