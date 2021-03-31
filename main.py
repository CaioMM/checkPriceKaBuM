import time
import checkLib as ck
from os import system

# Variáveis Globais

print('Preparando DB...')
# banco de dados
itensKabum, dados = ck.createDb()

print('Inicializando...')
time.sleep(2)

system('cls')

while True:

    cont = 0

    #     checar variação no banco quanto a disponibilidade dos itens

    for page in dados:
        for dado in page:

            if dado['codigo'] not in itensKabum:
                itensKabum[dado['codigo']] = [dado['disponibilidade'], False]

            ck.checkState(dado, itensKabum)

            if(ck.checkAvailable(dado)):

                ck.checkNividia(dado, cont, itensKabum)
                ck.checkAMD(dado, cont, itensKabum)

    if cont == 0:
        print('Não foram encontradas placas para os critérios de busca.')
    else:
        print(f'Foram encontrados {cont} itens disponíveis.')

    print('Iniciando Nova Busca em 2 segundos')
    time.sleep(2)
    for i in range(0,20):
        print('\r\n')

    dados = ck.requestKabumVGAPages()