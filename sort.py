import random

# Algoritmos de ordenamento

# Insertion sort com busca linear (ISBL)
# Fonte: LET #03
def ISBL(array): 
    trocas = comparacoes = 0
    for i in range(1, len(array)):             # do segundo ao último (o primeiro faz parte do subarray ordenado)
        chave = array[i]                       # chave a inserir no subarray ordenado
        j = i-1                                # último elemento do subarray ordenado         
        while (j >= 0) and (array[j] > chave): # busca linear da direita para a esquerda no subarray ordenado            
            comparacoes = comparacoes + 1
            array[j+1] = array[j]
            j = j -1
            trocas = trocas + 1
        array[j+1] = chave
        trocas = trocas + 1
    return {'trocas':trocas, 'comparacoes':comparacoes}                         # retorna quantidade de operações

# Insertion sort com busca binária (ISBB)
# Fonte: https://gist.github.com/danielmatoscastro/1392e5816a436553076b2361c4bbc67d
# !!! : Necessário adaptar para contabilizar as trocas e comparações

def busca_binaria(lista, inicio, fim, elemento):
    meio = ((fim - inicio) // 2) + inicio

    if lista[meio] == elemento or inicio >= fim:
        return meio
    elif lista[meio] < elemento:
        return busca_binaria(lista, meio+1, fim, elemento)
    else:
        return busca_binaria(lista, inicio, meio-1, elemento)


def ISBB(lista):
    for i in range(len(lista)):
        elemento = lista[i]
        j = i-1

        posicao = busca_binaria(lista, 0, j, elemento)

        while j >= posicao:
            lista[j+1] = lista[j]
            j = j-1

        if lista[posicao] <= elemento:
            lista[posicao+1] = elemento
        else:
            lista[posicao+1] = lista[posicao]
            lista[posicao] = elemento
# Shell sort (SheS)
# Fonte: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html
# !!! : Necessário adaptar para contabilizar as trocas e comparações

def SheS(lista):
    sublistcount = len(lista)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(lista,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",lista)

      sublistcount = sublistcount // 2

def gapInsertionSort(lista,start,gap):
    for i in range(start+gap,len(lista),gap):

        currentvalue = lista[i]
        position = i

        while position>=gap and lista[position-gap]>currentvalue:
            lista[position]=lista[position-gap]
            position = position-gap

        lista[position]=currentvalue

# Bubble sort (BubS)
# Fonte: LET #04

def BubS(array): 
    trocas = comparacoes = pos_troca = 0
    qtd_elementos = len(array)-1
    troca = True
    
    while troca:
        troca = False
        for i in range(0, qtd_elementos):
            comparacoes = comparacoes + 1
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                troca = True  
                pos_troca = i
                trocas = trocas + 1
        qtd_elementos = pos_troca
                
    return {'trocas':trocas, 'comparacoes':comparacoes}

# Quick sort randomizado (QukS)
# Fonte: https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
# !!! : Necessário adaptar para contabilizar as trocas e comparações

def QukS(lista):
    return quicksort(lista, 0, len(lista) - 1)

def quicksort(arr, start , stop):
    if(start < stop):
         
        # pivotindex is the index where
        # the pivot lies in the array
        pivotindex = partitionrand(arr,\
                             start, stop)
         
        # At this stage the array is
        # partially sorted around the pivot.
        # Separately sorting the
        # left half of the array and the
        # right half of the array.
        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)
 
# This function generates random pivot,
# swaps the first element with the pivot
# and calls the partition function.
def partitionrand(arr , start, stop):
 
    # Generating a random number between the
    # starting index of the array and the
    # ending index of the array.
    randpivot = random.randrange(start, stop)
 
    # Swapping the starting element of
    # the array and the pivot
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)
 
'''
This function takes the first element as pivot,
places the pivot element at the correct position
in the sorted array. All the elements are re-arranged
according to the pivot, the elements smaller than the
pivot is places on the left and the elements
greater than the pivot is placed to the right of pivot.
'''
def partition(arr,start,stop):
    pivot = start # pivot
     
    # a variable to memorize where the
    i = start + 1
     
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
         
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
 
# Selection sort (SelS)
# Fonte: desenvolvido como atividade da disciplina INF01202 no semestre 2021/1
# !!! : Necessário adaptar para contabilizar as trocas e comparações

def SelS(lista):
    for pos in range(len(lista) - 1):
        min = pos
        for i in range (pos + 1, len(lista)):
            if lista[i] < lista[min]:
                min = i
        if pos != min:
            lista[pos], lista[min] = lista[min], lista[pos]

# Heap sort (HepS)



# Timsort (TimS)
# Merge sort (MerS).

teste = [56,1,8,2,3,4,22,546,2]
ordenado = list(teste)
SelS(ordenado)
print(teste)
print(ordenado)