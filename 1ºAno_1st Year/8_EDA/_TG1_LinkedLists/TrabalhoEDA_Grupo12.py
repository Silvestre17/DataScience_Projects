# =============================================== TRABALHO DE GRUPO EDA ================================================
# ISCTE-IUL
# 1º ano | Licenciatura em Ciência de Dados
# Trabalho de Grupo Intermédio | U.C. Estruturas de Dados e Algoritmos
# André Silvestre Nº104532 | Diogo Catarino Nº104745 | Eduardo Silva Nº104943 | Francisco Gomes Nº104944


# ============= Imports =============
from matplotlib import pyplot as plt
import random
import timeit
import sys

# --------------- Aumentar o limite de recursividade do Python ---------------
sys.setrecursionlimit(3000)


# ============================================== LISTA DUPLAMENTE LIGADA ===============================================

# ==================== NÓ DA LISTA DL ====================
class Node_to_DP:

    def __init__(self, item):
        self.__data = item
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def prev(self):
        return self.__prev

    @property
    def next(self):
        return self.__next

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @next.setter
    def next(self, new_next):
        self.__next = new_next

    @prev.setter
    def prev(self, new_prev):
        self.__prev = new_prev


# ================== CLASSE DA LISTA DL ==================
class ListaDL:  # ListaDL | Lista Duplamente Ligada

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # [1] -> Comprimento ou tamanho: quantos itens estão na lista – len()
    def __len__(self):
        return self.__size

    # [2] -> Indicar se a lista está vazia – vazia()
    def vazia(self):
        return self.__size == 0

    # [3] -> Esvaziar a lista – limpar()
    def limpar(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # [4] -> Consultar (devolver) elemento na posição p – ver(p)
    def ver(self, p):
        if p > self.__size or self.vazia():
            raise ValueError('Posição Inválido')
        this = self.__head
        iterador = 1
        while iterador != p:
            this = this.next
            iterador += 1
        return f'Posição {p} na Lista: {this.data}'

    # [5] -> Inserir um dado item na lista - ins(item) -> inserção na cauda
    def ins(self, item):
        prev = None
        this = self.__tail
        while this != None:
            prev = this
            this = this.next
        newNode = Node_to_DP(item)
        if self.__head == None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
            newNode.prev = prev
        self.__tail = newNode
        self.__size += 1

    # [6] -> Remover um determinado item da lista - rem(item)
    def rem(self, item):
        if self.vazia():
            raise ValueError('Lista vazia')
        this = self.__head
        prev = None
        found = False
        while this != None and not found:
            if this.data == item:
                found = True
            else:
                prev = this
                this = this.next
        if found is True:
            if self.__size > 1:
                if prev == None:
                    self.__head = this.next
                    this.next.prev = None
                elif this.next == None:
                    prev.next = None
                    self.__tail = prev
                else:
                    prev.next = this.next
                    this.next.prev = this.prev
                self.__size -= 1
            else:
                self.limpar()
        return f"** O item {item} foi eliminado da Lista! **"

    # [7] -> Mostrar o conteúdo completo da lista – mostrar()
    def mostrar(self):  # __str__
        values = ''
        pointer = self.__head
        while pointer is not None:
            values += '{0} '.format(pointer.data)
            pointer = pointer.next
        if self.__head == None:
            return f'\nListaDL: [{values}] \n Head: {None} \n Tail: {None} \n Size: {self.__size}\n'
        return f'\nListaDL: [{values}] \n Head: {self.__head.data} \n Tail: {self.__tail.data} \n Size: {self.__size}\n'

    # [8] -> Indicar se existe na lista um item com um dado valor – existe(item)
    # Algoritmo de pesquisa binária -> devolver 0 (zero) se o item procurado não existir ou i se o item foi encontrado
    # na i-ésima posição e deve usar uma pesquisa sequencial
    def existe(self, item):
        b = self.copiar()
        b.ordenar("m")
        n = b.__size
        L = 0
        R = n - 1
        i = 0
        mid_node = b.__head
        while L <= R:
            mid_index = (L + R) // 2
            while i != mid_index:
                mid_node = mid_node.next
                i += 1
            if mid_node.data < item:
                L = mid_index + 1
            elif mid_node.data > item:
                R = mid_index - 1
            else:
                this = self.__head
                i_posicao = 1
                while i_posicao - 1 < self.__size:
                    if this.data == item:
                        print(f'O elemento {item} está na posição {i_posicao}!')
                    this = this.next
                    i_posicao += 1
                break
            i = 0
            mid_node = b.__head
        return 0

    # [EXTRA] - Algoritmo MergeSort - Dividir
    @staticmethod
    def dividir(tempHead):  # tempHead -> Cabeça temporária
        fast = slow = tempHead
        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
        meio = slow.next
        slow.next = None
        return meio

    # [EXTRA] - Algoritmo MergeSort - Merge
    def merge(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

    # [EXTRA] - Algoritmo MergeSort
    def mergeSort(self, tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead
        second = self.dividir(tempHead)
        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)
        return self.merge(tempHead, second)

    # [9] -> Ordenar a lista – ordenar()
    # Um parâmetro que indica qual a ordenação a usar (por exemplo: b indica bubblesort e q indica quicksort)
    def ordenar(self, arg='m'):
        if arg == 'b':
            if self.__size == 0:
                raise ValueError('Lista vazia')
            if self.__size == 1:
                return
            k = 0
            comp = self.__size
            this = self.__head
            while k < comp:
                for c in range(comp - 1):
                    if this.data > this.next.data:
                        this.data, this.next.data = this.next.data, this.data
                    this = this.next
                this = self.__head
                comp -= 1
                k += 1
        elif arg == 'm':
            if self.__size == 0:
                raise ValueError('Lista vazia')
            if self.__size == 1:
                return self.mostrar()
            self.__head = self.mergeSort(self.__head)
            prev = None
            this = self.__head
            while this != None:
                prev = this
                this = this.next
            self.__tail = prev

    # [EXTRA] - Retorna uma cópia da ListaDL
    def copiar(self):
        a = ListaDL()
        copia = [None] * self.__size
        this = self.__head
        i = 0
        while i < self.__size:
            copia[i] = this.data
            this = this.next
            i += 1
        for i in copia:
            a.ins(i)
        return a


# ================================================= LISTA CIRCULAR =====================================================

# ================= NÓ DA LISTA CIRCULAR ==================
class Node:

    def __init__(self, item):
        self.__data = item
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @next.setter
    def next(self, new_next):
        self.__next = new_next


# ====================================== TAD LISTA CIRCULAR ======================================
class ListaCircular:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # [1] -> Comprimento ou tamanho: quantos itens estão na lista – len()
    def __len__(self):
        return self.__size

    # [2] -> Indicar se a lista está vazia – vazia()
    def vazia(self):
        return self.__size == 0

    # [3] -> Esvaziar a lista – limpar()
    def limpar(self):
        self.__head = None
        self.__size = 0

    # [4] -> Consultar (devolver) elemento na posição p – ver(p)
    def ver(self, p):
        if p > self.__size or self.vazia():
            raise ValueError('Posição Inválido')
        this = self.__head
        iterador = 1
        while iterador != p:
            this = this.next
            iterador += 1
        return f'Posição {p} na Lista: {this.data}!!'

    # [5] -> Inserir um dado item na lista - ins(item) -> inserção no **fim**
    def ins(self, item):
        newNode = Node(item)
        if self.__head == None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__tail.next = self.__head
        self.__size += 1

    # [6] -> Remover um determinado item da lista - rem(item)
    def rem(self, item):
        if self.vazia():
            raise ValueError('Lista vazia')
        this = self.__head
        prev = None
        i = 0
        if self.__size > 1:
            while i < self.__size:
                if this.data == item:
                    if this == self.__head:  # Remover na cabeça
                        self.__tail.next = this.next
                        self.__head = this.next
                        self.__size -= 1
                        break
                    elif this == self.__tail:  # Remover na cauda
                        prev.next = self.__head
                        self.__tail = prev
                        self.__size -= 1
                        break
                    else:
                        prev.next = this.next  # Outros Casos
                        self.__size -= 1
                        break
                prev = this
                this = this.next
                i += 1
        elif this.data == item:
            self.limpar()
        return

    # [7] -> Mostrar o conteúdo completo da lista – mostrar()
    def mostrar(self):  # __str__
        values = ''
        pointer = self.__head
        i = 1
        while i <= self.__size:
            values += '{0} '.format(pointer.data)
            pointer = pointer.next
            i += 1
        if self.__head == None:
            return f'\nListaSL Circular: [{values}] \n Head: {None} \n Tail: {None} \n Size: {self.__size}\n'
        return f'\nListaSL Circular: [{values}] \n Head: {self.__head.data} \n Tail: {self.__tail.data} \n Size: ' \
               f'{self.__size}\n'

    # [8] -> Indicar se existe na lista um item com um dado valor – existe(item)
    def existe(self, item):
        b = self.copiar()
        b.ordenar("m")
        n = b.__size
        L = 0
        R = n - 1
        i = 0
        mid_node = b.__head
        while L <= R:
            mid_index = (L + R) // 2
            while i != mid_index:
                mid_node = mid_node.next
                i += 1
            if mid_node.data < item:
                L = mid_index + 1
            elif mid_node.data > item:
                R = mid_index - 1
            else:
                this = self.__head
                i_posicao = 1
                while i_posicao - 1 < self.__size:
                    if this.data == item:
                        print(f'O elemento {item} está na posição {i_posicao}!')
                    this = this.next
                    i_posicao += 1
                break
            i = 0
            mid_node = b.__head
        return 0

    # [EXTRA] - Algoritmo MergeSort - Dividir
    @staticmethod
    def dividir(tempHead):  # tempHead -> Cabeça temporária
        fast = slow = tempHead
        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp

    # [EXTRA] - Algoritmo MergeSort - Merge
    def merge(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

    # [EXTRA] - Algoritmo MergeSort
    def mergeSort(self, tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead
        second = self.dividir(tempHead)
        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)
        return self.merge(tempHead, second)

    # [9] -> Ordenar a lista – ordenar()
    # Um parâmetro que indica qual a ordenação a usar (por exemplo: b indica bubblesort e q indica quicksort)
    def ordenar(self, arg='m'):
        if arg == 'b':
            k = 0
            comp = self.__size
            this = self.__head
            while k <= comp * 2:
                for c in range(comp):
                    if this.data > this.next.data:
                        this.data, this.next.data = this.next.data, this.data
                    this = this.next
                this = self.__head
                comp -= 1
                k += 1
        elif arg == 'm':
            if self.__size == 0:
                raise ValueError('Lista vazia')
            if self.__size == 1:
                return
            self.__tail.next = None
            self.__head = self.mergeSort(self.__head)
            prev = None
            this = self.__head
            i = 0
            while i != self.__size:
                prev = this
                this = this.next
                i += 1
            self.__tail = prev
            self.__tail.next = self.__head

    # [EXTRA] - Retorna uma cópia da Lista Circular
    def copiar(self):
        a = ListaCircular()
        copia = [None] * self.__size
        this = self.__head
        i = 0
        while i < self.__size:
            copia[i] = this.data
            this = this.next
            i += 1
        for i in copia:
            a.ins(i)
        return a


# ========================================= ANÁLISE EMPÍRICA AOS ALGORITMOS ============================================

# [AUXILIAR] -> Devolve uma lista com n números inteiros gerados aleatoriamente entre 0 e 10 000 [0, 10 000]
def gera_inteiros(n):
    a = []
    for i in range(0, n):
        a.append(random.randrange(10001))
    return a


# [5] - Inserir | [6] - Remover | [8] - Existe | [9] - Ordenar (BubbleSort) | [9] - Ordenar (MergeSort)
n = [100, 300, 500, 800, 1100, 1400, 1700, 2000]

lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []


# [ANALISAR] -> Devolve o teste aos algoritmos em lists com n a variar em {100,300,500,800,1100,1400,1700,2000},
# cronometrando os tempos para os principais métodos das TAD Listas.

def testar(n):
    l = ListaDL()  # [ListaDL()] OU [ListaCircular()]
    seq = gera_inteiros(n)

    # Testar o [ins]
    inicio = timeit.default_timer()
    for item in seq:
        l.ins(item)
    fim = timeit.default_timer()
    duracao_ins = round((fim - inicio), 5)
    lista1.append(duracao_ins)

    # Testar o [existe] -> Pesquisa Binária
    inicio = timeit.default_timer()
    for item in seq:
        l.existe(item)
    fim = timeit.default_timer()
    duracao_existe = round((fim - inicio), 5)
    lista3.append(duracao_existe)

    # Testar o [ordenar()] -> Bubble Sort
    lo1 = l.copiar()
    inicio = timeit.default_timer()
    lo1.ordenar('b')
    fim = timeit.default_timer()
    duracao_ordenar_1 = round((fim - inicio), 5)
    lista4.append(duracao_ordenar_1)

    # Testar o [ordenar()] -> Merge Sort
    inicio = timeit.default_timer()
    l.ordenar('m')
    fim = timeit.default_timer()
    duracao_ordenar_2 = round((fim - inicio), 5)
    lista5.append(duracao_ordenar_2)

    # Testar o [rem]
    inicio = timeit.default_timer()
    for item in seq:
        l.rem(item)
    fim = timeit.default_timer()
    duracao_remover = round((fim - inicio), 5)
    lista2.append(duracao_remover)

    print(f"{n  :<15}{duracao_ins  :<20}{duracao_remover   :<20}{duracao_existe  :<20}{duracao_ordenar_1:<30}{duracao_ordenar_2:<30}")


n = [100, 300, 500, 800, 1100, 1400, 1700, 2000]


def plot():
    plt.plot(n, lista1, label='Insert')
    plt.plot(n, lista2, label='Remove')
    plt.plot(n, lista3, '#808080', label='Existe')
    plt.plot(n, lista4, label='OrdenarBubblesort')
    plt.plot(n, lista5, label='OrdenarMergesort')
    plt.legend()
    plt.show()


#if __name__ == '__main__':
    # ===================================== Testes à ListaDL ====================================
    # lst_DL = ListaDL()
    # lst_DL.ins(1)
    # lst_DL.ins(4)
    # lst_DL.ins(1)
    # lst_DL.ins(10)
    # lst_DL.ins(1)
    # lst_DL.ins(5)
    # lst_DL.ins(66)
    # lst_DL.ins(1)
    # lst_DL.ins(99)
    # lst_DL.ins(100)
    # print(lst_DL.mostrar())
    #
    # print(lst_DL.existe(100))
    # print(lst_DL.existe(1))
    # print(lst_DL.existe(456789))
    # print(lst_DL.ver(5))
    #
    # lst_DL.rem(4)
    # lst_DL.rem(99)
    # lst_DL.rem(80)
    # lst_DL.rem(1)
    # lst_DL.rem(1)
    # lst_DL.rem(10)
    # lst_DL.rem(5)
    # lst_DL.rem(1)
    # lst_DL.rem(1)
    # lst_DL.rem(1)
    # lst_DL.rem(66)
    # lst_DL.rem(100)
    # print(lst_DL.mostrar())

    # ================================= Testes à Lista Circular =================================
    # lst_Circular = ListaCircular()
    # lst_Circular.ins(1)
    # lst_Circular.ins(4)
    # lst_Circular.ins(1)
    # lst_Circular.ins(10)
    # lst_Circular.ins(1)
    # lst_Circular.ins(5)
    # lst_Circular.ins(66)
    # lst_Circular.ins(1)
    # lst_Circular.ins(99)
    # lst_Circular.ins(100)
    # print(lst_Circular.mostrar())
    #
    # print(lst_Circular.existe(100))
    # print(lst_Circular.existe(1))
    # print(lst_Circular.existe(456789))
    # print(lst_Circular.ver(5))
    #
    # lst_Circular.rem(4)
    # lst_Circular.rem(99)
    # lst_Circular.rem(80)
    # lst_Circular.rem(1)
    # lst_Circular.rem(1)
    # lst_Circular.rem(10)
    # lst_Circular.rem(5)
    # lst_Circular.rem(1)
    # lst_Circular.rem(1)
    # lst_Circular.rem(1)
    # lst_Circular.rem(66)
    # lst_Circular.rem(100)
    # print(lst_Circular.mostrar())

    # ==================================== Testes à Análise =====================================
    # print('\n=================================== LISTA DL ===================================')

    # print(f"{'Nº de Exec': <15}{'DL Inserir(ins) ': <20}{'DL Remover(rem)': <20}{'DL Existe': <20}
    #   {'DL Ordenar [BubbleSort]': <30}{'DL Ordenar [MergeSort]': <30}")

    # n = [100, 300, 500, 800, 1100, 1400, 1700, 2000]
    # for i in n:
    #     testar(i)
    # plot()

    # print('\n=================================== LISTA CIRCULAR===================================')
    # print(f"{'Nº de Exec': <15}{'LC Inserir(ins) ': <20}{'LC Remover(rem)': <20}{'LC Existe': <20}
    #     {'LC Ordenar [BubbleSort]': <30}{'LC Ordenar [MergeSort]': <30}")

    # n = [100, 300, 500, 800, 1100, 1400, 1700, 2000]
    # for i in n:
    #     testar(i)
    # plot()
