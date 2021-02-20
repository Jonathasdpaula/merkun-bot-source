import requests


def gen_cnpj(message):

    request = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=SEU TOKEN AQUI' +
                           message.text.replace('/gerarcnpj', '')).json()
    dados = request.get('data')
    numero = dados.get('number_formatted')

    return f'''
CNPJ: {numero}'''
