import requests

def ip(message):

     request = requests.get('http://ip-api.com/json/' + message.text.replace('https://', '').replace('http://', '').replace('/ip ', '')).json()

     if 'message' not in request:
        cep = request.get('cep')
        cidade = request.get('city')
        uf = request.get('state')
        vizinhanca = request.get('neighborhood')
        rua = request.get('street')

        return f'''
IP: {request.get('query')}
Pais: {request.get('country')}
Estado: {request.get('regionName')}
Cidade: {request.get('city')}
Provedor: {request.get('isp')}'''
     else:
        return 'CEP invalido'
