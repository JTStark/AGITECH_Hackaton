"""
This bot listens to a port for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot
from pymessenger import Element
from pymessenger import Button
from os import environ
import sys
sys.path.insert(0, '../internal_processing/')
import message_parser as parser


app = Flask(__name__)

ACCESS_TOKEN = "EAAEygPWKlxQBAAfVMjE9Lx9dZAxysVTbQlQ3GVCQukz2HDFuptDkEW2FZBLKOuj1ZArZBpkQfoTxZB9BaLHsON2hE6bt2RW6ibvZAsZBJNw2lUE0PmKnG277wR9yueRGSUB98adgHBb8f7YjvikVZBiOtH1J70Kkz1CgIZCzE34AgkgZDZD"
APP_SECRET = "ac3dd707db4f818e1c9f42db9d38ab94"
VERIFY_TOKEN = "test_token"
bot = Bot(ACCESS_TOKEN)


@app.route("/webhook", methods=['GET', 'POST'])
def hello():


    if request.method == 'GET':
        print("GOT A GET!!!")
        print(request.args.get("source"))
        #if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        #    return request.args.get("hub.challenge")
        #else:
        #    return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        print(output)
        print("OUTPUT RIGHT UP")
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        answer = parser.receive_message(recipient_id, message)
                        bot.send_text_message(recipient_id, answer)
                else:
                    pass
        return "Success"

def send_message(user_id, message):
    bot.send_text_message(user_id, message)

def initialize_payment_interface(user_id, amount):
    buttons = []
    button = Button(type='web_url', url='http://www.students.ic.unicamp.br/~ra158044/visa_checkout.html?value=50', title='Payment', webview_height_ratio='tall',webview_share_button='hide')
    buttons.append(button)
    text = 'Please click here to complete'
    result = bot.send_button_message(recipient_id, text, buttons)


if __name__ == "__main__":
    app.run(port=environ.get('PORT'), host='0.0.0.0')
