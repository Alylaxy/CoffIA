import random

class alimento:
    def __init__(self, nome, proteina, carboidrato, energia, colesterol,lipidios, fibra, vit_c, ferro,calcio,sodio,magnesio,potassio,fosforo,zinco,peso,id):
        self.nome = nome
        self.proteina = proteina
        self.carboidrato = carboidrato
        self.energia = energia
        self.colesterol = colesterol
        self.lipidios = lipidios
        self.fibra = fibra
        self.vit_C = vit_c
        self.ferro = ferro
        self.calcio = calcio
        self.sodio = sodio
        self.magnesio = magnesio
        self.potassio = potassio
        self.fosforo = fosforo
        self.zinco = zinco
        self.peso = peso
        self.id = id

class refeicao:
    def __init__(self,alimentos,proteina, carboidrato, energia, colesterol,lipidios, fibra, vit_c, ferro,calcio,sodio,magnesio,potassio,fosforo,zinco,peso):
        self.alimentos = alimentos
        self.proteina = proteina
        self.carboidrato = carboidrato
        self.energia = energia
        self.colesterol = colesterol
        self.lipidios = lipidios
        self.fibra = fibra
        self.vit_C = vit_c
        self.ferro = ferro
        self.calcio = calcio
        self.sodio = sodio
        self.magnesio = magnesio
        self.potassio = potassio
        self.fosforo = fosforo
        self.zinco = zinco
        self.peso = peso

# Função para criar um novo indivíduo
def criar_refeicao():
    refeicao_array = []
    
    for i in range(0,10):
        alimento_id = random.randint(0,10)
        alimento_novo = [x for x in alimento if x.id == alimento.id]
        proteina += alimento_novo[0].proteina
        carboidrato += alimento_novo[0].carboidrato
        energia +=  alimento_novo[0].energia
        colesterol += alimento_novo.colesterol
        lipidios += alimento_novo.lipidios
        fibra += alimento_novo.fibra
        vit_c += alimento_novo.vit_c
        ferro += alimento_novo.ferro
        calcio += alimento_novo.calcio
        sodio += alimento_novo.sodio
        magnesio += alimento_novo.magnesio
        potassio += alimento_novo.potassio
        fosforo += alimento_novo.fosforo
        zinco += alimento_novo.zinco
        peso += alimento_novo.peso
    
    nova_refeicao = refeicao(alimentos,proteina, carboidrato, energia, colesterol,lipidios, fibra, vit_c, ferro,calcio,sodio,magnesio,potassio,fosforo,zinco,peso)
    return refeicao

def criar_populacao():
    array_refeicoes = []
    for i in range(0,500):
        array_refeicoes.append(criar_refeicao())
    
    return array_refeicoes


