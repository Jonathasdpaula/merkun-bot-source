import requests


def gen_cpf(message):

    request = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=SEU TOKEN AQUI' +
                           message.text.replace('@merkun_bot', '').replace('/gerarcpf', '')).json()
    dados = request.get('data')
    numero = dados.get('number_formatted')

    return f'''
CPF: {numero}'''
