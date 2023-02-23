# pip install pyTelegramBotAPI
import telebot

token = "dfdfsf"
bot  = telebot.TeleBot(token)

questions = ["Столица России?", "Самое большое озеро в мире?", "Самый популрный спорт в мире?"] # Список вопросов
answers = [["Лондон", "Москва", "Париж"],
           ["Каспийское море", "Виктория", "Гурон"],
           ["Гольф", "Хоккей", "Футбол"]] # Список вариантов ответов
right = [2, 1, 3]

money = 0 # Баланс
i = 0 # Счётчик вопросов

@bot.message_handler(content_types=["text"])
def dialog(message):
    global i, money

    user_text = message.text
    if i == 0 or user_text == str(right[i-1]):
        if i != 0:
            money = money + 100
            mess = "Ваш баланс: " + str(money) + "$"
            bot.send_message(message.chat.id, mess)
        if i == 3:
            bot.send_message(message.chat.id, "Игра завершена")
            i = 0
            money = 0
        mess = questions[i] + '\n' + '1: '+ answers[i][0] + '\n' + '2: '+ answers[i][1] +'\n' + '3: '+ answers[i][2] +'\n' +  "Пиши ответ цифрой"
        bot.send_message(message.chat.id, mess)
        i = i + 1
    else:
        bot.send_message(message.chat.id, "Ответ неверный!")


if __name__ == "__main__":
    bot.infinity_polling()
