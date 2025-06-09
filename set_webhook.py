import os
import telebot

TOKEN = os.getenv("TELEGRAMTOKEN")
if not TOKEN:
    print("Error: No se encontró la variable de entorno TELEGRAM_TOKEN")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Quita cualquier webhook anterior
bot.remove_webhook()

# Pon el webhook apuntando a tu URL (cámbiala por la de tu app)
url = f"https://minetbot.onrender.com/{TOKEN}"

resultado = bot.set_webhook(url=url)
if resultado:
    print(f"Webhook configurado correctamente en: {url}")
else:
    print("Error al configurar el webhook")
