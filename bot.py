import telebot
import config
from random import choice

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def message_start(message):
    bot.send_message(message.chat.id, "Привет! Я Кико-бот")

# \n - переход на новую строку

@bot.message_handler(commands=["help"])
def message_start(message):
    bot.send_message(message.chat.id, "У меня есть команда start - чтобы начать общение  \n")

@bot.message_handler(content_types=["text"])
def dialog(message):
    m = message.text
    m = m.lower()
    # from random import randint
    if m == "привет":
        hello = ["hello", "Привет", "Здравствуй"]
        bot.send_message(message.chat.id, choice(hello))
    elif m == "lol":
        bot.send_message(message.chat.id, "kek")
    elif m == "шутка":
        bot.send_message(message.chat.id, "аххахаха")

if __name__ == "__main__":
    bot.infinity_polling()
