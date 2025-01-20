import telebot
from telebot import types

bot = telebot.TeleBot("7802621755:AAHUEipqmBnbzV0rTVRpSnGvsc24sOthPFk")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,f'Hello, {message.from_user.username}! type /openings to learn an opening')

@bot.message_handler(commands=['openings'])
def openings(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Queen's Gambit", callback_data="queens gambit")
    button2 = types.InlineKeyboardButton("King's Gambit", callback_data="kings gambit")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, "What opening do you want to learn?", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "queens gambit":
        bot.send_message(call.message.chat.id, "Queen's Gambit is a nice choise")
    elif call.data == "kings gambit":
        bot.send_message(call.message.chat.id, "King's Gambit is a nice choise")
bot.polling(none_stop=True)
