import telebot
import os
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Load environment variables
load_dotenv()

# Your Telegram Bot API Token
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    call_button = InlineKeyboardButton("Call Now", url="https://<username>.github.io/Twilio-Telegram-Bot-Website/")
    markup.add(call_button)
    
    bot.reply_to(message, "Welcome! Press the button to make a call.", reply_markup=markup)

# Echo handler
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Polling for new messages
bot.polling()
