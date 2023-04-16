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
# !!! : Necessário adaptar para contabilizar as trocas e comparações

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
# Fonte: https://www.programiz.com/dsa/heap-sort
# !!! : Necessário adaptar para contabilizar as trocas e comparações

def heapify(arr, n, i):
      # Find largest among root and children
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      # If root is not largest, swap with largest and continue heapifying
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
def HepS(arr):
      n = len(arr)
  
      # Build max heap
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
  
      for i in range(n-1, 0, -1):
          # Swap
          arr[i], arr[0] = arr[0], arr[i]
  
          # Heapify root element
          heapify(arr, i, 0)

# Timsort (TimS)
# Fonte: https://www.geeksforgeeks.org/timsort/
# !!! : Necessário adaptar para contabilizar as trocas e comparações

MIN_MERGE = 32
 
def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.
 
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
 
# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
 
# Merge function merges the sorted runs
def merge(arr, l, m, r):
 
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
 
    i, j, k = 0, 0, l
 
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1
 
    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
 
    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
 
 
# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def TimS(arr):
    n = len(arr)
    minRun = calcMinRun(n)
 
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
 
    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:
 
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
                merge(arr, left, mid, right)
 
        size = 2 * size

# Merge sort (MerS)
# Fonte: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
# !!! : Necessário adaptar para contabilizar as trocas e comparações

def MerS(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        MerS(lefthalf)
        MerS(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

teste = [56,1,8,2,3,4,22,546,2]
ordenado = list(teste)

funcao = SheS

retorno = funcao(ordenado)
print(teste)

print(f'Ordenando com a função {funcao.__name__}')
print(retorno)
print(ordenado)