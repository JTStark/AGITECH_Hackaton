from smsapi import SmsApi

def send_sms(phone, cod):
	username = "<USERNAME>"
    password = "<PASSWORD>"
    sms = SmsApi(username, password)
    sms = sms.send_sms(recipient="48123456789",sender_name="SENDER", message="MESSAGE",eco=False,)
    print sms