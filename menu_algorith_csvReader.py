import random
import csv

def get_line_from_csv(line_number):
    line = 0
    with open("alimentos.csv", 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for i, row in enumerate(reader):
            if i == line_number - 1:
                line = row
                break
        line = [float(x.replace(',','.')) for x in line[2:]]
    return line

def gera_refeicao():
    refeicao = [0]*6

    for i in range(random.randint(2, 6)):
        refeicao = [a+b for a,b in zip(get_line_from_csv(random.randint(2, 16)), refeicao)]
    return refeicao
def criar_populacao():
    array_refeicoes = []
    for i in range(500):
        array_refeicoes.append(gera_refeicao())

    return array_refeicoes

def upper_fitness(tester) -> int:
    idosos = [5, 15]
    tabela_do_alimento = [a for a in dir(tester) if not a.startswith("__")]
    death_count = 0
    for i in idosos:
        for limite in i:
            death_count += 1 if tester > limite else 0
    return death_count

def lower_fitness(tester) -> int:
    idoso = [5, 15]
    tabela_do_alimento = [a for a in dir(tester) if not a.startswith("__")]
    death_count = 0
    for i in idoso:
        for limite in i:
            death_count += 1 if tester < limite else 0
    return death_count

def fitness_test(tester):
    death_count = upper_fitness(tester)
    death_count += lower_fitness(tester)


def main():
    populacao = criar_populacao()
    for i in populacao:
        print(i)


if __name__ == "__main__":
    main()