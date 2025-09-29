# São pacotes/bibliotecas feitas por terceiro, não fazendo parte do conjunt o padrão do python, podendo ser instalado usando o gerenciamento de pacotes pip

# exemplo da biblioteca requests, basicamente contem series de instruções e funções que nos ajudam a fazer requisições HTTP em vários sites de variaveis metodos
# pip install resquests


print("\nImportação e uso de um módulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTPS para {url} retornou o status {response.status_code}")