import requests                                         
def placa(message):

    message = message.text.replace('/placa ', '').replace('-', '')


    try:
        request = requests.get(f'http://api.masterplaca.devplank.com/v2/placa/{message}/json').json()
        modelo = request.get('modelo')
        marca = request.get('marca')
        ano = request.get('ano')
        anoModelo = request.get('anoModelo')
        chassi = request.get('chassi')
        cor = request.get('cor')
        situacao = request.get('situacao')
        cidade = request.get('municipio')
        uf = request.get('uf')

        return f'''
Placa: {message.upper()}
Modelo: {modelo.title()}
Marca: {marca}
Ano: {ano}/{anoModelo}
Cor: {cor}
Situacao: {situacao}
Municipio: {cidade.title()}-{uf}
Chassi: {chassi}'''

    except(ValueError, AttributeError):
        return 'Placa invalida'
