"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot
from os import environ

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
                        elements = []
                        element = Element(title="test", image_url="http://orig06.deviantart.net/562d/f/2014/187/e/8/half_life_3_logo__with_lightning_effect__by_stavrapid_official-d7pho0q.png", subtitle="subtitle", item_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                        elements.append(element)
                        bot.send_generic_message(recipient_id, elements)
                        print(recipient_id + " " + message)
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=environ.get('PORT'), host='0.0.0.0')
