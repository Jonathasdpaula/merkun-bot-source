import requests

def cep(message):

     request = requests.get('https://brasilapi.com.br/api/cep/v1/' + message.text.replace('/cep ', '')).json()

     if 'message' not in request:

        return f'''
CEP: {cep}
Município: {cidade} - {uf}
Vizinhança: {vizinhanca}
Rua: {rua}'''

     else:
        return 'CEP invalido'
