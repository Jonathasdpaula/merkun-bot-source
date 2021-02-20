import requests


def bin(message):

    try:
        request = requests.get(
            'https://lookup.binlist.net/' + message.text.replace('@merkun_bot', '').replace('/bin ', '')).json()
        band = request.get('scheme')
        tipo = request.get('type')
        pais = request.get('country')
        banco = request.get('bank')
        nivel = request.get('brand')

        return f'''
Bandeira: {band}
Tipo: {tipo}
Nivel: {nivel}
Pais: {pais.get('name')} {pais.get('emoji')}
Banco: {banco.get('name')}'''

    except(ValueError, AttributeError):
        return 'Bin invalida'
