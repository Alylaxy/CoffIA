import requests
from bs4 import BeautifulSoup
import re

def extrair(url):
    # Enviar uma solicitação HTTP para obter o conteúdo da página
    response = requests.get(url)
    
    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Criar um objeto BeautifulSoup com o conteúdo da página
        resultados = []
        soup = BeautifulSoup(response.content, 'html.parser')
        with open('soup_content.txt', 'w+r', encoding='utf-8') as file:

            file.write(str(soup.prettify()))

        with open('soup_content.txt', 'r') as entrada:
            # Lendo o conteúdo do arquivo
            conteudo = entrada.read()
        # Abre o arquivo de entrada em modo de leitura e o arquivo de saída em modo de escrita
        resultados = pattern.findall(conteudo)
        print(len(resultados))

        with open('soup_content.txt', 'r') as arquivo_entrada, open('links.txt', 'w') as arquivo_saida:
            # Lê todas as linhas do arquivo de entrada e as coloca em uma lista
            for resultado in resultados:
                arquivo_saida.write(resultado + '\n')

            linhas = arquivo_entrada.readlines()
            
            # Cria um conjunto para armazenar as linhas únicas
            linhas_unicas = set(linhas)
            
            # Escreve as linhas únicas no arquivo de saída
            for linha in linhas_unicas:
                arquivo_saida.write(linha)

# Exemplo de uso
if __name__ == "__main__":
    url_produto = f'https://www.tabelatacoonline.com.br/todos-os-alimentos'
    pattern = re.compile(r'"slug":"[^"]+"')
    extrair(url_produto)
