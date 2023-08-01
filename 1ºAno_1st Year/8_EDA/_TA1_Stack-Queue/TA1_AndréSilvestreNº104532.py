print('========================================================================')
print('                   Bem-vind@ à *Loja do Cidadão*!                       ')
print('              Para abrir o *Menu Principal* digite menu()               ')
print('========================================================================')


# T1 | CLASSE CLIENTE - Nome; NºCC/P; Secção [RC],[RP],[QC]; Prioritário (True/False)
class Cliente:

    # CONSTRUTOR - Criar o objeto do tipo Cliente
    def __init__(self, nome, numero, seccao, prioridade):
        self.__nome = nome
        self.__numero = numero
        self.__seccao = seccao
        self.__prioridade = prioridade

    # PROPRIEDADES - Servem para ser possível consultar qualquer um dos atributos (não os alterando)
    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def seccao(self):
        return self.__seccao

    @property
    def prioridade(self):
        return self.__prioridade

    # __STR__ - Converter um objeto do tipo Cliente numa string, através da instrução print().
    def __str__(self):
        return f"Nome: {self.__nome} | Nº de CC/P: {self.__numero} | Secção: {self.__seccao} | " \
               f"Prioridade: {self.__prioridade} "


# T2 | FILA DE ATENDIENTO
class Fila_de_Antendimento:

    # Iniciar a Fila de Atendimento (vazia)
    def __init__(self):
        self.__fila_de_atendimento = []
        self.__posicao = 0
        self.__prioritarios = 0

    # A fim de obter a Posição de cada Cliente, criei um iterador "__posicao"; e fiz o mesmo para Prioritários,
    # de modo a conseguir adiciona-los depois dos restantes Clientes Prioritários, mas antes dos Não Prioritários

    # Verifica se a fila está vazia
    def is_empty(self):
        return len(self.__fila_de_atendimento) == 0

    # Inserir clientes ** NÃO PRIORITÁRIOS ** (fim da fila)
    def insert_client(self, cliente):
        if not isinstance(cliente, Cliente):
            return f"*Erro* - Adicione um Cliente!"
        # append() -> Método que adiciona um elemento ao final da lista
        self.__fila_de_atendimento.append(cliente)
        self.__posicao += 1

    # Inserir clientes prioritários (início da fila MAS após o último Cliente Prioritário já na fila)
    def insert_p_client(self, cliente):
        if not isinstance(cliente, Cliente):
            return f"*Erro* - Adicione um Cliente!"
        # insert() -> Método que insere um elemento na lista no índice indicado (neste caso o __prioritarios)
        self.__fila_de_atendimento.insert(self.__prioritarios, cliente)
        self.__prioritarios += 1
        self.__posicao += 1

    # Atender o próximo cliente, retirando-o da fila de espera
    def serve_client(self):
        if self.is_empty():
            return f"A *Fila de Atendimento* está vazia!"
        self.__posicao -= 1
        for cliente in self.__fila_de_atendimento:
            if cliente.prioridade:
                self.__prioritarios -= 1
        c_atendido = self.__fila_de_atendimento[0]
        # del() -> Método que remove um elemento de um dado índice
        del (self.__fila_de_atendimento[0])  # Elimina o 1º elemento da lista (índice 0)
        return f"** Cliente em Atendimento ** | {c_atendido.nome}"

    # Visualizar o próximo cliente a ser atendido
    def view_next_client(self):
        if self.is_empty():
            return f"A *Fila de Atendimento* está vazia!"
        proximo = self.__fila_de_atendimento[0]
        return f"** Próximo Cliente ** | {proximo.nome}"

    # Eliminar um cliente pela sua posição -→ Logo, o índice a remover é [posição - 1]
    def abandon_queue(self, posicao):
        if self.is_empty():
            return f"A *Fila de Atendimento* está vazia!"
        cliente_a_remover = self.__fila_de_atendimento[posicao - 1]
        del (self.__fila_de_atendimento[posicao - 1])
        if cliente_a_remover.prioridade:
            self.__prioritarios -= 1
        self.__posicao -= 1
        return f"** Cliente removido ** | [{cliente_a_remover.seccao}] C{str(posicao).rjust(2, '0')} - " \
               f"{cliente_a_remover.nome}"  # C -> Cliente

    # Encerrar o atendimento, removendo todos os clientes em espera
    def close(self):
        self.__fila_de_atendimento = []
        self.__posicao = 0
        self.__prioritarios = 0
        return f" *Fila de Atendimento* encerrada com sucesso!!"

    # EXTRA | Guardar Pedidos
    def save_(self, f):  # f - Ficheiro
        for c in self.__fila_de_atendimento:
            f.write('{};{};{};{}'.format(c.nome, c.numero, c.seccao, c.prioridade) + '\n')

    # EXTRA | IMPORTAR Pedidos
    def import_(self, f):  # f - Ficheiro
        line = f.readline().strip()
        while line != '':
            line_ = line.split(';')
            nome = line_[0]
            numero = line_[1]
            seccao = line_[2]
            prioridade = line_[3]
            line = f.readline().strip()
            cliente = Cliente(nome, numero, seccao, prioridade)
            self.insert_client(cliente)
        f.close()

    # Devolve o número total de clientes em espera
    def __len__(self):
        return len(self.__fila_de_atendimento)

    # Devolve uma lista de todos os clientes em espera, indicando o seu nome e posição na fila (começa em 1!)
    def __str__(self):
        queue_str = '\n'
        seccao = ''
        nomes = []
        for cliente in self.__fila_de_atendimento:
            nomes.append(cliente.nome)
            seccao = cliente.seccao
        for n in range(0, self.__posicao):
            queue_str = queue_str + f"[{seccao}] C{str(n + 1).rjust(2, '0')} | {nomes[n]}\n"
        return f"============ Fila de Atendimento [{seccao}] ============\n {queue_str}"  # C -> Cliente


