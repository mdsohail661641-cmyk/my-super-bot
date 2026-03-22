import telebot
from telebot import types
from flask import Flask
from threading import Thread

# 1. Aapka Asli Token
API_TOKEN = '8112674013:AAHSNHT4gyyX-yn7bnTrQyZb3CmLuky_wX'
bot = telebot.TeleBot(API_TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Bot is Live!"

def run():
    app.run(host='0.0.0.0', port=8080)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('🎬 Movie Store')
    btn2 = types.KeyboardButton('📱 Premium Apps')
    btn3 = types.KeyboardButton('🔞 Adult 18+ (Lock)')
    btn4 = types.KeyboardButton('⚜️ Buy Premium')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Welcome back! Bot is active 🚀", reply_markup=markup)

def start_server():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    start_server()
    bot.polling(none_stop=True)
    
