import requests
from datetime import date, datetime

class TestVenda:

    headers = {'Authorization' : 'Token 271315972f0a63c0039a551b53681ce7747107bd'}

    url_base_vendas = 'http://localhost:8000/api/v1/vendas/'
    url_base_venda = 'http://localhost:8000/api/v1/venda/'
    url_base_unidades = 'http://localhost:8000/api/v1/unidades/'
    url_base_diretorias = 'http://localhost:8000/api/v1/diretorias/'
    url_base_gerentes = 'http://localhost:8000/api/v1/gerentes/'
    url_base_diretores = 'http://localhost:8000/api/v1/diretores/'
    url_base_vendedores = 'http://localhost:8000/api/v1/vendedores/'

    #TESTANDO O GET GERAL
    def test_get_vendas(self):
        resposta = requests.get(url=self.url_base_vendas, headers=self.headers)
        assert resposta.status_code == 200

    def test_get_venda(self):
        resposta = requests.get(url=self.url_base_vendas+"?id=2", headers=self.headers)
        assert resposta.status_code == 200
    
    def test_post_venda(self):
        novaVenda = {
            "data": date.today(),
            "hora": datetime.now().strftime("%H:%M:%S"),
            "valorTotal": 4250,
            "latLong": "-15.601754458320847, -56.09832706558087",
            "roaming": False,
            "unidadeProx": 1,
            "vendedor": 2
        }

        resultado = requests.post(url=self.url_base_vendas,headers=self.headers,data=novaVenda)
        assert resultado.status_code == 201
    
    def test_put_venda(self):
        venda = {
            "data": "2022-12-21",
            "hora": "12:54:23",
            "valorTotal": 4250,
            "latLong": "-15.601754458320847, -56.09832706558087",
            "roaming": False,
            "unidadeProx": 1,
            "vendedor": 2
        }