import telebot

bot_token = '8364997544:AAH5SbYKxg9s_P9tN_W5eHr95j46jlSEGE8'
bot = telebot.TeleBot(bot_token)

interval_minutes = 0
drank = 0
goal = 2000

@bot.message_handler(commands=['start'])
def start(message):
    global interval_minutes, drank
    bot.send_message(message.chat.id,
        "Привет! Я напомню тебе не забывать пить воду!💧\n"
        "Введите /setreminder - напоминания каждые n минут\n"
        "Введите /drank - введите сколько вы выпили воды\n"
        "Введите /status - посмотреть текущий статус\n"
        "Введите /stop - остановить напоминания")

@bot.message_handler(commands=['setreminder'])
def set_reminder(message):
    global interval_minutes
    try:
        interval_minutes = int(message.text.split()[1])
        bot.send_message(message.chat.id, f"Напоминания каждые {interval_minutes} минут установлены.")
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Пожалуйста, укажите число минут. Пример: /setreminder 30")
@bot.message_handler(commands=['stop'])
def stop(message):
    global interval_minutes
    interval_minutes = 0
    bot.send_message(message.chat.id, "Напоминания остановлены.")

@bot.message_handler(commands=['drank'])
def drank_command(message):
    global drank
    parts = message.text.split()
    if len(parts) == 2 and parts[1].isdigit():
        amount = int(parts[1])
        drank += amount
        bot.send_message(message.chat.id, f"Записано: {amount} мл. Всего: {drank} мл.")
    else:
        bot.send_message(message.chat.id, "Используй так: /drank 200")

@bot.message_handler(commands=['status'])
def status(message):
    remaining = max(goal - drank, 0)
    bot.send_message(
        message.chat.id,
        f"💧 Выпито: {drank} мл\n Осталось: {remaining} мл до цели ({goal} мл)"
    )




bot.polling()

