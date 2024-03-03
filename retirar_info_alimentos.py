import csv
import requests
from bs4 import BeautifulSoup

def extrair(url, linha):
    # Enviar uma solicitação HTTP para obter o conteúdo da página
    response = requests.get(url)
    
    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        print(response.status_code)
        # Criar um objeto BeautifulSoup com o conteúdo da página
        soup = BeautifulSoup(response.content, 'html.parser')
        nome = soup.find("h1", class_="text-lg md:text-xl lg:text-2xl")
        tabela = soup.find("div", class_="grid gap-6 lg:gap-8 grid-cols-2 md:grid-cols-4 lg:grid-cols-5")
        valores = tabela.find_all("p", class_="text-sm")
        teste = tabela.find_all("p", class_="text-zinc-500")
        caracteristicas = []
        caracteristicas.append(["nome:", nome.text])
        caracteristicas.append(["id:", linha])
        for i in range(0, len(valores), 2): # Aumenta i de 2 em 2
            if ':' in valores[i].text:
                caracteristicas.append([valores[i].text, valores[i+1].text])
        return caracteristicas

def criar_csv(total):
    with open('alimentos.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Crie um objeto writer
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        # Escreva os dados no arquivo CSV
        for row in total:
            writer.writerow(row)

# Exemplo de uso
if __name__ == "__main__":
    with open('links.txt', 'r') as arquivo:
    # Lendo todas as linhas do arquivo e armazenando-as em uma lista
        links = [link.strip() for link in arquivo]
    total = [] 
    for i, link in enumerate(links):
        print(link)
        print(i)
        url_produto = f'https://www.tabelatacoonline.com.br/{link}'
        parte = extrair(url_produto, i)
        total.append(parte)
    criar_csv(total)