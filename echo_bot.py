import os
from flask import Flask, request
import telebot

# Cargar token desde variable de entorno
#TOKEN = os.getenv("TELEGRAM_TOKEN")
#TOKEN = os.getenv("7924004154:AAHr_UcMelDIXbNhH45-rAPZDZjikhgaBmI")
#TOKEN = "7924004154:AAHr_UcMelDIXbNhH45-rAPZDZjikhgaBmI"

TOKEN = os.getenv("TELEGRAM_TOKEN")

# Si TOKEN es None (no definido en entorno), puedes poner el token aquí para pruebas locales
if TOKEN is None:
    TOKEN = "7924004154:AAHr_UcMelDIXbNhH45-rAPZDZjikhgaBmI"  # <- Pon tu token aquí solo para pruebas locales

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Mensajes de comando
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message,
        """
        hola Soy 🤖MINETBOT, Tu asistente virtual 24/7.

        MINET es tu Proveedor de servicios de internet que te brinda tecnología en Fibra Óptica.

        ¿En qué podemos ayudarte?

        /1 - 👨‍🔧​ Soporte técnico / Problemas con el WiFi  
        /2 - 💯 Planes de Servicio de Internet  
        /3 - 📲 Cambiar contraseña del WiFi
        """
    )

@bot.message_handler(commands=["1"])
def soporte(message):
    bot.reply_to(message,
    """
    Soporte técnico / Problemas con el WiFi

    1. Verifica otros dispositivos  
    2. Revisa las luces del módem  
    3. Reinicia el módem/router  
    4. Prueba con un cable Ethernet  
    5. Contacta a soporte: 3213819255
    """)

@bot.message_handler(commands=["2"])
def planes(message):
    bot.reply_to(message,
    """
    Planes de Servicio de Internet

    ⚡ Plan Básico - 100MB x $75.000  
    🔥 Plan Medio - 150MB x $85.000  
    🤩 Plan Avanzado - 200MB x $95.000
    """)

@bot.message_handler(commands=["3"])
def cambiar_contra(message):
    bot.reply_to(message,
    """
    Cambiar contraseña del WiFi:

    (Aquí puedes insertar instrucciones o pedir datos)
    """)

@bot.message_handler(content_types=["text"])
def responder_texto(message):
    if message.text.lower() in ["hola", "hello", "hi"]:
        bot.send_message(message.chat.id, f"Hola {message.from_user.first_name}, ¿en qué puedo ayudarte?")
    else:
        bot.send_message(message.chat.id, "Comando no reconocido. Usa /start para ver el menú.")

# Ruta del webhook para recibir mensajes de Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    json_str = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# Ruta base para comprobar que el servidor está vivo
@app.route("/", methods=["GET"])
def home():
    return "Bot en línea."

# Main
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
