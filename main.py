import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot("6886020079:AAErZlJ2fWBOFCEPCLEljsqCLpHJVmqz3tg")

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.reply_to(message, "Привет! Я чат бот, который будет напоминать тебе пить воду и принимать витамины!")
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()
    vitamins_reminder_thread = threading.Thread(target=send_reminders1, args=(message.chat.id,))
    vitamins_reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = ["**Человеческое тело теряет в среднем около 2,5 литра воды в день через пот, дыхание и выделения**", "**Вода расширяется при замерзании, что является уникальным свойством и играет ключевую роль в природных процессах, таких как эрозия скал**", "**Пресная вода составляет всего около 2,5% от всего объема воды на Земле, и большая ее часть заморожена в ледниках и ледяных шапках**"]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о воде {random_fact}')

@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = """Список доступных команд:
/start - Запустить бота и начать получать напоминания о питье воды и приеме витаминов.
/fact - Получить случайный факт о воде.
/help - Получить список доступных команд и описание.

Помните, что забота о своем теле - это важно. Пейте воду и не забывайте о витаминах!
"""
    bot.reply_to(message, help_text)

def send_reminders(chat_id):
    first_rem = "09:00"
    second_rem = "15:00"
    end_rem = "20:34"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)
        time.sleep(1)

def send_reminders1(chat_id):
    first_rem = "09:10"
    end_rem = "20:35"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - прими витамины")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)