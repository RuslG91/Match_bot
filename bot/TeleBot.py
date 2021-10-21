import telebot
from Config import match_day, alert, napominalka, match_date
import schedule
import time

#Тело бота
bot = telebot.TeleBot("TOKEN", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['start', 'help', 'match', 'Fmatch', 'Notice'])
def send_welcome(message):
    if message.text == '/start':
        x = message
        bot.send_message(message, f'Привет, я бот который подскажет ближайшие матчи Зенита. Чтобы узнать список команд набери /help')
        print(x)
    elif message.text == '/help':
        n = '\n'	
        bot.reply_to(message, f"Я могу обработать команды :{n}/start - ты увидишь приветствие {n}/help - ты уже читаешь эту комаду {n}/match - ты увидишь даты ближайших матчей Зенита {n}/memory - запомнит тебя и пришлёт сообщение в день игры что Зенит играет")
    elif message.text == '/match':
        bot.reply_to(message, f'{match_day()}')
    elif message.text == '/Fmatch':
        bot.reply_to(message, f'{alert()}')
    elif message.text == '/Notice':
        bot.send_message(message.chat.id, f'Сегоня играет Зенит в {alert()}')

# Отдельный обработчик сообщений для напоминания об игре в день игры. Функция отправка выполняет проверку на истинность даты игры, получая от функции матч дэйт значения тру или фолс, если приходит тру, то выполняется отправка сообщения пользователю, если фолс то ничего не происходит.
@bot.message_handler(commands=['memory'])
def send_notification(message):
    def otpravka():
        match_date()
        true_date = match_date()
        if true_date == True:
            bot.send_message(chat_id, f'{napominalka()}')
        else:
            print('false')
            pass    
    if message.text == '/memory':
        chat_id = message.chat.id
        username = message.from_user.username
        schedule.every().day.at('15:59').do(otpravka) # модуль шедул каждодневно проверяет играет ли сегодня зенит
        bot.send_message(chat_id, f'{username} Я напомню Вам когда состоится матч') 
    while True: # поддержание модуля шедул в рабочем состоянии на постоянной основе
        schedule.run_pending()
        time.sleep(60)        
bot.polling(none_stop=True, interval=0)







