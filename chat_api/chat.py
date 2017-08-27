"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot
from pymessenger import Element
from pymessenger import Button
from os import environ
import sys
sys.path.append('../')
import internal_processing.apiai_get as apiai_get



app = Flask(__name__)

ACCESS_TOKEN = "EAAEygPWKlxQBAAfVMjE9Lx9dZAxysVTbQlQ3GVCQukz2HDFuptDkEW2FZBLKOuj1ZArZBpkQfoTxZB9BaLHsON2hE6bt2RW6ibvZAsZBJNw2lUE0PmKnG277wR9yueRGSUB98adgHBb8f7YjvikVZBiOtH1J70Kkz1CgIZCzE34AgkgZDZD"
APP_SECRET = "ac3dd707db4f818e1c9f42db9d38ab94"
VERIFY_TOKEN = "test_token"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        print("message1")
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    print("message2")
                    if x['message'].get('text'):
                        message = x['message']['text']
                        buttons = []
                        button = Button(type='postback', title="select option 1", payload="1")
                        #button = Button(type='web_url', url='http://www.students.ic.unicamp.br/~ra158044/visa_checkout.html?value=50', title='Button', webview_height_ratio='full',webview_share_button='hide')
                        buttons.append(button)
                        button = Button(type='postback', title="select option 2", payload="2")
                        buttons.append(button)
                        text = 'Select'
                        result = bot.send_button_message(recipient_id, text, buttons)
        return "Success"


if __name__ == "__main__":
    app.run(port=environ.get('PORT'), host='0.0.0.0')