# De modo a dividir as 3 secções, optei por instanciar (isto é, criar variáveis) 3 filas, uma para cada secção.

Fila_de_Antendimento_RC = Fila_de_Antendimento()  # Fila da Criação/Renovação do CC
Fila_de_Antendimento_RP = Fila_de_Antendimento()  # Fila da Criação/Renovação do Passaporte
Fila_de_Antendimento_QC = Fila_de_Antendimento()  # Fila de Questões Judiciais


# T3 | INTERFACE - menu()
def menu():
    print('================= MENU PRINCIPAL *Loja do Cidadão* ===================')
    print('1. Inserir Cliente à *Fila de Atendimento*')
    print('2. Atender Cliente')
    print('3. Ver Próximo Cliente da *Fila de Atendimento*')
    print('4. Eliminar Cliente da *Fila de Atendimento*')
    print('5. Listar Todos os Clientes da *Fila de Atendimento*')
    print('6. Número de Clientes na *Fila de Atendimento*')
    print('7. Encerrar o Atendimento (Remover todos os clientes em espera)')
    print('8. Gerir Pedidos de Atendimento')
    print('0. Sair do menu')
    print('======================================================================')
    value = input('Bem vind@ à *Loja do Cidadão*! Selecione uma das opções: ')  # de 0 a 8
    # Garantir que o input inserido é um n.º de 0 a 8
    while str.isdigit(value) is False:
        print('\n ** Por favor introduza um número do menu principal! ** ')
        value = input('Bem vind@ à *Loja do Cidadão*! Selecione uma das opções: ')
    value = int(value)
    while value >= 9:
        print('\n ** Erro ao abrir o *Menu* | Digite um N.º Válido [0,8] **')
        value = input('Tente de novo! | Menu Principal *Loja do Cidadão* | Selecione uma das opções:')
        if str.isdigit(value):
            value = int(value)
        else:
            while str.isdigit(value) is False:
                print('\n ** Erro ao abrir o *Menu* | Digite um N.º Válido [0,8] **')
                value = input('Tente de novo!')
        value = int(value)
    value = int(value)
    # Para cada input inserido no Menu realizar uma operação, invocando-a
    while 0 <= value < 9:
        # 1. Inserir Cliente à *Fila de Atendimento*
        if value == 1:
            print('\n------------------------ INSERIR CLIENTE À FILA ------------------------')
            print('Preencha os campos obrigatórios *')
            # Input do Nome Completo
            nome = input('Introduza o seu Nome Completo*: ')
            while len(nome) <= 2:
                print('\n ** Por favor introduza um *Nome* Válido ** ')
                nome = input('Introduza o seu Nome Completo*: ')
            # Input do Número do CC/Passaporte
            numero = input('Introduza o seu Número do CC/Passaporte*: ')
            # str.isdigit() -> Verifica se o input inserido é um N.º
            while str.isdigit(numero) is False:
                print(' ** Por favor introduza o seu Número do CC/Passaporte ** ')
                numero = input('Introduza o seu Número do CC/Passaporte*: ')
            # Input da Secção de Atendimento
            seccao = input('Introduza a Secção de Atendimento [RC] Criação/Renovação do cartão de cidadão | [RP] '
                           'Criação/Renovação do passaporte | [QC] Questões judiciais *: ')
            # str().upper() -> Método que retorna uma string onde todos os caracteres estão em maiúsculas
            while str(seccao).upper() not in ('RC', 'RP', 'QC'):
                seccao = input('Introduza uma *Secção* Válida [RP] [RC] [QC]  *: ')
            # Input da Prioridade
            prioridade = input('É Cliente Priortário? Responda [S]/[N]*: ')
            while str(prioridade).upper() not in ('S', 'N'):
                print(' ** Por favor introduza apenas as iniciais [S] - Sim | [N] - Não ** ')
                prioridade = input('É Cliente Priortário? Responda [S]/[N]*: ')
            if str(prioridade).upper() == 'S':
                prioridade = True
            elif str(prioridade).upper() == 'N':
                prioridade = False
            cliente = Cliente(str(nome), int(numero), str(seccao).upper(), bool(prioridade))
            # Divisão por Secções RC | RP | QC
            if cliente.seccao == 'RC':
                if cliente.prioridade:
                    Fila_de_Antendimento_RC.insert_p_client(cliente)
                elif not cliente.prioridade:
                    Fila_de_Antendimento_RC.insert_client(cliente)
            elif cliente.seccao == 'RP':
                if cliente.prioridade:
                    Fila_de_Antendimento_RP.insert_p_client(cliente)
                elif not cliente.prioridade:
                    Fila_de_Antendimento_RP.insert_client(cliente)
            elif cliente.seccao == 'QC':
                if cliente.prioridade:
                    Fila_de_Antendimento_QC.insert_p_client(cliente)
                elif not cliente.prioridade:
                    Fila_de_Antendimento_QC.insert_client(cliente)
            print('\n', cliente, '\n ** Cliente inserido com sucesso! **')
        # 2. Atender Cliente - Separado por filas
        elif value == 2:
            print('\n------------------------ ATENDER CLIENTE ------------------------')
            print('Preencha os campos obrigatórios *')
            seccao = input('Introduza a Secção de Atendimento [RC] [RP] [QC] que pretende Atender*: ')
            while str(seccao).upper() not in ('RC', 'RP', 'QC'):
                seccao = input('Introduza a Secção de Atendimento [RC] Criação/Renovação do cartão de cidadão | [RP] '
                               'Criação/Renovação do passaporte | [QC] Questões judiciais *: ')
            if str(seccao).upper() == 'RC':
                print('\n', Fila_de_Antendimento_RC.serve_client())
            elif str(seccao).upper() == 'RP':
                print('\n', Fila_de_Antendimento_RP.serve_client())
            elif str(seccao).upper() == 'QC':
                print('\n', Fila_de_Antendimento_QC.serve_client())
        # 3. Ver Próximo Cliente da *Fila de Atendimento*
        elif value == 3:
            print('\n------------------------ PRÓXIMO CLIENTE ------------------------')
            print('Preencha os campos obrigatórios *')
            seccao = input('Introduza a Secção de Atendimento [RC] [RP] [QC] *: ')
            while str(seccao).upper() not in ('RC', 'RP', 'QC'):
                seccao = input('Introduza a Secção de Atendimento [RC] Criação/Renovação do cartão de cidadão | [RP] '
                               'Criação/Renovação do passaporte | [QC] Questões judiciais *: ')
            if str(seccao).upper() == 'RC':
                print('\n', Fila_de_Antendimento_RC.view_next_client())
            elif str(seccao).upper() == 'RP':
                print('\n', Fila_de_Antendimento_RP.view_next_client())
            elif str(seccao).upper() == 'QC':
                print('\n', Fila_de_Antendimento_QC.view_next_client())
        # 4. Eliminar Cliente da *Fila de Atendimento*
        elif value == 4:
            print('\n------------------------ ELIMINAR CLIENTE ------------------------')
            print('Preencha os campos obrigatórios *')
            seccao = input('Introduza a Secção de Atendimento [RC] [RP] [QC] que pretende Atender*: ')
            while str(seccao).upper() not in ('RC', 'RP', 'QC'):
                seccao = input('Introduza a Secção de Atendimento [RC] Criação/Renovação do cartão de cidadão | [RP] '
                               'Criação/Renovação do passaporte | [QC] Questões judiciais *: ')
            posicao = input('Introduza a **Posição** do cliente a ser removido*: ')
            while str.isdigit(posicao) is False:
                posicao = input(' ** Por favor introduza o N.º de Fila do Cliente a remover ** ')
            while int(posicao) <= 0:
                posicao = input(' ** Por favor introduza o N.º maior que 0 ** ')
            if str(seccao).upper() == 'RC':
                if not int(posicao) > len(Fila_de_Antendimento_RC):
                    print('\n', Fila_de_Antendimento_RC.abandon_queue(int(posicao)))
                else:
                    print('O N.º de Posição inserido é *Inválido* ! | A Fila de Atendimento da Secção [RC] tem apenas',
                          len(Fila_de_Antendimento_RC), 'Clientes!')
            elif str(seccao).upper() == 'RP':
                if not int(posicao) > len(Fila_de_Antendimento_RP):
                    print('\n', Fila_de_Antendimento_RP.abandon_queue(int(posicao)))
                else:
                    print('O N.º de Posição inserido é *Inválido* ! | A Fila de Atendimento da Secção [RP] tem apenas',
                          len(Fila_de_Antendimento_RP), 'Clientes!')
            elif str(seccao).upper() == 'QC':
                if not int(posicao) > len(Fila_de_Antendimento_QC):
                    print('\n', Fila_de_Antendimento_QC.abandon_queue(int(posicao)))
                else:
                    print('O N.º de Posição inserido é *Inválido* ! | A Fila de Atendimento da Secção [QC] tem apenas',
                          len(Fila_de_Antendimento_QC), 'Clientes!')
        # 5. Listar Todos os Clientes da *Fila de Atendimento*
        elif value == 5:
            print('\n------------------------ LISTAR CLIENTES ------------------------')
            print('Preencha os campos obrigatórios *')
            seccao = input('Introduza a Secção de Atendimento [RC] [RP] [QC] que pretende listar | '
                           'Pressione [ENTER] para listar todos: ')
            while str(seccao).upper() not in ('RC', 'RP', 'QC', ''):
                seccao = input('Introduza a Secção de Atendimento [RC] Criação/Renovação do cartão de cidadão | [RP] '
                               'Criação/Renovação do passaporte | [QC] Questões judiciais *: ')
            if str(seccao).upper() == 'RC':
                print(Fila_de_Antendimento_RC)
            elif str(seccao).upper() == 'RP':
                print(Fila_de_Antendimento_RP)
            elif str(seccao).upper() == 'QC':
                print(Fila_de_Antendimento_QC)
            elif str(seccao).upper() == '':
                print(Fila_de_Antendimento_RC)
                print(Fila_de_Antendimento_RP)
                print(Fila_de_Antendimento_QC)
        # 6. Número de Clientes na *Fila de Atendimento*
        elif value == 6:
            print('\n------------------------ NÚMERO DE CLIENTES ------------------------')
            print('[RC] ', len(Fila_de_Antendimento_RC), 'Clientes em Espera')
            print('[RP] ', len(Fila_de_Antendimento_RP), 'Clientes em Espera')
            print('[QC] ', len(Fila_de_Antendimento_QC), 'Clientes em Espera')
            total = len(Fila_de_Antendimento_RC) + len(Fila_de_Antendimento_RP) + len(Fila_de_Antendimento_QC)
            print('\nTotal de Clientes em Espera: ', total, 'Clientes')
        # 7. Encerrar o Atendimento (Remover todos os clientes em espera)
        elif value == 7:
            print('\n------------------------ ENCERRAR ATENDIMENTO ------------------------')
            print('Preencha os campos obrigatórios *')
            confirmacao = input('Confirma que quer * Remover todos os Clientes em Espera * [ENTER]:')
            if confirmacao == '':
                print('[RC] ', Fila_de_Antendimento_RC.close())
                print('[RP] ', Fila_de_Antendimento_RP.close())
                print('[QC] ', Fila_de_Antendimento_QC.close())
        # 8. Gerir Pedidos de Atendimento
        elif value == 8:
            print('\n================================= GERIR *ATENDIMENTO* =======================================')
            print('1. Guardar os pedidos de atendimento já inseridos na fila que não puderam ser atendidos.     ')
            print('2. Importar os pedidos de atendimento.                                                       ')
            print('=============================================================================================')
            gerir()
        # 0. Sair do menu
        elif value == 0:
            print('\n~~~~~~~~~~~~~~~ **** *** ** * Menu *Loja do Cidadão* Terminado! * ** *** **** ~~~~~~~~~~~~~~~\n')
            return
        print('=============================================================================================')
        value = input('Bem vind@ à *Loja do Cidadão*! Selecione uma das opções: ')  # de 0 a 8
        # Garantir que o input inserido é um n.º de 0 a 8
        while str.isdigit(value) is False:
            print('\n ** Por favor introduza um número do menu principal! ** ')
            value = input('Bem vind@ à *Loja do Cidadão*! Selecione uma das opções: ')
        value = int(value)
        while value >= 9:
            print('\n           **Erro ao abrir o Menu**             ')
            value = input('Tente de novo! | Menu Principal *Loja do Cidadão* | Selecione uma das opções:')
            if str.isdigit(value):
                value = int(value)
            else:
                while str.isdigit(value) is False:
                    print('           **Erro ao abrir o Menu**             ')
                    value = input('Tente de novo!')
            value = int(value)
        value = int(value)


