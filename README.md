# Simulador de Substituição de Páginas na Memória
Implementação de simulações de algoritmos de substituição de páginas na memória que ocorrem em um Sistema Operacional.
Para executar o script, é necessário ter a versão mais recente do Python (3.10.7) instalada e abrir um terminal na mesma pasta que o arquivo _main.py_, e executar o comando:
```
python3 main.py
```
Após, deverá ser informado ao programa o _nome do arquivo_ de entrada que contém as sequências de acesso à memória - exemplo: inMemoria - e aguardar que a execução seja finalizada para cada um dos algoritmos de substituição de páginas escolhidos - são eles: FIFO (First in, first out), MRU (Menos recentemente usada), NUF (Não usada frequentemente) e o algoritmo ótimo.

## Importante: 
O arquivo de entrada deverá estar no formato _.txt_ e deverá estar localizado dentro da pasta _entrada_, que está contida na pasta _arquivos_*. 
Ao término da execução, será impresso no console os resultados das operações com os algoritmos, sendo eles, a quantidade de troca de páginas que cada um dos algoritmos utilizou, juntamente do nome do mais performático dentre eles. Os resultados obtidos também serão armazenados em um arquivo chamado "outMemoria", no caminho "arquivos/saida".

*O caminho "arquivos/saida/<nome_do_arquivo.txt>" não deverá ser passado para o programa, quando este pedir pelo nome do arquivo a executar. Apenas _nome_do_arquivo.txt_ deverá ser passado.
