import requests

def covid(message):

    request = requests.get('https://api.covid19api.com/summary' + message.text.replace('/covid', '')).json()
    dados = request.get('Global')
    casos = dados.get('TotalConfirmed')
    mortes = dados.get('TotalDeaths')
    recuperados = dados.get('TotalRecovered')

    return  f'''
Casos: {casos}
Mortes: {mortes}
Recuperados: {recuperados}'''
