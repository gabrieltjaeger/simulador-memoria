from collections import OrderedDict, Counter


def fifo(numero_molduras: int, sequencia_de_acesso: list) -> int:
    molduras = []
    trocas_de_paginas = 0
    while len(sequencia_de_acesso) > 0:
        pagina = sequencia_de_acesso.pop(0)
        if pagina in molduras:
            continue
        if pagina not in molduras:
            if len(molduras) == numero_molduras:
                molduras.pop(0)
            molduras.append(pagina)
            trocas_de_paginas += 1
    return trocas_de_paginas


def mru(numero_molduras: int, sequencia_de_acesso: list) -> int:
    molduras = {}
    trocas_de_paginas = 0
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
            trocas_de_paginas += 1
        else:
            molduras[pagina] = tempo
    return trocas_de_paginas


def nuf(numero_molduras: int, sequencia_de_acesso: list) -> int:
    molduras = OrderedDict()
    trocas_de_paginas = 0
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
            trocas_de_paginas += 1
        else:
            molduras[pagina] += 1
    return trocas_de_paginas


def otimo(numero_molduras: int, sequencia_de_acesso: list) -> int:
    molduras = OrderedDict()
    trocas_de_paginas = 0
    for i, pagina in enumerate(sequencia_de_acesso):
        molduras = OrderedDict(
            {k: v-1 for k, v in molduras.items() if (v > 1)})
        if pagina in molduras:
            if pagina in sequencia_de_acesso[i+1:]:
                molduras[pagina] = sequencia_de_acesso.index(pagina, i+1) - i+1
            continue
        trocas_de_paginas += 1
        if len(molduras) >= numero_molduras:
            molduras = OrderedDict(
                sorted(molduras.items(), key=lambda x: x[1]))
            molduras.popitem()
        if pagina in sequencia_de_acesso[i+1:]:
            molduras[pagina] = sequencia_de_acesso.index(pagina, i+1) - i+1
    return trocas_de_paginas


def main():
    saida_log = ''
    with open('arquivos/entrada/inMemoria', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            linha = linha.split('|')
            numero_molduras = int(linha[0])
            sequencia_de_acesso = list(map(int, linha[2].split(' ')))

            resultados = {
                'FIFO': fifo(numero_molduras, list(sequencia_de_acesso)),
                'MRU': mru(numero_molduras, list(sequencia_de_acesso)),
                'NUF': nuf(numero_molduras, list(sequencia_de_acesso)),
                'OTIMO': otimo(numero_molduras, list(sequencia_de_acesso))
            }
            resultado_otimo = resultados.pop('OTIMO')
            melhor_resultado = min(resultados, key=resultados.get)
            empate = False
            count = Counter(resultados.values())
            melhor_resultado_repete = count[resultados[melhor_resultado]] > 1
            melhor_resultado_igual_ao_otimo = resultados[melhor_resultado] == resultado_otimo
            if melhor_resultado_repete or melhor_resultado_igual_ao_otimo:
                empate = True
            resultados = f'{resultados["FIFO"]}|{resultados["MRU"]}|{resultados["NUF"]}|{resultado_otimo}|{"empate" if empate else melhor_resultado}'
            saida_log += f'{resultados}\n'
            print(resultados)
    with open('arquivos/saida/outMemoria', 'w') as saida:
        saida.write(saida_log)


if __name__ == '__main__':
    main()
