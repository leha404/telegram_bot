import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
my_key = os.getenv('TELEGRAM_API_KEY')
bot = telebot.TeleBot(my_key)

print('Start bot...')

# KeyboardInit
keyboard = types.InlineKeyboardMarkup()

key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
keyboard.add(key_yes)

key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
keyboard.add(key_no)

@bot.message_handler(content_types=['text'])
def start(message):    
    if message.text == "/start":
        bot.send_message(message.chat.id, "Привет. Я тестовый бот leha_404. Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.chat.id, "Ой, привет) Я еще в разработке и не понимаю команд) Попробуй написать /start")

def get_name(message):
    name = message.text
    question = 'Тебя зовут ' + name + '?'
    bot.send_message(message.chat.id, text=question, reply_markup=keyboard)
    bot.register_callback_query_handler(message, callback_worker)

# If no decorator - will register new functions (bad)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(callback_query):
    message = callback_query.message
    if callback_query.data == "yes":
        bot.send_message(message.chat.id, 'Окей, записали :)')
    if callback_query.data == "no":
        bot.send_message(message.chat.id, 'Невнимательного человека ответ :O')

bot.polling(none_stop=True, interval=0)