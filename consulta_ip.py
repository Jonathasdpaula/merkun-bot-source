import requests

def ip(message):

     request = requests.get('http://ip-api.com/json/' + message.text.replace('https://', '').replace('http://', '').replace('/ip ', '')).json()

     if 'message' not in request:

        return f'''
IP: {request.get('query')}
Pais: {request.get('country')}
Estado: {request.get('regionName')}
Cidade: {request.get('city')}
Provedor: {request.get('isp')}'''
     else:
        return 'IP invalido'
