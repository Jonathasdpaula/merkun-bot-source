import requests

def cep(message):

    try:
        request = requests.get('https://brasilapi.com.br/api/cep/v1/' + message.text.replace('/cep ', '')).json()
        cep = message.text.replace('/cep ', '')
        cidade = request.get('city')
        uf = request.get('state')
        vizinhanca = request.get('neighborhood')
        rua = request.get('street')

        return f'''
CEP: {cep}
Município: {cidade} - {uf}
Vizinhança: {vizinhanca}
Rua: {rua}'''

    except(ValueError, AttributeError):
        return 'CEP invalido'
