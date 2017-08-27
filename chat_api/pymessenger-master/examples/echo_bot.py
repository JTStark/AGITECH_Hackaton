"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot
from pymessenger import Element

app = Flask(__name__)

ACCESS_TOKEN = ""
VERIFY_TOKEN = ""
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
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        elements = []
                        element = Element(title="test", image_url="https://vignette4.wikia.nocookie.net/half-life/images/b/b9/Half-Life_3_logo.png/revision/latest/scale-to-width-down/220?cb=20160110005409&path-prefix=en", subtitle="subtitle", item_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                        elements.append(element)
                        bot.send_generic_message(recipient_id, elements)
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=5002, debug=True)
