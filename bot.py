#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import coin
API_TOKEN = '5095857991:AAGbQhcB2mvELKlT2LhZ-OnBPXje5QNwTZY'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """\
# Hi there, I am EchoBot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am coin bot.
I am here to give you the coin price as you wish!
if you want to start enter : /coin \
""")

@bot.message_handler(commands=['coin'])
def send_welcome(message):
    bot.reply_to(message ,"tamam bahar azadi"+coin.get_coin())

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    te=coin.get_coin()
    bot.reply_to(message, coin.text)

bot.infinity_polling()