# EXTRA (+ 18 val)

# EXTRA | Para fazer a opção no *Menu* que permite guardar todos os pedidos de atendimento já inseridos na fila que
# não puderam ser atendidos no horário de atendimento desse dia para um ficheiro de texto abri 3 ficheiros
# correspondetes às 3 secções e criei na T2 o método *save_* que escreve no ficheiro os vários clientes.
def guardar_pedidos():
    ficheiro_RC = open('FdL_Secção[RC].txt', 'w')
    Fila_de_Antendimento_RC.save_(ficheiro_RC)
    ficheiro_RC.close()
    ficheiro_RP = open('FdL_Secção[RP].txt', 'w')
    Fila_de_Antendimento_RP.save_(ficheiro_RP)
    ficheiro_RP.close()
    ficheiro_QC = open('FdL_Secção[QC].txt', 'w')
    Fila_de_Antendimento_QC.save_(ficheiro_QC)
    ficheiro_QC.close()


# EXTRA | Para fazer a opção no *Menu* que permite carregar a informação guardada no ficheiro para a fila no
# arranque do programa, optei por criar um método no T2 *import_* que adiciona os Clientes do ficheiro à Fila na
# Secção correspondente.
def importar_pedidos():
    ficheiro_RC = open('FdL_Secção[RC].txt', 'r')
    Fila_de_Antendimento_RC.import_(ficheiro_RC)
    ficheiro_RC.close()
    ficheiro_RP = open('FdL_Secção[RP].txt', 'r')
    Fila_de_Antendimento_RP.import_(ficheiro_RP)
    ficheiro_RP.close()
    ficheiro_QC = open('FdL_Secção[QC].txt', 'r')
    Fila_de_Antendimento_QC.import_(ficheiro_QC)
    ficheiro_QC.close()


