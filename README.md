# README.md — 💧 Telegram-бот «Пей воду»

Простой Telegram-бот на Python, который напоминает пить воду и считает выпитый объём.

## Команды
- `/start` — приветствие и краткая инструкция
- `/setreminder N` — установить интервал напоминаний каждые **N минут**
- `/stop` — остановить напоминания
- `/drank X` — добавить **X мл** воды в статистику
- `/status` — показать прогресс по цели (по умолчанию 2000 мл)

> ⚠️ В текущей версии интервал сохраняется в памяти, но **планировщик напоминаний не запущен**.
> Для автосообщений каждые N минут добавьте планировщик (см. раздел «Автономные напоминания» ниже).

---

## Требования
- Python 3.8+
- Библиотека: `pyTelegramBotAPI`

## Установка
```bash
# 1) создать и активировать виртуальное окружение (по желанию)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) установить зависимости
pip install pyTelegramBotAPI

# 3) создать файл с ботом (например, bot.py) и вставить код из репозитория/примера
Настройка токена
Никогда не храните реальный токен в коде. Вместо этого используйте переменные окружения.

Вариант A — .env (через python-dotenv):


'''
pip install python-dotenv'''
Создайте файл .env:

init

BOT_TOKEN=ваш_токен_из_BotFather
И в коде бота замените:
'''
import os
from dotenv import load_dotenv'''
load_dotenv()
bot_token = os.getenv("BOT_TOKEN")'''
Вариант B — переменная окружения:

# Windows (PowerShell)
setx BOT_TOKEN "ваш_токен"
# macOS/Linux (bash/zsh)
export BOT_TOKEN="ваш_токен"
Запуск

python bot.py
Пример диалога
bash
Копировать
Редактировать
/start
/setreminder 30
/drank 250
/status
/stop
Автономные напоминания (по желанию)
Чтобы бот сам отправлял напоминания каждые N минут (а не просто запоминал число), добавьте планировщик. Самый простой способ — threading.Timer, более надёжный — APScheduler.

Вариант: APScheduler (рекомендуется)
bash
Копировать
Редактировать
pip install APScheduler
Скетч интеграции:

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
# при установке интервала:
# scheduler.add_job(lambda: bot.send_message(chat_id, "Пора сделать глоток 💧"), "interval", minutes=interval_minutes, id=str(chat_id), replace_existing=True)
# при stop:
# scheduler.remove_job(str(chat_id))
scheduler.start()
В продакшене используйте БД (например, SQLite/Redis) для хранения интервалов/прогресса и перезапускайте джобы после рестарта.

Частые проблемы
Unauthorized/401 — неверный или просроченный BOT_TOKEN.

Сообщения не приходят — бот не запущен (нет bot.polling()), бот не начат пользователем (надо нажать «Start»), ваш аккаунт не в чате/канале.

Напоминания не идут — в базовой версии нет планировщика; добавьте APScheduler (см. выше).

Структура (минимальная)
bash
Копировать
Редактировать
project/
├─ bot.py
├─ requirements.txt   # pyTelegramBotAPI[, APScheduler][, python-dotenv]
└─ .env               # BOT_TOKEN=... (не коммитить)
