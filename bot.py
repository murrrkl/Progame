import telebot
from random import choice

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def dialog(message):
    m = message.text
    m = m.lower()
    
    if m == "привет":
        hello = ["hello", "Привет", "Здравствуй"]
        bot.send_message(message.chat.id, choice(hello))
    elif m == "lol":
        bot.send_message(message.chat.id, "kek")
    elif m == "шутка":
        bot.send_message(message.chat.id, "аххахаха")
    else:
         bot.send_message(message.chat.id, "команда не распозана!")

if __name__ == "__main__":
    bot.infinity_polling()
