import telebot
from telebot import types
from flask import Flask
from threading import Thread
import os

# 1. Web Server (Bot ko Render/Replit par zinda rakhne ke liye)
app = Flask('')

@app.route('/')
def home():
    return "SOHAIL Creations Bot is Online!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Bot Setup (Aapka Token)
API_TOKEN = '8512674013:AAGshcht4gXyX-yn7bmArQyzb3CmkuAy_yA'
bot = telebot.TeleBot(API_TOKEN)

# 3. Welcome Message with Buttons
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn1 = types.InlineKeyboardButton("🎬 Movie Store", callback_data='movies')
    btn2 = types.InlineKeyboardButton("📥 Video Downloader", callback_data='download')
    btn3 = types.InlineKeyboardButton("⚜️ Buy Premium ⚜️", callback_data='premium')
    btn4 = types.InlineKeyboardButton("📜 Rules", callback_data='rules')
    
    markup.add(btn1, btn2, btn3, btn4)
    
    welcome_text = (
        f"👋 Welcome **{message.from_user.first_name}**!\n\n"
        "Aapka swagat hai SOHAIL Creations mein. Main ek advanced bot hoon.\n\n"
        "Neeche diye gaye buttons use karein:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

# 4. Button Actions (Callback Handling)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "rules":
        bot.send_message(call.message.chat.id, "📜 **Rules:**\n1. Spam mat karo.\n2. Payment proof @mdsohail661641 ko bhejein.")
        
    elif call.data == "premium":
        payment_text = (
            "⚜️ **PREMIUM MEMBERSHIP** ⚜️\n\n"
            "✅ Super Fast Downloads\n"
            "✅ No Ads / Unlimited Movies\n\n"
            "💰 **Price:** ₹99/month\n\n"
            "👇 Payment ke baad proof yahan bhejein:"
        )
        markup = types.InlineKeyboardMarkup()
        proof_btn = types.InlineKeyboardButton("📸 Send Proof to Admin", url="https://t.me/mdsohail661641")
        markup.add(proof_btn)
        bot.send_message(call.message.chat.id, payment_text, reply_markup=markup, parse_mode='Markdown')

    elif call.data == "download":
        bot.send_message(call.message.chat.id, "📥 **Downloader Mode:**\n\nBas Instagram Reels ya YouTube link paste karein, bot video process karega.")

    elif call.data == "movies":
        bot.send_message(call.message.chat.id, "🎬 **Movie Store:**\n\nMujhe koi bhi movie file bhejein, main aapko uski ID de dunga save karne ke liye.")

# 5. File ID Extraction (For Movie Store)
@bot.message_handler(content_types=['video', 'document', 'photo'])
def handle_files(message):
    file_id = ""
    if message.video: file_id = message.video.file_id
    elif message.document: file_id = message.document.file_id
    elif message.photo: file_id = message.photo[-1].file_id
    
    bot.reply_to(message, f"✅ **File Received!**\n\n**File ID:** `{file_id}`")

# 6. Run Everything
print("⚡ Super-Bot is starting...")
if __name__ == "__main__":
    keep_alive() # Starts the web server
    bot.infinity_polling()