# EXTRA | Criei um "Menu *Gerir Clientes*" a fim de conseguir introduzir à Interface [T3] já criada as opções de
# *guardar_pedidos* e *importar_pedidos*
def gerir():
    valor_ = input('Selecione uma opção do Menu *Gerir Clientes* | Para voltar ao menu inicial introduza 0: ')
    while str.isdigit(valor_) is False:
        print('Por favor introduza um número do Menu *Gerir Clientes*')
        valor_ = input('Bem vind@ ao Menu *Gerir Clientes* | Selecione uma das opções: ')
    valor_ = int(valor_)
    while valor_ >= 3:
        print('           **Erro ao abrir o Menu**             ')
        valor_ = input('Tente de novo! | Menu *Gerir Clientes* | Selecione uma das opções: ')
        if str.isdigit(valor_):
            valor_ = int(valor_)
        else:
            while str.isdigit(valor_) is False:
                print('           **Erro ao abrir o Menu**             ')
                valor_ = input('Tente de novo! |Menu *Gerir Clientes* | Selecione uma das opções: ')
        valor_ = int(valor_)
    valor_ = int(valor_)
    while valor_ != 0:
        # 1. Guardar os pedidos de atendimento
        if valor_ == 1:
            print('\n------------------------------- ** GUARDAR PEDIDOS CLIENTE ** -------------------------------')
            guardar_pedidos()
            print(' ** Pedidos guardados com sucesso! **')
        # 2. Importar para a Fila do dia seguinte
        elif valor_ == 2:
            print('\n---------------------------------- ** IMPORTAR PEDIDOS ** -----------------------------------')
            importar_pedidos()
            print(' ** Pedidos importados com sucesso! **')
        valor_ = input('Selecione uma opção do Menu *Gerir Clientes* | Para voltar ao menu inicial introduza 0: ')
        while str.isdigit(valor_) is False:
            print('Por favor introduza um número do Menu *Gerir Clientes*')
            valor_ = input('Bem vind@ ao Menu *Gerir Clientes* | Selecione uma das opções: ')
        valor_ = int(valor_)
        while valor_ >= 3:
            print('           **Erro ao abrir o Menu**             ')
            valor_ = input('Tente de novo! | Menu *Gerir Clientes* | Selecione uma das opções: ')
            if str.isdigit(valor_):
                valor_ = int(valor_)
            else:
                while str.isdigit(valor_) is False:
                    print('           **Erro ao abrir o Menu**             ')
                    valor_ = input('Tente de novo! |Menu *Gerir Clientes* | Selecione uma das opções: ')
            valor_ = int(valor_)
        valor_ = int(valor_)
    print('~~~~~~~~~~~~~~~~~~~~ *** ** * Menu *Gerir Clientes* Terminado! * ** *** ~~~~~~~~~~~~~~~~~~~~~\n')


