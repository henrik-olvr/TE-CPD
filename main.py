import sys
import random

def lerNumero(arq, bytes, pos):
    arq.seek(pos * bytes)
    return int.from_bytes(arq.read(bytes), byteorder='little')

obterAleatorios = False # Obter os números de forma aleatória (True) ou sequencial (False) do arquivo
def obterNumeros(arq, tam):
    ret = []
    for i in range(tam):
        r = random.randint(0, max_arquivo) if obterAleatorios else i
        #print(f'r={r}')
        num = lerNumero(arq, bytes_num, r)
        ret.append(num)
    return ret

print('\n\nComparação de Algoritmos de Classificação\n')
print('Aluno: João Raphael Fontoura Dorneles (333315)')
print('Disciplina: INF01124 - Classificação e Pesquisa de Dados\n')

nome_arquivo = 'randomnumbers'
max_arquivo = 10000000
bytes_num = 4
try:
    arq = open(f'{nome_arquivo}.bin', 'rb')
    print(f'O arquivo {nome_arquivo}.bin foi aberto com sucesso.')
except:
    print(f'Não foi possível abrir o arquivo {nome_arquivo}.bin, verifique o diretório e tente novamente.')
    sys.exit(0)

# Conferindo se o arquivo está sendo lido corrretamente
ref = [253161, 293217, 84591, 57084, 992328, 1438214, 910653, 106848, 600246, 844451]
correto = True
for i in range(10):
    n = lerNumero(arq, bytes_num, i)
    if n != ref[i]:
        correto = False
        break
    #print(f'{n:07d}')

if correto:
    print('O arquivo foi lido corretamente.')
else:
    print('Não foi possivel ler o arquivo corretamente, verifique o arquivo no diretório e a lista de referência.')
    if (input('Você deseja continuar mesmo assim? (S/N) ').lower() == 'n'):
        print('Interrompendo execução.')
        sys.exit(0)

a0 = obterNumeros(arq, 5) # Array obtido sem ordem específica
a1 = list(a0)
a1.sort() # Array ordenado de forma crescente
a2 = list(a1)
a2.reverse() # Array ordenado de forma decrescente

#print(a0)
#print(a1)
#print(a2)