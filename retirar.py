import re

# Definindo a expressão regular para encontrar o padrão "descricao":"Tomate, salada"
pattern = re.compile(r'"slug":"[^"]+"')

# Abrindo o arquivo de entrada para leitura
with open('soup_content.txt', 'r') as entrada:
    # Lendo o conteúdo do arquivo
    conteudo = entrada.read()

# Encontrando todas as ocorrências do padrão
resultados = pattern.findall(conteudo)
print(len(resultados))

# Abrindo o arquivo de saída para escrita
with open('saida.txt', 'w') as saida:
    # Escrevendo as informações extraídas no novo arquivo
    for resultado in resultados:
        saida.write(resultado + '\n')

print("Processo concluído. Informações extraídas gravadas em 'saida.txt'.")

