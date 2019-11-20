import telebot


bot = telebot.TeleBot()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я чат-бот. Пока я глупенький, но я еще учусь ^^')
@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id,"Пока! Жду тебя снова ^^")
    exit(0)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"Приветик! Я чат-бот которого обучает комьюнити!\nВот мои команды:\n/add_message - добавить сообщение в базу\n\nЕсли я отвечаю грубо или плохо - напишите @KeyboardDestroyer")
    
@bot.message_handler(commands=['add_message'])
def add_message(message):
    bot.send_message(message.chat.id, "Введи текст: ")
    bot.register_next_step_handler(message, register_message)
    
def add_reply(message):
    bot.send_message(message.chat.id, "Введи текст: ")
    bot.register_next_step_handler(message, register_reply)
def register_message(message):
    bot.send_message(message.chat.id, "Теперь введи ответ: ")
    print("Writing message...")
    msgfile = open('messages.txt', 'a')
    msgfile.write(str(message.text) + '\n')
    msgfile.close()
    bot.register_next_step_handler(message, register_reply)
def register_reply(message):
    bot.send_message(message.chat.id, "Регистрация нового паттерна... ")
    replyfile = open('replytext.txt', 'a')
    replyfile.write(str(message.text) + '\n')
    replyfile.close()
    
@bot.message_handler(content_types=['text'])
def send_text(message):
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
            reply.close()
    msgfile.close()
    #if message.text.lower() == 'hello':
    #    bot.send_message(message.chat.id, 'Hello there!')


bot.polling()