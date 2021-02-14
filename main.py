import telebot                     
from start_menu import menu
from consulta_ip import ip
from consulta_bin import bin
from consulta_placa import placa

bot = telebot.TeleBot(
    token='SEU TOKEN AQUI')


@bot.message_handler(commands=['start'])
def startmenu(message):

    bot.reply_to(message, menu())


@bot.message_handler(commands=['ip'])
def consulta_ip(message):

    bot.reply_to(message, ip(message))


@bot.message_handler(commands=['bin'])
def consulta_bin(message):

    bot.reply_to(message, bin(message))



@bot.message_handler(commands=['placa'])
def consulta_placa(message):

    bot.reply_to(message, placa(message))


if __name__ == '__main__':

    bot.polling(none_stop=True)
