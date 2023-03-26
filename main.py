from flask import Flask, render_template, request
import logging
from src import bot 

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    logger.info(f"User said: {user_input}")
    response = bot.chatbot(user_input)
    return response

if __name__ == "__main__":
    app.run()