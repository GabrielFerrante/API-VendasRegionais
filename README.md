# API-VendasRegionais
API REST utilizando Django 4 e Django-rest-framework.


Banco de dados SQLite

## Instalação
Clone o repositório e construa o ambiente com o Docker-compose


<code>git clone https://github.com/GabrielFerrante/API-VendasRegionais.git
docker-compose build
docker-compose up
</code>

Este repositório já possui um pequeno banco de dados para teste, que já vai ser lido quando o container for executado.
A API foi testada com testes automatizados com PyTest e com o Software Insomnia (manualmente).


Execute o arquivo na raiz do repositório:

<code>pytest test_pytest.py</code>

## Estrutura do banco de dados

O banco de dados foi construído utilizando os modelos do ORM do Django-framework. 
O código de construção do banco se encontra em: 

./appApiVendas/models.py

Neste arquivo, somente estão as tabelas referentes à regra de negócio. Tabelas de autenticação como de usuários já são implementadas pelo Django.
Portanto, as tabelas criadas foram:

### Diretor
  User do Django - Relação 1-1 </br>
  geral - Boolean (referente a ser o Diretor Geral)
 
### Gerente
  User do Django - Relação 1-1 </br>

### Diretoria
  Nome - String</br>
  Diretor - Relação 1-1
  
### Unidade
  Latitude e Longitude - String</br>
  cidade - String</br>
  Diretoria - Relação 1-N</br>
  Gerente - Relação 1-1
  
### Vendedor
  User do Django - Relação 1-1</br>
  Unidade - Relação 1-N

### Venda
  data - Date</br>
  hora - Time</br>
  Vendedor - Relação 1-N</br>
  valorTotal - Float</br>
  Latitude e Longitude - String</br>
  Unidade mais próxima - Relação 1-N</br>
  roaming - Boolean</br>
  
*observação: Os modelos Diretor, Gerente e Vendedor possuem relação com o modelo de Usuário padrão do Django, dessa forma, facilita a transição de cargo entre os usuários.

*observação: Para visualizar os cadastros, acessar: 127.0.0.0:8000/admin, com o login: admin e senha: 123

## Endpoints/rotas
A API possui autenticação via Token, vinculada com o Usuário. O usuário Admin já possui um Token cadastrado no banco.
O retorno de cada endpoint é em formato Json.

### Métodos GET
  </br>
  Endpoint - 127.0.0.1:8000/api/v1/vendas/ (Retorna todas as vendas)</br>
  ------ Filtros</br>
  ---------- .../v1/vendas/?id=2 (Retorna uma venda específica)</br>
  ---------- .../v1/vendas/?data=2022-12-19 (Retorna as vendas de uma data específica)</br>
  ---------- .../v1/vendas/?hora=00:10:51 (Retorna as vendas de uma hora específica)</br>
  ---------- .../v1/vendas/?CriadoHoraMin=00:10:51&CriadoHoraMax=06:10:23 (Retorna as vendas dentre um intervalo de horas)</br>
  ---------- .../v1/vendas/?CriadoDataMin=2022-12-19&CriadoDataMax=2022-12-22 (Retorna as vendas dentre um intervalo de datas)</br>
  ---------- .../v1/vendas/?latLong=-15.601754458320842, -56.09832706558089(Retorna as vendas com uma latitude e longitude específica)</br>
  ---------- .../v1/vendas/?vendedor=3(Retorna as vendas de um vendedor específico)</br>
  ---------- .../v1/vendas/?unidadeProx=1(Retorna as vendas vinculadas à uma unidade em específico)</br>
  ---------- .../v1/vendas/?roaming=true(Retorna as vendas em roaming)</br>
  ---------- .../v1/vendas/?valorTotal=324.23(Retorna as vendas com o valor especificado)</br>
  </br>
  Endpoint - 127.0.0.1:8000/api/v1/unidades/ (Retorna todas as unidades)</br>
  ------ Filtros</br>
  ---------- .../v1/unidades/?id= </br>
  ---------- .../v1/unidades/?latLong=</br>
  ---------- .../v1/unidades/?cidade=</br>
  ---------- .../v1/unidades/?diretoria=</br>
  ---------- .../v1/unidades/?gerente=</br>
  </br>
  Endpoint - 127.0.0.1:8000/api/v1/diretorias/ (Retorna todas as diretorias)</br>
  ------ Filtros</br>
  ---------- .../v1/diretorias/?id= </br>
  ---------- .../v1/diretorias/?nomeDiretoria= </br>
  ---------- .../v1/diretorias/?diretor= </br>
  </br>
  Endpoint - 127.0.0.1:8000/api/v1/gerentes/ (Retorna todos os gerentes)</br>
  ------ Filtros</br>
  ---------- .../v1/gerentes/?id= </br>
  </br>
  Endpoint - 127.0.0.1:8000/api/v1/diretores/ (Retorna todos os diretores)</br>
  ------ Filtros</br>
  ---------- .../v1/diretores/?id= </br>
  ---------- .../v1/diretores/?geral= </br>
   </br>
  Endpoint - 127.0.0.1:8000/api/v1/vendedores/ (Retorna todos os vendedores)</br>
  ------ Filtros</br>
  ---------- .../v1/vendedores/?id= </br>
  ---------- .../v1/vendedores/?unidade= </br>
  
### Métodos POST
  </br>
  Endpoint - 127.0.0.1:8000/api/v1/venda/ (Realiza o cadastro de uma venda)</br>
  **Consultar os demais endpoints para consultar o ID de vendedores e unidades para realizar o cadastro</br>
  Exemplo de POST com Python:
  
    import requests
    headers = {'Authorization' : 'Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}
    def test_post_venda(self):
  
          novaVenda = { 
              "data": date.today(), 
              "hora": datetime.now().strftime("%H:%M:%S"), 
              "valorTotal": 4250, 
              "latLong": "-23.0392039, -70.232134", 
              "roaming": False, 
              "unidadeProx": 4, 
              "vendedor": 2 
          }

          resultado = requests.post(url='http://localhost:8000/api/v1/venda/',headers=headers,data=novaVenda)
          assert resultado.status_code == 201`
          
          
### Métodos PUT
  </br>
  Endpoint - 127.0.0.1:8000/api/v1/venda/ (Realiza a atualização de uma venda, basta informar o ID da venda)</br>
  Exemplo de PUT com Python:
  
  
    import requests
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
        
        resultado = requests.put(url=http://localhost:8000/api/v1/venda/+"21/",headers=headers,data=venda)
        assert resultado.status_code == 201
