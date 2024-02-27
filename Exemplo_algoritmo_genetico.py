import random

# Função de fitness
def fitness(individuo):
    return sum(individuo)

# Função para criar um novo indivíduo
def criar_individuo(tamanho):
    return [random.randint(0,  1) for _ in range(tamanho)]

# Função para cruzar dois indivíduos
def cruzar(parente1, parente2):
    pos = random.randint(0, len(parente1))
    filho1 = parente1[:pos] + parente2[pos:]
    filho2 = parente2[:pos] + parente1[pos:]
    return filho1, filho2

# Função para mutar um indivíduo
def mutate(individuo, chance_mutacao):
    for i in range(len(individuo)):
        if random.random() < chance_mutacao:

            individuo[i] =  1 if individuo[i] ==  0 else  0
    return individuo

# Algoritmo genético
def algoritmo_genetico(populacao_tamanho, individuo_tamanho, geracaos, chance_mutacao):
    # Inicializa a população
    populacao = [criar_individuo(individuo_tamanho) for _ in range(populacao_tamanho)]

    for geracao in range(geracaos):
        # Calcula a aptidão da população
        fitnesses = [fitness(individuo) for individuo in populacao]

        # Seleciona os pais para reprodução
        parentes = random.choices(populacao, weights=fitnesses, k=2)

        # Cria os filhos através de cruzar
        filho1, filho2 = cruzar(*parentes)

        # Muta os filhos
        filho1 = mutate(filho1, chance_mutacao)
        filho2 = mutate(filho2, chance_mutacao)

        # Substitui um dos pais pela cópia do filho
        populacao[random.randint(0, populacao_tamanho -  1)] = filho1
        populacao[random.randint(0, populacao_tamanho -  1)] = filho2

    # Retorna o melhor indivíduo da última geração
    print(len(populacao))
    return max(populacao, key=fitness)

# Executa o algoritmo genético
melhor_individuo = algoritmo_genetico(1000,  15,  1000,  0.0001)
print("Melhor indivíduo encontrado: ", melhor_individuo)
print("Fitness do melhor indivíduo: ", fitness(melhor_individuo))
