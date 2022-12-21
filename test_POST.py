import requests
from datetime import date, datetime

headers = {'Authorization' : 'Token 271315972f0a63c0039a551b53681ce7747107bd'}

url_base_vendas = 'http://localhost:8000/api/v1/vendas/'


novaVenda = {
    "data": date.today(),
    "hora": datetime.now().strftime("%H:%M:%S"),
    "valorTotal": 4250,
    "latLong": "-15.601754458320847, -56.09832706558087",
    "roaming": False,
    "unidadeProx": 1,
    "vendedor": 2
}

resultado = requests.post(url=url_base_vendas,headers=headers,data=novaVenda)


#TESTANDO O CÓDIGO STATUS HTTP
assert resultado.status_code == 201

print('POST-FUNCIONANDO')