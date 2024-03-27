import numpy as np
import random
import csv

def get_line_from_csv(line_number):
    with open("alimentos.csv", 'r') as file:
        line = list(csv.reader(file, delimiter=";"))[line_number - 1]
        return [float(x.replace(',','.')) for x in line[2:len(line)-3]]

def gera_refeicao():
    return [sum(x) for x in zip(*[get_line_from_csv(random.randint(2, 581)) for _ in range(random.randint(2, 6))])]

def criar_populacao(N):
    return [gera_refeicao() for _ in range(N)]

def seleção(população, death_count, k=3):
    seleção = np.random.choice(len(população), k)
    return população[np.argmin(death_count[seleção])]

def crossover(parente1,parente2):
    filho1 = []
    filho2 = []
    stop = len(parente1)
    cont = 0
    while cont < stop:
        if bool(random.getrandbits(1)):
            filho1.append(parente1[cont])
            filho2.append(parente2[cont])
        else:
            filho1.append(parente2[cont])
            filho2.append(parente1[cont])
        cont = cont + 1
    return filho1, filho2

def upper_fitness(tester) -> int:
    men_nutritional_values_upper = [
        600,  # Calories upper bound
        30,  # Protein upper bound
        60,  # Carbohydrates upper bound
        600,  # Energy (no upper bound)
        77,  # Cholesterol upper bound
        77,  # Lipids (Fats) upper bound
        25,  # Fiber upper bound
        90,  # Vitamin C upper bound
        18,  # Iron upper bound
        1200,  # Calcium upper bound
        2300,  # Sodium upper bound
        420,  # Magnesium upper bound
        4700,  # Potassium upper bound
        5,  # Manganese upper bound
        1250,  # Phosphorus upper bound
        2,  # Copper upper bound
        11,  # Zinc upper bound
        900,  # Retinol (Vitamin A) upper bound
        1.2,  # Thiamine (Vitamin B1) upper bound
        1.3,  # Riboflavin (Vitamin B2) upper bound
        1.7,  # Pyridoxine (Vitamin B6) upper bound
        16  # Niacin (Vitamin B3) upper bound
    ]
    women_nutritional_values_upper = [
        600,  # Calories upper bound
        30,  # Protein upper bound
        60,  # Carbohydrates upper bound
        600,  # Energy (no upper bound)
        77,  # Cholesterol upper bound
        77,  # Lipids (Fats) upper bound
        25,  # Fiber upper bound
        90,  # Vitamin C upper bound
        18,  # Iron upper bound
        1200,  # Calcium upper bound
        2300,  # Sodium upper bound
        320,  # Magnesium upper bound
        4700,  # Potassium upper bound
        5,  # Manganese upper bound
        1250,  # Phosphorus upper bound
        2,  # Copper upper bound
        9,  # Zinc upper bound
        700,  # Retinol (Vitamin A) upper bound
        1.1,  # Thiamine (Vitamin B1) upper bound
        1.1,  # Riboflavin (Vitamin B2) upper bound
        1.5,  # Pyridoxine (Vitamin B6) upper bound
        16  # Niacin (Vitamin B3) upper bound
    ]

    death_count = 0
    for test_value,upper_bound in zip(tester, women_nutritional_values_upper):
        death_count += 1 if test_value > upper_bound else 0

    for test_value, upper_bound in zip(tester, men_nutritional_values_upper):
        death_count += 1 if test_value > upper_bound else 0

    return death_count

def lower_fitness(tester) -> int:
    women_nutritional_values_lower = [
        400,  # Calories lower bound
        20,  # Protein lower bound
        45,  # Carbohydrates lower bound
        400,  # Energy (no lower bound)
        44,  # Cholesterol lower bound
        44,  # Lipids (Fats) lower bound
        25,  # Fiber lower bound
        90,  # Vitamin C lower bound
        8,  # Iron lower bound
        1000,  # Calcium lower bound
        2300,  # Sodium lower bound
        270,  # Magnesium lower bound
        3500,  # Potassium lower bound
        2,  # Manganese lower bound
        700,  # Phosphorus lower bound
        0.9,  # Copper lower bound
        8,  # Zinc lower bound
        600,  # Retinol (Vitamin A) lower bound
        0.8,  # Thiamine (Vitamin B1) lower bound
        0.8,  # Riboflavin (Vitamin B2) lower bound
        1.3,  # Pyridoxine (Vitamin B6) lower bound
        14  # Niacin (Vitamin B3) lower bound
    ]
    men_nutritional_values_lower = [
        400,  # Calories lower bound
        20,  # Protein lower bound
        45,  # Carbohydrates lower bound
        400,  # Energy (no lower bound)
        44,  # Cholesterol lower bound
        44,  # Lipids (Fats) lower bound
        25,  # Fiber lower bound
        90,  # Vitamin C lower bound
        8,  # Iron lower bound
        1000,  # Calcium lower bound
        2300,  # Sodium lower bound
        320,  # Magnesium lower bound
        3500,  # Potassium lower bound
        2,  # Manganese lower bound
        700,  # Phosphorus lower bound
        0.9,  # Copper lower bound
        8,  # Zinc lower bound
        700,  # Retinol (Vitamin A) lower bound
        1.1,  # Thiamine (Vitamin B1) lower bound
        1.1,  # Riboflavin (Vitamin B2) lower bound
        1.3,  # Pyridoxine (Vitamin B6) lower bound
        14  # Niacin (Vitamin B3) lower bound
    ]
    death_count = 0
    for test_value, lower_bound in zip(tester, women_nutritional_values_lower):
        death_count += 1 if test_value < lower_bound else 0

    for test_value, lower_bound in zip(tester, men_nutritional_values_lower):
        death_count += 1 if test_value < lower_bound else 0

    return death_count

def fitness_test(tester) -> int:
    return upper_fitness(tester) + lower_fitness(tester)

def mutacao(populacao, frequencia, amplitude):
    mutantes = []
    for individuo in populacao:
        if random.random() <= frequencia:
            mutante = []
            for val in individuo:
                if random.random() <= frequencia:
                    mutante.append(val * (1 + (((random.random() * 2) - 1) * amplitude)))
                else:
                    mutante.append(val)

            mutantes.append(mutante) 
        else:
            mutantes.append(individuo)
    return mutantes

def main():
    N_população = int(input("Digite o numero de população:"))
    geração = int(input("Digite o numero de gerações:"))
    frequencia = float(input("Digite a frequencia de mutaçao (0 a 1):"))
    populacao = criar_populacao(N_população)
    
    for _ in range(geração):
        print(_)
        nova_população =[]
        for _ in range(N_população):
            death_count =np.array([fitness_test(i) for i in populacao])
            parente1=seleção(populacao,death_count)
            parente2=seleção(populacao,death_count)
            
            filho1, filho2 = crossover(parente1,parente2)
            print(filho1)
            print(filho2)
            nova_população.append(filho1)
            nova_população.append(filho2)
        populacao = mutacao(nova_população, frequencia, 0.1)

if __name__ == "__main__":
    main()
