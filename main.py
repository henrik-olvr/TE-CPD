import sys
import random
import time
from datetime import datetime
import sort

# Constantes

CARTOES = [333315, 314523]
NOME_ARQ = 'randomnumbers'
NOME_SAIDA = f'R{CARTOES[0]:08d}-{CARTOES[1]:08d}'
MAX_ARQ = 10000000
BYTES_NUM = 4
FUNCOES = [sort.ISBL, sort.ISBB, sort.SheS, sort.BubS, sort.QukS, 
           sort.SelS, sort.HepS,sort.TimS, sort.MerS]
TAM_ARRAYS = [1000, 10000, 100000, 1000000, 10000000]
TAM_ARRAYS_TESTE = [5, 100, 500, 1000, 5000]

# Funções

def lerNumero(arq, bytes, pos):
    arq.seek(pos * bytes)
    return int.from_bytes(arq.read(bytes), byteorder='little')

obterAleatorios = False # Obter os números de forma aleatória (True) ou sequencial (False) do arquivo
def obterNumeros(arq, tam):
    ret = []
    for i in range(tam):
        r = random.randint(0, MAX_ARQ) if obterAleatorios else i
        #print(f'r={r}')
        num = lerNumero(arq, BYTES_NUM, r)
        ret.append(num)
    return ret

def escreverLinha(arq, texto):
    arq.write(texto + '\n')

def formatarResultados(algoritmo, tipo, tamanho, trocas, comparacoes, tempo):
    return f'{algoritmo}, {tipo}, {tamanho}, {trocas}, {comparacoes}, {tempo}'

def imprimirResultados(algoritmo, tipo, tamanho, trocas, comparacoes, tempo):
    if tipo == 'O':
        tipo = 'ordenado'
    elif tipo == 'I':
        tipo = 'inverso'
    else:
        tipo = 'randômico'
    print(f'O algoritmo {algoritmo}, aplicado sobre um array {tipo} com {tamanho} elementos precisou de {trocas} trocas, {comparacoes} comparações e {tempo}ms para ser ordenado.')

# Mensagens iniciais

print('\n\nComparação de Algoritmos de Classificação\n')
print('Aluno: João Raphael Fontoura Dorneles (333315)')
print('Aluno: Luiz Henrik Oliveira (314523)')
print('Disciplina: INF01124 - Classificação e Pesquisa de Dados\n')

# Abertura do arquivo de dados

try:
    arq = open(f'{NOME_ARQ}.bin', 'rb')
    print(f'O arquivo {NOME_ARQ}.bin foi aberto com sucesso.')
except:
    print(f'Não foi possível abrir o arquivo {NOME_ARQ}.bin, verifique o diretório e tente novamente.')
    sys.exit(0)

# Verificação da integridade do arquivo de dados

ref = [253161, 293217, 84591, 57084, 992328, 1438214, 910653, 106848, 600246, 844451]
correto = True
for i in range(10):
    n = lerNumero(arq, BYTES_NUM, i)
    if n != ref[i]:
        correto = False
        break
    #print(f'{n:07d}')

if correto:
    print(f'O arquivo {NOME_ARQ}.bin foi lido corretamente.')
else:
    print('Não foi possivel ler o arquivo corretamente, verifique o arquivo no diretório e a lista de referência.')
    if (input('Você deseja continuar mesmo assim? (S/N) ').lower() == 'n'):
        print('Interrompendo execução.')
        sys.exit(0)

# Abertura do arquivo de saída

try:
    saida = open(f'{NOME_SAIDA}.txt', 'w')
    print(f'O arquivo {NOME_SAIDA}.txt foi aberto com sucesso.')
except:
    print(f'Não foi possível criar o arquivo {NOME_SAIDA}.txt, verifique o diretório e tente novamente.')
    sys.exit(0)


escreverLinha(saida, formatarResultados('algoritmo', 'tipo', 'tamanho', 'trocas', 'comparacoes', 'tempo'))

for elementos in TAM_ARRAYS:
    a0 = obterNumeros(arq, elementos) # Array obtido sem ordem específica
    a1 = list(a0)
    a1.sort() # Array ordenado de forma crescente
    a2 = list(a1)
    a2.reverse() # Array ordenado de forma decrescente

    for algoritmo in FUNCOES:
        for tipo in ['R', 'O', 'I']:
            if tipo == 'R':
                array = list(a0)
            elif tipo == 'O':
                array = list(a1)
            else:
                array = list(a2)

            ini = round(time.time()) 

            # aqui entra a operação de ordem
            metricas = algoritmo(array)

            diferenca = round(time.time()) - ini

            agora = datetime.now()
            agoraFormatado = agora.strftime("%H:%M:%S")

            print(f'({agoraFormatado})', end=' ')
            imprimirResultados(algoritmo.__name__, tipo, elementos, metricas['trocas'], metricas['comparacoes'], diferenca)

            escreverLinha(saida, formatarResultados(algoritmo.__name__, tipo, elementos, metricas['trocas'], metricas['comparacoes'], diferenca))

#print(formatarResultados('QukS', 'O', 1000, 30, 120, 10))
#imprimirResultados('QukS', 'O', 1000, 30, 120, 10)

arq.close()
saida.close()