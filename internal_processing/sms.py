import requests

def send_sms(phone, cod):
	requests.post('https://textbelt.com/text', {'phone': '5519983168458','message': 'Hello world','key': 'f0fbd85507ed2eb656dd1da626e1ff77bca76157BYHGKj19tkEj4rruWICZBBNTy',})

	#f0fbd85507ed2eb656dd1da626e1ff77bca76157BYHGKj19tkEj4rruWICZBBNTy

	#requests.post('https://textbelt.com/text', {'phone': '+5519983168458', 'message': 'Ola mundo', 'key':'f0fbd85507ed2eb656dd1da626e1ff77bca76157BYHGKj19tkEj4rruWICZBBNTy'})

	#