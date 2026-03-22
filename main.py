import telebot
from telebot import types
import os
from flask import Flask
from threading import Thread

# 1. Apna Token yahan daalein
API_TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(API_TOKEN)

# 2. Apni Telegram ID yahan daalein (@userinfobot se milegi)
ADMIN_ID = 123456789 

# 3. Apne 18+ Wale Bot ka Link yahan daalein
ADULT_BOT_LINK = "https://t.me/Aapka_Adult_Bot_Username"

app = Flask('')

@app.route('/')
def home():
    return "Bot is Running!"

def run():
    app.run(host='0.0.0.0', port=8080)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('🎬 Movie Store')
    btn2 = types.KeyboardButton('📱 Premium Apps')
    btn3 = types.KeyboardButton('🔞 Adult 18+ (Lock)')
    btn4 = types.KeyboardButton('⚜️ Buy Premium')
    btn5 = types.KeyboardButton('📞 Support')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    bot.send_message(message.chat.id, "Welcome to Super Bot Store! 🚀\n\nMovies, Apps aur exclusive content ke liye niche buttons use karein.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == '🎬 Movie Store':
        bot.send_message(message.chat.id, "📽️ Konsi movie chahiye? Naam likhein.")
    
    elif message.text == '📱 Premium Apps':
        bot.send_message(message.chat.id, "🔥 **Premium Apps List:**\n\n1. Spotify\n2. Canva\n3. PicsArt\n\nDownload ke liye app ka naam likhein.")
        
    elif message.text == '🔞 Adult 18+ (Lock)':
        # Yahan hum user ko doosre bot par bhej rahe hain
        text = f"🔐 **Premium Adult Content Lock Hai!**\n\nIs content ko access karne ke liye niche diye gaye button par click karke hamare 18+ bot par jayein 👇"
        markup = types.InlineKeyboardMarkup()
        btn_link = types.InlineKeyboardButton("Unlock 18+ Content 🔓", url=ADULT_BOT_LINK)
        markup.add(btn_link)
        bot.send_message(message.chat.id, text, reply_markup=markup)

    elif message.text == '⚜️ Buy Premium':
        bot.send_message(message.chat.id, "💎 Premium Subscription ke liye Admin @Aapki_ID ko message karein.")

# Admin ke liye File ID nikalne ka feature
@bot.message_handler(content_types=['document', 'video', 'photo'])
def get_file_id(message):
    if message.from_user.id == ADMIN_ID:
        if message.content_type == 'document':
            f_id = message.document.file_id
        elif message.content_type == 'video':
            f_id = message.video.file_id
        else:
            f_id = message.photo[-1].file_id
        bot.reply_to(message, f"✅ **File ID:** `{f_id}`")

def start_server():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    start_server()
    bot.polling(none_stop=True)
    
