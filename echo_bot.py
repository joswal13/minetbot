import os
from flask import Flask, request
import telebot 

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Asegúrate que esta variable está en Render
print(f"Token leído: {TOKEN!r}")  # Imprime el token entre comillas para detectar espacios o None

if TOKEN is None:
    print("ERROR: La variable de entorno TELEGRAM_TOKEN no está definida.")
    exit(1)
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    print(f"Recibido /start de {message.from_user.id}")
    bot.reply_to(message, "Hola, soy tu bot!")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    try:
        json_str = request.get_data().decode("utf-8")
        print(f"Payload recibido:\n{json_str}")  # 👈 Agrega esto
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return "OK", 200
    except Exception as e:
        print(f"Error procesando update: {e}")
        return "Error", 500

@app.route("/", methods=["GET"])
def home():
    return "Bot online"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Iniciando servidor en puerto {port}")
    app.run(host="0.0.0.0", port=port)
