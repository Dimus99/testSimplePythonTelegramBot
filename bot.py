import telebot;
import config
token = config.token
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "hi?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Hi?")
    else:
        bot.send_message(message.from_user.id, message.text)


bot.polling(none_stop=True, interval=0)
