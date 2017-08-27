import apiai

CLIENT_ACCESS_TOKEN = '59ce8c44bceb47aba5718afc297339f7'

def parse_message(message):
	conn = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
	request = ai.text_request()
	request.lang = 'pt-BR'    #optional, default value equal en
	request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
	request.query = message
	response = request.getresponse()
	return response


parse_message("transfere")
