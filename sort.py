import random

# Algoritmos de ordenamento

# Insertion sort com busca linear (ISBL)
# Fonte: LET #03
def ISBL(lista): 
    trocas = comparacoes = 0
    for i in range(1, len(lista)):             # do segundo ao último (o primeiro faz parte do sub lista ordenado)
        chave = lista[i]                       # chave a inserir no sub lista ordenado
        j = i-1                                # último elemento do sub lista ordenado         
        while (j >= 0) and (lista[j] > chave): # busca linear da direita para a esquerda no sub lista ordenado            
            comparacoes = comparacoes + 1
            lista[j+1] = lista[j]
            j = j -1
            trocas = trocas + 1
        lista[j+1] = chave
        trocas = trocas + 1
    return {'trocas':trocas, 'comparacoes':comparacoes}                         # retorna quantidade de operações

# Insertion sort com busca binária (ISBB)
# Fonte: https://gist.github.com/danielmatoscastro/1392e5816a436553076b2361c4bbc67d
# Adaptado para contabilizar os dados de desempenho (trocas e comparações)

def busca_binaria(lista, inicio, fim, elemento, comparacoes):
    meio = ((fim - inicio) // 2) + inicio

    comparacoes = comparacoes + 1 # faz sempre 1 comparação, entrando obrigatoriamente em uma das condições
    if lista[meio] == elemento or inicio >= fim:
        #return [meio]
        return {'resultado' : meio, 'comparacoes': comparacoes}
    elif lista[meio] < elemento:
        return busca_binaria(lista, meio+1, fim, elemento, comparacoes)
    else:
        return busca_binaria(lista, inicio, meio-1, elemento, comparacoes)


def ISBB(lista):
    trocas = comparacoes = 0
    for i in range(len(lista)):
        comparacoes = comparacoes + 1
        elemento = lista[i]
        j = i-1

        busca = busca_binaria(lista, 0, j, elemento, 0)
        posicao = busca['resultado']
        comparacoes = comparacoes + busca['comparacoes']

        while j >= posicao:
            trocas = trocas + 1
            lista[j+1] = lista[j]
            j = j-1

        if lista[posicao] <= elemento:
            trocas = trocas + 1
            lista[posicao+1] = elemento
        else:
            trocas = trocas + 1
            lista[posicao+1] = lista[posicao]
            lista[posicao] = elemento

    return {'trocas':trocas, 'comparacoes':comparacoes}
# Shell sort (SheS)
# Fonte: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OShellSort.html
# Adaptado para contabilizar os dados de desempenho (trocas e comparações)

def SheS(lista):
    trocas = comparacoes = 0
    sublistcount = len(lista)//2
    while sublistcount > 0:
      comparacoes = comparacoes + 1
      for startposition in range(sublistcount):
        gap = gapInsertionSort(lista,startposition,sublistcount)
        trocas = trocas + gap['trocas']
        comparacoes = comparacoes + gap['comparacoes']

      sublistcount = sublistcount // 2

    return {'trocas': trocas, 'comparacoes': comparacoes}

def gapInsertionSort(lista,start,gap):
    trocas = comparacoes = 0
    for i in range(start+gap,len(lista),gap):

        currentvalue = lista[i]
        position = i

        while position>=gap and lista[position-gap]>currentvalue:
            comparacoes = comparacoes + 1
            trocas = trocas + 1

            lista[position]=lista[position-gap]
            position = position-gap

        trocas = trocas + 1
        lista[position]=currentvalue

    return {'trocas': trocas, 'comparacoes': comparacoes}

# Bubble sort (BubS)
# Fonte: LET #04

def BubS(lista): 
    trocas = comparacoes = pos_troca = 0
    qtd_elementos = len(lista)-1
    troca = True
    
    while troca:
        troca = False
        for i in range(0, qtd_elementos):
            comparacoes = comparacoes + 1
            if  lista[i] >  lista[i+1]:
                tmp =  lista[i]
                lista[i] =  lista[i+1]
                lista[i+1] = tmp
                troca = True  
                pos_troca = i
                trocas = trocas + 1
        qtd_elementos = pos_troca
                
    return {'trocas':trocas, 'comparacoes':comparacoes}

# Quick sort randomizado (QukS)
# Fonte: https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
# Adaptado para contabilizar os dados de desempenho (trocas e comparações)

def QukS(lista):
    return quicksort(lista, 0, len(lista) - 1, 0, 0)

def quicksort(lista, start , stop, trocas, comparacoes):
    if(start < stop):
        comparacoes = comparacoes + 1
        # pivotindex is the index where
        # the pivot lies in the array
        part = partitionrand(lista,\
                             start, stop, trocas, comparacoes)
        pivotindex = part['pivot']
        trocas = trocas + part['trocas']
        comparacoes = comparacoes + part['comparacoes']
         
        # At this stage the array is
        # partially sorted around the pivot.
        # Separately sorting the
        # left half of the array and the
        # right half of the array.
        quicksort(lista , start , pivotindex-1, trocas, comparacoes)
        quicksort(lista, pivotindex + 1, stop, trocas, comparacoes)
    return {'trocas': trocas, 'comparacoes': comparacoes}
 
# This function generates random pivot,
# swaps the first element with the pivot
# and calls the partition function.
def partitionrand(lista , start, stop, trocas, comparacoes):
 
    # Generating a random number between the
    # starting index of the array and the
    # ending index of the array.
    randpivot = random.randrange(start, stop)
 
    # Swapping the starting element of
    # the array and the pivot
    trocas = trocas + 1
    lista[start],  lista[randpivot] = \
         lista[randpivot],  lista[start]
    return partition(lista, start, stop, trocas, comparacoes)
 
'''
This function takes the first element as pivot,
places the pivot element at the correct position
in the sorted array. All the elements are re-arranged
according to the pivot, the elements smaller than the
pivot is places on the left and the elements
greater than the pivot is placed to the right of pivot.
'''
def partition(lista,start,stop, trocas, comparacoes):
    pivot = start # pivot
     
    # a variable to memorize where the
    i = start + 1
     
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
         
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if  lista[j] <=  lista[pivot]:
            comparacoes = comparacoes + 1
            trocas = trocas + 1
            lista[i] ,  lista[j] =  lista[j] ,  lista[i]
            i = i + 1

    trocas = trocas + 1
    lista[pivot] ,  lista[i - 1] =\
             lista[i - 1] ,  lista[pivot]
    pivot = i - 1
    return {'pivot' : pivot, 'trocas': trocas, 'comparacoes': comparacoes}
 
# Selection sort (SelS)
# Fonte: desenvolvido como atividade da disciplina INF01202 no semestre 2021/1
# Adaptado para contabilizar os dados de desempenho (trocas e comparações)

def SelS(lista):
    trocas = comparacoes = 0
    for pos in range(len(lista) - 1):
        min = pos
        for i in range (pos + 1, len(lista)):
            if lista[i] < lista[min]:
                comparacoes = comparacoes + 1
                min = i
        if pos != min:
            trocas = trocas + 1
            lista[pos], lista[min] = lista[min], lista[pos]
    return {'trocas': trocas, 'comparacoes': comparacoes}

# Heap sort (HepS)
# Fonte: https://www.programiz.com/dsa/heap-sort
# Adaptado para contabilizar os dados de desempenho (trocas e comparações)

def heapify(lista, n, i, trocas, comparacoes):
    trocas = comparacoes = 0
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and  lista[i] <  lista[l]:
        comparacoes = comparacoes + 1
        largest = l

    if r < n and  lista[largest] <  lista[r]:
        comparacoes = comparacoes + 1
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        comparacoes = comparacoes + 1
        trocas = trocas + 1
        lista[i],  lista[largest] =  lista[largest],  lista[i]
        heapify(lista, n, largest, trocas, comparacoes)

    return {'trocas': trocas, 'comparacoes': comparacoes}
    
  
def HepS(lista):
    trocas = comparacoes = 0
    n = len(lista)

    # Build max heap
    for i in range(n//2, -1, -1):
        h = heapify(lista, n, i, 0, 0)
        trocas = trocas + h['trocas']
        comparacoes = comparacoes + h['comparacoes']

    for i in range(n-1, 0, -1):
        # Swap
        trocas = trocas + 1
        lista[i],  lista[0] =  lista[0],  lista[i]

        # Heapify root element
        h = heapify(lista, i, 0, 0, 0)
        trocas = trocas + h['trocas']
        comparacoes = comparacoes + h['comparacoes']
    return {'trocas': trocas, 'comparacoes': comparacoes}


# Timsort (TimS)
# Fonte: https://www.geeksforgeeks.org/timsort/
# Adaptado para contabilizar os dados de desempenho (trocas e comparações)

MIN_MERGE = 32
 
def calcMinRun(n):
    trocas = comparacoes = 0
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.
 
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        comparacoes = comparacoes + 1
        r |= n & 1
        n >>= 1
    #return n + r
    return {'retorno' : (n + r), 'trocas': trocas, 'comparacoes': comparacoes}
 
 
# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(lista, left, right):
    trocas = comparacoes = 0
    for i in range(left + 1, right + 1):
        j = i
        while j > left and  lista[j] <  lista[j - 1]:
            comparacoes = comparacoes + 1
            trocas = trocas + 1
            lista[j],  lista[j - 1] =  lista[j - 1],  lista[j]
            j -= 1
    return {'trocas': trocas, 'comparacoes': comparacoes}
 
 
# Merge function merges the sorted runs
def merge(lista, l, m, r):
    trocas = comparacoes = 0
 
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(lista[l + i])
    for i in range(0, len2):
        right.append(lista[m + 1 + i])
 
    i, j, k = 0, 0, l
 
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        comparacoes = comparacoes + 1
        if left[i] <= right[j]:
            comparacoes = comparacoes + 1
            trocas = trocas + 1
            lista[k] = left[i]
            i += 1
 
        else:
            comparacoes = comparacoes + 1
            trocas = trocas + 1
            lista[k] = right[j]
            j += 1
 
        k += 1
 
    # Copy remaining elements of left, if any
    while i < len1:
        comparacoes = comparacoes + 1
        trocas = trocas + 1
        lista[k] = left[i]
        k += 1
        i += 1
 
    # Copy remaining element of right, if any
    while j < len2:
        comparacoes = comparacoes + 1
        trocas = trocas + 1
        lista[k] = right[j]
        k += 1
        j += 1
    return {'trocas': trocas, 'comparacoes': comparacoes}
 
# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def TimS(lista):
    trocas = comparacoes = 0
    n = len(lista)
    minRunCall = calcMinRun(n)
    minRun = minRunCall['retorno']
    trocas = trocas + minRunCall['trocas']
    comparacoes = comparacoes + minRunCall['comparacoes']
 
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        i = insertionSort(lista, start, end)
        trocas = trocas + i['trocas']
        comparacoes = comparacoes + i['comparacoes']
 
    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:
        comparacoes = comparacoes + 1
        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
 
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                comparacoes = comparacoes + 1
                m = merge(lista, left, mid, right)
                trocas = trocas + m['trocas']
                comparacoes = comparacoes + m['comparacoes']
 
        size = 2 * size
    return {'trocas': trocas, 'comparacoes': comparacoes}

# Merge sort (MerS)
# Fonte: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
# Adaptado para contabilizar os dados de desempenho (trocas e comparações)

def MerS(lista):
    return merge_sort(lista, 0, 0)

def merge_sort(lista, trocas, comparacoes):
    trocas = comparacoes = 0
    if len(lista)>1:
        mid = len(lista)//2
        lefthalf = lista[:mid]
        righthalf = lista[mid:]

        lt = merge_sort(lefthalf, 0, 0)
        rt = merge_sort(righthalf, 0, 0)

        trocas = trocas + lt['trocas'] + rt['trocas']
        comparacoes = comparacoes + lt['comparacoes'] + rt['comparacoes']

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            comparacoes = comparacoes + 2
            if lefthalf[i] < righthalf[j]:
                comparacoes = comparacoes + 1
                trocas = trocas + 1
                lista[k]=lefthalf[i]
                i=i+1
            else:
                 comparacoes = comparacoes + 1
                 trocas = trocas + 1
                 lista[k]=righthalf[j]
                 j=j+1
            k=k+1

        while i < len(lefthalf):
            comparacoes = comparacoes + 1
            trocas = trocas + 1
            lista[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            comparacoes = comparacoes + 1
            trocas = trocas + 1
            lista[k]=righthalf[j]
            j=j+1
            k=k+1
            
    return {'trocas': trocas, 'comparacoes': comparacoes}
"""
teste = [56,1,8,2,3,4,22,546,2]
print(f'Array original: {teste}\n')

funcoes = [ISBL, ISBB, SheS, BubS, QukS, SelS, HepS, TimS, MerS]

for i in range(len(funcoes)):
    f = funcoes[i]

    ordenado = list(teste)
    retorno = f(ordenado)

    print(f'({i+1}) Ordenando com o algoritmo {f.__name__}')
    print(f'Retorno: {retorno}')
    print(f'Array ordenado: {ordenado}')
"""