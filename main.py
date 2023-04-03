from ai import ai
import telebot
from keys import TELEGRAM_BOT_KEY
from ai import ai
bot = telebot.TeleBot(TELEGRAM_BOT_KEY)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/ask':
        bot.send_message(message.from_user.id, "Type the description")
        bot.register_next_step_handler(message, get_description)
    else:
        bot.send_message(message.from_user.id, 'To ask about film type /ask')

def get_description(message):
    bot.send_message(message.from_user.id, ai.getFilm(message.text))

while (1):
    try:
        bot.polling()
    except Exception:
        pass