import telebot
import requests
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes 
from telegram import Update

# Вставь свои ключи здесь
TELEGRAM_TOKEN = '7946709623:AAF7KPXX9MwZ8BePd-fZpYJR_vuFurD5UlU'
WEATHER_API_KEY = '1477f2b93f4a429a89a22410252404'

# Функция для получения погоды
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return "Город не найден!"
    weather = response["weather"][0]["description"]
    temp = response["main"]["temp"]
    return f"Погода в {city}: {weather}, температура: {temp}°C"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /weather <город>, чтобы узнать погоду.")

# Команда /weather
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Пожалуйста, укажи город после команды.")
        return
    city = " ".join(context.args)
    weather_info = get_weather(city)
    await update.message.reply_text(weather_info)

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", weather))

    app.run_polling()