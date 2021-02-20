import telebot
from start_menu import menu
from consultar_ip import ip
from consultar_bin import bin
from consultar_placa import placa
from consultar_cep import cep
from gerar_cpf import gen_cpf
from gerar_cnpj import gen_cnpj
from covid import covid

bot = telebot.TeleBot(
    token='SEU TOKEN AQUI')


@bot.message_handler(commands=['start', 'menu'])
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


@bot.message_handler(commands=['cep'])
def consulta_cep(message):

    bot.reply_to(message, cep(message))


@bot.message_handler(commands=['gerarcpf'])
def gera_cpf(message):

    bot.reply_to(message, gen_cpf(message))


@bot.message_handler(commands=['gerarcnpj'])
def gera_cnpj(message):

    bot.reply_to(message, gen_cnpj(message))


@bot.message_handler(commands=['covid'])
def covidstats(message):

    bot.reply_to(message, covid(message))


if __name__ == '__main__':
    bot.polling(none_stop=True)