# Programa de Teste/Simulação | Clientes já inseridos no sistema *Para Testar*

# Clientes RC
C1 = Cliente('Afonso Guimarães', 10101010, 'RC', False)
C6 = Cliente('Joana Silva', 60606060, 'RC', True)
C7 = Cliente('Isabel Gomes ', 70707070, 'RC', False)
C10 = Cliente('Gustavo Pedro', 100100100, 'RC', True)
# ORDEM DA FILA | Isabel -> Afonso -> Gustavo -> Joana

# Clientes RP
C2 = Cliente('Daniela Monte Real ', 20202020, 'RP', True)
C3 = Cliente('Amilcar Santos', 30303030, 'RP', False)
C8 = Cliente('Gilberto Oliveira', 80808080, 'RP', False)
C11 = Cliente('Débora de Souza', 110110110, 'RP', True)
# ORDEM DA FILA | Gilberto -> Amilcar -> Débora -> Daniela

# Clientes QC
C4 = Cliente('Ana Tereza Vasques ', 40404040, 'QC', False)
C5 = Cliente('Artur Silvestre', 50505050, 'QC', False)
C9 = Cliente('Diogo Morais', 90909090, 'QC', False)
C12 = Cliente('Albertina Silva', 120120120, 'QC', True)
# ORDEM DA FILA | Diogo -> Artur -> Ana -> Albertina

Clientes = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12]
for C in Clientes:
    if C.seccao == 'RC':
        if C.prioridade:
            Fila_de_Antendimento_RC.insert_p_client(C)
        elif not C.prioridade:
            Fila_de_Antendimento_RC.insert_client(C)
    elif C.seccao == 'RP':
        if C.prioridade:
            Fila_de_Antendimento_RP.insert_p_client(C)
        elif not C.prioridade:
            Fila_de_Antendimento_RP.insert_client(C)
    elif C.seccao == 'QC':
        if C.prioridade:
            Fila_de_Antendimento_QC.insert_p_client(C)
        elif not C.prioridade:
            Fila_de_Antendimento_QC.insert_client(C)

menu()  # Abrir o Menu!
