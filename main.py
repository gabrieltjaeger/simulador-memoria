# Simulador de Substituição de Páginas na Memória
from collections import OrderedDict
from operator import index
from re import M, T


class Memoria:
    def __init__(self, numero_molduras):
        self.numero_molduras = numero_molduras
        self.molduras = []
    
    def cheia(self):
        return len(self.molduras) == self.numero_molduras

    def __str__(self):
        return str(self.molduras)

    def __repr__(self):
        return str(self.molduras)

    def __contains__(self, pagina):
        return pagina in self.molduras

    def __getitem__(self, index):
        return self.molduras[index]

    def __setitem__(self, index, pagina):
        self.molduras[index] = pagina

    def append(self, pagina):
        self.molduras.append(pagina)

    def pop(self, index=-1):
        return self.molduras.pop(index)

    def index(self, pagina):
        return self.molduras.index(pagina)
        
        

def fifo(numero_molduras, numero_paginas, sequencia_de_acesso):
    molduras = Memoria(numero_molduras)
    cont = 0
    while len(sequencia_de_acesso) > 0:
        pagina = sequencia_de_acesso.pop(0)
        if pagina in molduras:
            continue
        if pagina not in molduras:
            if molduras.cheia():
                molduras.pop(0)
            molduras.append(pagina)
            cont += 1
    return cont

def mru(numero_molduras, numero_paginas, sequencia_de_acesso):
    molduras = {}
    cont = 0
    tempo = -1
    while len(sequencia_de_acesso) > 0:
        tempo += 1
        pagina = sequencia_de_acesso.pop(0)
        if pagina not in molduras.keys():
            if not (len(molduras) == numero_molduras):
                molduras[pagina] = tempo
            else:
                molduras.pop(min(molduras, key=molduras.get))
                molduras[pagina] = tempo
            cont += 1
        else:
            molduras[pagina] = tempo
    return cont

def nuf(numero_molduras, numero_paginas, sequencia_de_acesso):
    molduras = {}
    cont = 0
    while len(sequencia_de_acesso) > 0:
        pagina = sequencia_de_acesso.pop(0)
        if pagina not in molduras.keys():
            if not (len(molduras) == numero_molduras):
                molduras[pagina] = 0
            else:
                molduras = OrderedDict(sorted(molduras.items()))
                minimo = min(molduras, key=molduras.get)
                molduras.pop(minimo)
                molduras[pagina] = 0
            cont += 1
        else:
            molduras[pagina] += 1
    return cont

def otimo(numero_molduras, numero_paginas, sequencia_de_acesso):
    return 0

def menor_resultado(resultados):
    return min(resultados, key=resultados.get)
   

def main():
    # nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
    # with open(f'arquivos/entrada/{nome_arquivo_entrada}', 'r') as arquivo:
    with open('arquivos/entrada/inMemoria', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            linha = linha.split('|')
            numero_molduras = int(linha[0])
            numero_paginas = int(linha[1])
            sequencia_de_acesso = linha[2].split(' ')
            sequencia_de_acesso = [int(i) for i in sequencia_de_acesso]
            
            resultados = {
                'fifo': fifo(numero_molduras, numero_paginas, list(sequencia_de_acesso)),
                'mru': mru(numero_molduras, numero_paginas, list(sequencia_de_acesso)),
                'nuf': nuf(numero_molduras, numero_paginas, list(sequencia_de_acesso)),
            }

            resultado_otimo = otimo(numero_molduras, numero_paginas, sequencia_de_acesso)
            melhor_resultado = min(resultados, key=resultados.get)
            empate = False
            if resultados[melhor_resultado] == resultado_otimo:
                empate = True
            print(f'{resultados["fifo"]}|{resultados["mru"]}|{resultados["nuf"]}|{resultado_otimo}|{"empate" if empate else melhor_resultado}')
                


if __name__ == '__main__':
    main()