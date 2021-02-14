import requests


def ip(message):

    message = message.text.replace(
        'https://', '').replace('http://', '').replace('/ip ', '')
    if len(message) < 4:
        return 'IP invalido'

    else:
        request = requests.get('http://ip-api.com/json/' + message).json()

        return f'''
IP: {request.get('query')}
Pais: {request.get('country')}
Estado: {request.get('regionName')}
Cidade: {request.get('city')}
Provedor: {request.get('isp')}'''
