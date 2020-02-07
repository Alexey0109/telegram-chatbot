import telebot

token = "959976424:AAHQ7FxDWp9kCiRJjCwoj4EOnMQTwDshOsU"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    print('Starting!')
    bot.send_message(message.chat.id, 'Hello! I am a chatbot and you can teach me some new words!')
@bot.message_handler(commands=['stop'])
def stop(message):
    print('Stopping!')
    bot.send_message(message.chat.id,"Bye :D")
    exit(0)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"Hello! I am a chatbot and you can teach me some new words!\nHere my commands::\n/add_message - add message pattern to DB\n\nIf I know rude words - text @KeyboardDestroyer")
    
@bot.message_handler(commands=['add_message'])
def add_message(message):
    print('Adding message')
    bot.send_message(message.chat.id, "Введи текст: ")
    bot.register_next_step_handler(message, register_message)
    
def add_reply(message):
    bot.send_message(message.chat.id, "Send message text: ")
    bot.register_next_step_handler(message, register_reply)
def register_message(message):
    print(message.text)
    bot.send_message(message.chat.id, "Send reply text: ")
    print("Writing message...")
    msgfile = open('messages.txt', 'a')
    msgfile.write(str(message.text) + '\n')
    msgfile.close()
    bot.register_next_step_handler(message, register_reply)
def register_reply(message):
    print(message.text)
    bot.send_message(message.chat.id, "Writing... ")
    replyfile = open('replytext.txt', 'a')
    replyfile.write(str(message.text) + '\n')
    replyfile.close()
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text, end='; ')
    msgfile = open('messages.txt', 'r')
    reply = open('replytext.txt', 'r')
    num = 0
    for num, line in enumerate(msgfile, 1):
        if message.text.lower() in line.lower():
            reply = open('replytext.txt', 'r')
            r = ''
            for j in range(num):
                r = reply.readline()
            bot.send_message(message.chat.id, r)
            print(r)
            reply.close()
    msgfile.close()
    #if message.text.lower() == 'hello':
    #    bot.send_message(message.chat.id, 'Hello there!')


bot.polling()