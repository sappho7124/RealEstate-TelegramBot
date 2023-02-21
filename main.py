import telebot
from telebot import types

def get_token(token_file='token.txt'):
	with open('Data/token.txt') as f:
		token = f.read()
	f.close()
	return token

bot = telebot.TeleBot(get_token(), parse_mode=None)
bot.infinity_polling()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	#print(message.from_user.first_name)
	msg = "Hola " + str(message.from_user.first_name) + ", puedes usar /help para ver la lista de comandos disponibles"
	bot.reply_to(message, msg)

@bot.message_handler(commands=['stop'])
def send_welcome(message):
	#print(message.from_user.first_name)
	msg = "Stop"
	bot.reply_to(message, msg)
	bot.stop_polling()


