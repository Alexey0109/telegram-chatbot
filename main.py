import telebot

#TOKEN = '959976424:AAHQ7FxDWp9kCiRJjCwoj4EOnMQTwDshOsU'
TOKEN = '966351011:AAGDUmgrpOfujpT5flyRlOn26Li-_U8f7Dg'
MESSAGES = {}
TEXT = None
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['add'])
def add_message(message):
    bot.send_message(message.chat.id, 'Enter message: ')
    bot.register_next_step_handler(message, set_incoming)
def set_incoming(message):
    global TEXT
    text = message.text
    TEXT = text
    bot.send_message(message.chat.id, 'Enter reply: ')
    bot.register_next_step_handler(message, set_reply)
def set_reply(message):
    global MESSAGES, TEXT
    MESSAGES[TEXT] = message.text
    bot.send_message(message.chat.id, 'Success! ')

@bot.message_handler(content_types=['text'])
def incoming_message(message):
    global MESSAGES
    try:
        text = MESSAGES[message.text]
        print(text)
        bot.send_message(message.chat.id, text)
    except Exception as e:
        print(e)

bot.polling()