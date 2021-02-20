import requests


def cep(message):

    request = requests.get('https://brasilapi.com.br/api/cep/v1/' +
                           message.text.replace('/cep ', '')).json()

    if 'message' not in request:
        cep = request.get('cep')
        cidade = request.get('city')
        uf = request.get('state')                                                        vizinhanca = request.get('neighborhood')
        rua = request.get('street')

        return f'''
CEP: {cep}
Município: {cidade} - {uf}
Vizinhança: {vizinhanca}
Rua: {rua}'''

    else:
        return 'CEP invalido'
