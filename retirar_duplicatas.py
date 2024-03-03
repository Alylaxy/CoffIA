# Abre o arquivo de entrada em modo de leitura e o arquivo de saída em modo de escrita
with open('saida.txt', 'r') as arquivo_entrada, open('saida2.txt', 'w') as arquivo_saida:
    # Lê todas as linhas do arquivo de entrada e as coloca em uma lista
    linhas = arquivo_entrada.readlines()
    
    # Cria um conjunto para armazenar as linhas únicas
    linhas_unicas = set(linhas)
    
    # Escreve as linhas únicas no arquivo de saída
    for linha in linhas_unicas:
        arquivo_saida.write(linha)
