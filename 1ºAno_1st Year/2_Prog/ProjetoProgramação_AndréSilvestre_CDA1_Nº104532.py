print('=====================================================')
print('               Bem-vind@ ao *LyftIUL*!               ')
print('   Para abrir o *Menu Principal* digite LyftIUL()    ')
print('=====================================================')


# T1 | CLASSE UTILIZADOR
class Utilizador:

    def __init__(self, n_de_estudante, nome, morada='', email='', telemovel=''):
        self.__n_de_estudante = n_de_estudante
        self.nome = nome
        self.morada = morada
        self.email = email
        self.telemovel = telemovel

    # Consultar qualquer um dos atributos
    @property
    def n_de_estudante(self):
        return self.__n_de_estudante

    # Alterar a morada, o email e o telemóvel.
    # Morada --> Concelho e da Freguesia (Sintra, Monte Abraão)
    def alterar_morada(self, nova_morada):
        self.morada = nova_morada
        return self.morada

    def alterar_email(self, novo_email):
        self.email = novo_email
        return self.email

    def alterar_telemovel(self, novo_telemovel):
        self.telemovel = novo_telemovel
        return self.telemovel

    # Converter um utilizador numa string
    def __str__(self):
        return 'Nº de Estudante: ' + str(self.__n_de_estudante) + ' | Nome: ' + str(self.nome) + ' | Morada: ' + str(
            self.morada) + ' | Email: ' + str(self.email) + ' | Telemóvel: ' + str(self.telemovel)


# T1 | CLASSE VIATURA
class Viatura:

    def __init__(self, matricula, n_de_estudante_condutor, descricao, n_de_lugares_sentados, n_de_viagens_efetuadas=0):
        self.matricula = matricula
        self.n_de_estudante_condutor = n_de_estudante_condutor
        self.descricao = descricao
        self.n_de_lugares_sentados = n_de_lugares_sentados
        self.__n_de_viagens_efetuadas = n_de_viagens_efetuadas

    # Consultar qualquer um dos seus atributos
    @property
    def n_de_viagens_efetuadas(self):
        return self.__n_de_viagens_efetuadas

    # Alterar a descrição
    def alterar_descricao(self, nova_descricao):
        self.descricao = nova_descricao
        return self.descricao

    # Médodo que adiciona o valor 1 ao número de viagens efetuadas
    def add_new_trip(self):
        self.__n_de_viagens_efetuadas = self.__n_de_viagens_efetuadas + 1

    # Converter uma viatura numa string
    def __str__(self):
        return 'Matrícula: ' + str(self.matricula) + ' | Nº de Estudante do Condutor: ' + str(
            self.n_de_estudante_condutor) + ' | Descrição da Viatura: ' + str(
            self.descricao) + ' | Nº de Lugares Sentados: ' + str(
            self.n_de_lugares_sentados) + ' | Nº de Viagem Efetuadas ' + str(self.__n_de_viagens_efetuadas)


# Data e Horas
from datetime import time, datetime, timedelta


def get_datetime(t):
    myt = time.fromisoformat(t)
    now = datetime.now()
    mydt = datetime(now.year, now.month, now.day, myt.hour, myt.minute)
    if (mydt - now).days < 0:
        mydt += timedelta(days=1)
    return mydt


# T2 | CLASSE VIAGEM
class Viagem:

    def __init__(self, viatura, h_da_partida, morada, n_maximo_de_boleias):  # h_da_partida --> hh:mm
        self.id_viagem = str(viatura.matricula) + "-" + str(viatura.n_de_viagens_efetuadas + 1)
        self.matricula = viatura.matricula
        self.datetime = get_datetime(h_da_partida)
        self.morada = morada
        self.n_maximo_de_boleias = n_maximo_de_boleias
        self.lista_de_passageiros = []

    @property
    def ativa(self):
        data_da_partida = self.datetime
        data_atual = datetime.now()
        if data_da_partida > data_atual:
            return True
        else:
            return False

    @property
    def boleias_disponiveis(self):
        return self.n_maximo_de_boleias - len(self.lista_de_passageiros)

    def aceita_passageiro(self):
        if self.boleias_disponiveis > 0:
            return True
        else:
            return False

    def adicionar_passageiro(self, n_de_estudante):
        if self.boleias_disponiveis > 0:
            self.lista_de_passageiros.append(n_de_estudante)
            print('Adicionad@ à viagem com sucesso!!')
        elif self.boleias_disponiveis == 0:
            print('A viatura já perfez o Nº Máximo de Boleias!')

    def __str__(self):
        return 'ID da viagem: ' + str(self.id_viagem) + ' | Matrícula: ' + str(
            self.matricula) + ' | Data e Hora da viagem: ' + str(
            self.datetime) + ' | Morada: ' + str(
            self.morada) + ' | Nº de Máximo de Boleias: ' + str(
            self.n_maximo_de_boleias) + ' | Lista de passageiros ' + str(self.lista_de_passageiros)


# T3 | CLASSE GESTOR
class Gestor:

    def __init__(self):
        self.lista_de_utilizadores = []
        self.lista_de_viaturas = []
        self.lista_de_viagens = []
        self.lista_de_viagens_ida = []
        self.lista_de_viagens_volta = []

    # GESTOR DE UTILIZADORES
    # Verifica se o estudante existe na lista de Users através do número de estudante
    def exists_user(self, n_de_estudante):
        for n in self.lista_de_utilizadores:
            if n.n_de_estudante == n_de_estudante:
                return True
        return False

    # Adicionar um novo estudante ao sistema. Verificar se já existe.
    def add_user(self, n):
        if isinstance(n, Utilizador):
            for u in self.lista_de_utilizadores:
                if u.n_de_estudante == n.n_de_estudante:
                    return 'Este utilizador já foi registado!'
            return self.lista_de_utilizadores.append(n)
        return False

    # Listar os utilizadores existentes
    def list_users(self):
        for u in self.lista_de_utilizadores:
            print(u)

    # GESTOR DE VIATURAS
    # Verificar se existe uma viatura dando a matrícula
    def exists_viatura(self, matricula):
        for v in self.lista_de_viaturas:
            if v.matricula == matricula:
                return True
        return False

    # Adicionar uma nova viatura
    def add_viatura(self, n):
        if isinstance(n, Viatura):
            for v in self.lista_de_viaturas:
                if v.matricula == n.matricula:
                    return str('A *Viatura* já está foi registada!')
            return self.lista_de_viaturas.append(n)
        return False

    # Listar as viaturas
    def list_viaturas(self):
        for v in self.lista_de_viaturas:
            print(v)

    # GESTOR DE VIAGENS
    # Listar todas as viagens registadas no sistema;
    def listar_viagens(self):
        for v in self.lista_de_viagens:
            print(v)

    # Listar todas as viagens agendadas, de ou para, uma determinada morada;
    def listar_viagens_morada(self):
        morada_ = input('Digite a sua *Morada* [Concelho, Freguesia // Distrito, Cidade] --> p.e.: (Sintra, '
                        'Monte Abraão): ')
        print('Viagens agendadas para a *Morada* digitada: ')
        for v in self.lista_de_viagens:
            if morada_ == v.morada:
                print(v)

    # Criar uma nova viagem, dado o número do estudante condutor;
    # Viagem --> id_viagem | matricula | h_da_partida | morada | n_maximo_de_boleias
    def adicionar_viagem(self):
        print('Preencha os campos obrigatórios (*)')
        n_de_estudante_condutor = input('Digite o Nº de Estudante do Condutor*: ')
        while str.isdigit(n_de_estudante_condutor) is False:
            print('-------------------------------')
            n_de_estudante_condutor = input('Digite o Nº de Estudante do Condutor*: ')
        n_de_estudante_condutor = int(n_de_estudante_condutor)
        for u in self.lista_de_utilizadores:
            if u.n_de_estudante == n_de_estudante_condutor:
                estudante = u
        for v in self.lista_de_viaturas:
            if v.n_de_estudante_condutor == n_de_estudante_condutor:
                veiculo_do_estudante = v
        tipo_de_viagem = input(
            'Introduza o Tipo de Viagem [Ida para o ISCTE (Digite 1) // Regresso do ISCTE (Digite 2)]*: ')
        hora_de_partida = input('Introduza a Hora e os Minutos da Viagem [hh:mm]*: ')
        n_de_lugares_disponivel = input('Introduza o Nº de Lugares Disponível para Boleia (Se o número de lugares '
                                        'não for indicado, assume-se o nº Lugares da Viatura - 1): ')
        if n_de_lugares_disponivel == '':
            n_de_lugares_disponivel = veiculo_do_estudante.n_de_lugares_sentados - 1
        morada = input('Introduza a sua Morada [Concelho, Freguesia // Distrito, Cidade] --> p.e.: (Sintra, '
                       'Monte Abraão) (Caso não preencha assume-se que a morada é a que está definida no perfil do '
                       'condutor!): ')
        if morada == '':
            morada = estudante.morada
            if morada == '':
                print('*** Ainda não tem nenhuma morada associada ao perfil!! ***')
                morada = input('Introduza a sua morada [Concelho e da Freguesia --> p.e.: (Sintra, Monte Abraão)]: ')
        n = Viagem(veiculo_do_estudante, hora_de_partida, morada, n_de_lugares_disponivel)
        if tipo_de_viagem == str(1):
            self.lista_de_viagens_ida.append(n)
        elif tipo_de_viagem == str(2):
            self.lista_de_viagens_volta.append(n)
        print('-------------------------------------------------------------------------------------------')
        print(' ***** Registo da *Viagem* efetuado com sucesso! Obrigado por utilizar a *LyftIUL*!! *****')
        print(n)
        n.viatura.add_new_trip()
        self.lista_de_viagens.append(n)

    # Inscrever um passageiro numa viagem, dado o seu número de estudante e o ID da viagem;
    def inscrever_passageiro(self):
        n_de_estudante = input('Digite o seu Nº de Estudante: ')
        id_viagem_para_adicionar = input('Digite o ID da Viagem a que se pretende inscrever: ')
        for i in self.lista_de_viagens:
            if i.id_viagem == id_viagem_para_adicionar:
                i.adicionar_passageiro(int(n_de_estudante))
                print(i)

    # Registar e remover todas as viagens já concluídas, tendo em conta a hora atual.; (v_i --> Viagem Inativa)
    def limpar_concluidas(self):
        lista_de_viagens_nao_ativas = []
        for v in self.lista_de_viagens:
            if v.datetime < datetime.now():
                lista_de_viagens_nao_ativas.append(v)
                for v_i in lista_de_viagens_nao_ativas:
                    self.lista_de_viagens.remove(v_i)
                    for v_ida in self.lista_de_viagens_ida:
                        if v_i == v_ida:
                            self.lista_de_viagens_ida.remove(v_i)
                    for v_volta in self.lista_de_viagens_volta:
                        if v_i == v_volta:
                            self.lista_de_viagens_volta.remove(v_i)
        f = open('historico.txt', 'a')
        for i in lista_de_viagens_nao_ativas:
            f.write('{};{};{};{};{};{}'.format(i.id_viagem, i.matricula, i.datetime, i.morada,
                                               i.n_maximo_de_boleias, i.lista_de_passageiros) + '\n')
        f.close()

    # ESTATÍSTICAS
    # Número de utilizadores registados na plataforma
    def n_users(self):
        print('Número de *Utilizadores* registados na plataforma: ' + str(len(self.lista_de_utilizadores)))

    # Número de viaturas registadas no sistema
    def n_viaturas(self):
        print('Número de *Viaturas* registadas na plataforma: ' + str(len(self.lista_de_viaturas)))

    # Número de viagens ativas, separando por viagens de ida e de regresso do Iscte
    def n_viagens(self):
        total_ida = len(self.lista_de_viagens_ida)
        total_volta = len(self.lista_de_viagens_volta)
        print('Nº de viagens ativas de *IDA*: ' + str(total_ida) + ' |  Nº de viagens ativas de *VOLTA*: ' + str(
            total_volta))

    # Soma do número de viagens realizadas por viaturas registadas na plataforma
    def soma_de_viagens(self):
        f = open('historico.txt', 'r')
        line_count = 0
        for line in f:
            if line != "\n":
                line_count += 1
        n_total_de_viagens = line_count
        f.close()
        print('Número total de *Viagens* registadas na plataforma: ' + str(n_total_de_viagens) + ' Viagens.')

    # TOP 5 viaturas com mais viagens
    def top5(self):
        import numpy
        top5 = sorted(numpy.array(self.lista_de_viaturas), key=lambda Viatura: Viatura.n_de_viagens_efetuadas,
                      reverse=True)
        # PESQUISA QUE FIZ DO MÉTODO ** SORTED() **
        # Fonte: https://www.programiz.com/python-programming/methods/built-in/sorted
        # numpy.array(self.lista_de_viaturas) ----> ITERÁVEL :serve como 'ITERADOR' e cria um vetor com as viaturas
        # key=lambda Viatura: Viatura.n_de_viagens_efetuadas ----> CHAVE: uma função que serve como chave para a
        # comparação de classificação
        # reverse=True ---> REVERSO: Por defeito esta função vem por ordem Crescende e TOP5 <=> Ordem Decrescente -->
        # Reverso tem de estar ativo!
        top5 = top5[:5]
        r = 1  # Posição/Rank
        for i in top5:
            print(str(r) + 'º-> Viatura: ' + str(i.matricula) + ' com um total de ' + str(
               i.n_de_viagens_efetuadas) + ' Viagens')
            r += 1


g = Gestor()


# T4 | LyftIUL
# UTILIZADORES (n_de_estudante, nome, morada, email, telemovel) --> EXTRA FUNÇÕES
def criar_utilizador():
    print('Preencha os campos obrigatórios *')
    print('Os restantes pode pressionar Enter para prosseguir!')
    n_de_estudante = input('Introduza um nº de estudante*: ')
    for i in g.lista_de_utilizadores:
        while i.n_de_estudante == n_de_estudante:
            print('Atenção! Já existe este número associado a um estudante! Tente de novo!')
            n_de_estudante = input('Introduza um nº de estudante do : ')
    nome = input('Introduza o seu nome*: ')
    morada = input('Introduza a sua morada [Concelho, Freguesia // Distrito, Cidade] --> p.e.: (Sintra, '
                   'Monte Abraão): ')
    email = input('Introduza o seu email: ')
    telemovel = input('Introduza o seu telemóvel: ')
    novo_user = Utilizador(n_de_estudante, nome, morada, email, telemovel)
    g.lista_de_utilizadores.append(novo_user)
    print('Registo efetuado com sucesso! Bem-vind@ ao LyftIUL!!')
    return novo_user


# VIATURAS (matricula, n_de_estudante_condutor, descricao, n_de_lugares_sentados, n_de_viagens_efetuadas) --> EXTRA
def criar_viatura():
    print('Preencha os campos todos!*')
    matricula = input('Digite a Matrícula da viatura: ')
    for i in g.lista_de_viagens:
        while matricula == i.matricula:
            matricula = input('Matrícula já registada! Digite uma matrícula ainda não registada!: ')
    n_de_estudante_condutor = input('Digite o Nº de Estudante do Condutor: ')
    descricao = input('Digite a Descrição da Viatura (Marca, Modelo, Cor --> [p.e. Tesla Model 3 Azul ]: ')
    n_de_lugares_sentados = input('Digite o Nº de Lugares Sentados: ')
    n_de_viagens_efetuadas = 0
    nova_viatura = Viatura(matricula, n_de_estudante_condutor, descricao, n_de_lugares_sentados, n_de_viagens_efetuadas)
    g.lista_de_viaturas.append(nova_viatura)
    print('Registo da viatura efetuado com sucesso!')
    return nova_viatura


# T4 | LyftIUL
# Programa que, com base num objeto da classe Gestor, faça a gestão da plataforma.
def LyftIUL():
    print('================== MENU PRINCIPAL *LyftIUL* ====================')
    print('1. Listar Utilizadores')
    print('2. Listar Viaturas')
    print('3. Listar Viagens Agendadas')
    print('4. Listar Viagens Agendadas com filtro por Morada')
    print('5. Registar Viagem')
    print('6. Inscrever Passageiro em Viagem')
    print('7. Registar e Remover as Viagens Concluídas')
    print('8. Informações do Sistema [Estatísticas]')
    print('9. Actividade por Hora do Dia')
    print('10. É novo na aplicação? Registe-se já na *LyftIUL*!')
    print('11. Adicionar uma Viatura à *LyftIUL*')
    print('0. Sair do menu')
    print('=================================================================')
    value = input('Bem vind@ à LyftIUL! Selecione uma das opções: ')
    while str.isdigit(value) is False:
        print('================================================================')
        print(' ** Por favor introduza um número do menu principal! ** ')
        value = input('Bem vind@ à LyftIUL! Selecione uma das opções: ')
    value = int(value)
    while value >= 13:
        print('================================================================')
        print('           **Erro ao abrir o Menu**             ')
        value = input('Tente de novo! | Menu Principal *LyftIUL* | Selecione uma das opções:')
        print('================================================================')
        if str.isdigit(value):
            value = int(value)
        else:
            while str.isdigit(value) is False:
                print('           **Erro ao abrir o Menu**             ')
                value = input('Tente de novo!')
        value = int(value)
    value = int(value)
    while value != 0 and 0 <= value < 13:
        # 1. Listar Utilizadores
        if value == 1:
            print('=====================================')
            print('         LISTAR UTILIZADORES         ')
            print('=====================================')
            g.list_users()
        # 2. Listar Viaturas
        elif value == 2:
            print('=====================================')
            print('           LISTAR VIATURAS           ')
            print('=====================================')
            g.list_viaturas()
        # 3. Listar Viagens Agendadas
        elif value == 3:
            print('=====================================')
            print('      LISTAR VIAGENS AGENDADAS       ')
            print('=====================================')
            g.listar_viagens()
        # 4. Listar viagens agendadas com filtro por morada
        elif value == 4:
            print('============================================================')
            print('      LISTAR VIAGENS AGENDADAS (FILTRADO PELA MORADA)       ')
            print('============================================================')
            g.listar_viagens_morada()
        # 5. Registar viagem
        elif value == 5:
            print('====================== REGISTAR VIAGEM ======================')
            g.adicionar_viagem()
        # 6. Inscrever passageiro em viagem
        elif value == 6:
            print('=====================================')
            print('        INSCREVER PASSAGEIRO         ')
            print('=====================================')
            g.inscrever_passageiro()
        # 7. Registar e remover as viagens concluídas
        elif value == 7:
            print('=====================================')
            print('      R.R. VIAGENS CONCLUIDAS        ')
            print('=====================================')
            g.limpar_concluidas()
            print(' ** Registo e remoção das viagens concluídas realizado com sucesso!! **')
        # 8. Informações do sistema
        elif value == 8:
            print('==================================== MENU *ESTATÍSTICA* ====================================')
            print('1. Número de utilizadores registados na plataforma.')
            print('2. Número de viaturas registadas na plataforma.')
            print('3. Número de viagens ativas, separando por viagens de ida e de regresso do ISCTE.')
            print('4. Soma do número de viagens realizadas por viaturas registadas na plataforma.')
            print('5. TOP 5 viaturas que realizaram mais viagens.')
            print('===========================================================================================')
            menu_estatistica()
        # 9. Atividade por hora do dia
        elif value == 9:
            print('===================== MENU *ATIVIDADE* =====================')
            print('1. Média de viagens por hora.')
            print('2. Hora do dia com maior número de boleias.')
            print('3. Proporção de viagens ocorridas na parte da manhã.')
            print('4. Ver gráfico que ilustra a atividade por hora.')
            print('5. Ver a matriz que representa a atividade por hora.')
            print('============================================================')
            menu_atividade()
        # 10. É novo na aplicação? Registe-se já na *LyftIUL*!
        elif value == 10:
            print('=====================================')
            print('    REGISTAR UM NOVO UTILIZADOR      ')
            print('=====================================')
            criar_utilizador()
        # 11. Adicionar uma viatura à *LyftIUL*.
        elif value == 11:
            print('=====================================')
            print('      REGISTAR UMA NOVA VIATURA      ')
            print('=====================================')
            criar_viatura()
        # 0. Sair do menu.
        elif value == 0:
            print(' =========== SAIR DO MENU ===========')
            return
        print('================================================================')
        value = input('Bem vind@ à LyftIUL! Selecione outra opção: ')
        while str.isdigit(value) is False:
            print('================================================================')
            print('Por favor introduza um número do menu principal')
            value = input('Bem vind@ à LyftIUL! Selecione uma das opções: ')
        value = int(value)
        while value >= 13:
            print('================================================================')
            print('           **Erro ao abrir o Menu**             ')
            value = input('Tente de novo!')
            print('================================================================')
            if str.isdigit(value):
                value = int(value)
            else:
                while str.isdigit(value) is False:
                    print('           **Erro ao abrir o Menu**             ')
                    value = input('Tente de novo!')
            value = int(value)
        value = int(value)
    print('=========== SAIU DO MENU ===========')


# Menu aberto quando se escolhe a opção 8
def menu_estatistica():
    valor = input('Introduza o número da opção a executar: ')
    while str.isdigit(valor) is False:
        print('Por favor introduza um número do *Menu Estatística*')
        valor = input('Bem vind@ à LyftIUL *Menu Estatística* | Selecione uma das opções: ')
    valor = int(valor)
    while valor >= 6:
        print('           **Erro ao abrir o Menu**             ')
        valor = input('Tente de novo! | *Menu Estatística* | Selecione uma das opções: ')
        if str.isdigit(valor):
            valor = int(valor)
        else:
            while str.isdigit(valor) is False:
                print('           **Erro ao abrir o Menu**             ')
                valor = input('Tente de novo! | *Menu Estatística* | Selecione uma das opções: ')
        valor = int(valor)
    valor = int(valor)
    while valor != 0:
        print('=================== MENU *ESTATÍSTICA* ====================')
        # 1. Número de utilizadores registados na plataforma.
        if valor == 1:
            print('=================================================')
            print(' NÚMERO DE UTILIZADORES REGISTADAS NA PLATAFORMA ')
            print('=================================================')
            g.n_users()
        # 2. Número de viaturas registadas na plataforma.
        elif valor == 2:
            print('=================================================')
            print('   NÚMERO DE VIATURAS REGISTADAS NA PLATAFORMA   ')
            print('=================================================')
            g.n_viaturas()
        # 3. Número de viagens ativas, separando por viagens de ida e de regresso do Iscte.
        elif valor == 3:
            print('=====================================')
            print('       NÚMERO DE VIAGENS ATIVAS      ')
            print('=====================================')
            g.n_viagens()
        # 4. Soma do número de viagens realizadas por viaturas registadas na plataforma.
        elif valor == 4:
            print('=====================================')
            print('    Nº TOTAL DE VIAGENS *LyftIUL*    ')
            print('=====================================')
            g.soma_de_viagens()
        # 5. TOP 5 viaturas que realizaram mais viagens.
        elif valor == 5:
            print('=====================================')
            print('   TOP 5 VIATURAS COM MAIS VIAGENS   ')
            print('=====================================')
            g.top5()
        print('==================================== MENU *ESTATÍSTICA* ====================================')
        print('1. Número de utilizadores registados na plataforma.')
        print('2. Número de viaturas registadas na plataforma.')
        print('3. Número de viagens ativas, separando por viagens de ida e de regresso do ISCTE.')
        print('4. Soma do número de viagens realizadas por viaturas registadas na plataforma.')
        print('5. TOP 5 viaturas que realizaram mais viagens.')
        print('==========================================================================================')
        valor = input('Selecione uma opção do *Menu Estatítica* | Para voltar ao menu inicial introduza 0: ')
        while str.isdigit(valor) is False:
            print('Por favor introduza um número do *Menu Estatística*')
            valor = input('Bem vind@ à LyftIUL *Menu Estatística* ! Selecione uma das opções: ')
        valor = int(valor)
        while valor >= 6:
            print('               **Erro ao abrir o Menu**               ')
            valor = input('Tente de novo! | *Menu Estatística* | Selecione uma das opções: ')
            if str.isdigit(valor):
                valor = int(valor)
            else:
                while str.isdigit(valor) is False:
                    print('               **Erro ao abrir o Menu**               ')
                    valor = input('Tente de novo! | *Menu Estatística* | Selecione uma das opções: ')
            valor = int(valor)
        valor = int(valor)
    print(' ***** Menu *Estatística* Terminado! ***** ')


import numpy as np
import matplotlib.pyplot as plt


# T5 | ATIVIDADE
class Atividade:

    # Criar uma matriz 24(número de horas de um dia) x 2 (número de viagens | número de boleias)
    def matriz(self):
        matrix = np.zeros([24, 2], int)
        f = open('historico.txt', 'r')
        line = f.readline().strip()
        while line != '':
            line_ = line.split(';')
            hora_data = line_[2]
            hora_ = hora_data[hora_data.find(' '):]
            hora = hora_[1:3]
            n_de_passageiros = 0
            if line_[5] != '[]':
                lista_de_passageiros = line_[5].split(',')
                n_de_passageiros = len(lista_de_passageiros)
            matrix[int(hora), 0] += 1
            matrix[int(hora), 1] += n_de_passageiros
            line = f.readline().strip()
        f.close()
        return matrix

    # a) Média de viagens por hora (para ver só a coluna do nº de viagens --> m[:,:1] )
    def media_de_viagens_por_hora(self):
        matrix = self.matriz()
        m = matrix[:, :1]
        media = np.mean(m, axis=0)  # pesquisei na biblioteca numpy
        print('Média de viagens por hora: ' + str(media) + ' viagens.')

    # b) Hora do dia com maior número de boleias (para ver só a coluna do nº de boleias --> m[:,1:] )
    def hora_do_dia_com_maior_numero_de_boleias(self):
        matrix = self.matriz()
        hora_max = matrix[:, 1:].argmax()
        n_boleias_max = matrix[:, 1:].max()
        print('Hora do dia com Maior Nº de Boleias: ' + str(hora_max) + ':00-' + str(
            hora_max) + ':59' + ', com um máximo de ' + str(n_boleias_max) + " boleias!!")

    # c) Proporção de viagens ocorridas da parte da manhã (00:00 - 11:59).
    def proporcao_de_viagens_ocorridas_da_parte_da_manha(self):
        matrix = self.matriz()
        total_viagens = matrix[:, :1].sum()
        total_manha = matrix[:12, :1].sum()
        proporcao = total_manha / total_viagens * 100
        print('Proporção de viagens ocorridas no período da manhã (00:00 - 11:59): ' + str(proporcao) + '% das '
                                                                                                        'viagens!!')

    # Gráfico ( x --> Nº de Boleias | y--> Nº de Viagens )
    def mostrar_grafico(self):
        matrix = self.matriz()
        plt.plot(matrix)
        # PESQUISA QUE FIZ ACERCA DA BILIOTECA matplotlib.pyplot
        # Fonte: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
        bars = ('0:00', '', '', '', '', '', '', '', '', '', '', '', '12:00', '', '', '', '', '', '', '', '', '', '', '',
                '24:00')
        x_pos = np.arange(len(bars))
        plt.xticks(x_pos, bars)
        plt.title('Atividade por Hora do Dia')
        plt.xlabel('Hora do dia')
        plt.ylabel('Nº de Boleias (Laranja) | Nº de Viagens (Azul)')
        plt.show()

    # Print da Matriz
    def mostrar_matriz(self):
        print(self.matriz())


a = Atividade()


# Menu *Atividade*
def menu_atividade():
    a.matriz()
    valor_ = input('Selecione uma opção do *Menu Atividade* | Para voltar ao menu inicial introduza 0: ')
    while str.isdigit(valor_) is False:
        print('Por favor introduza um número do *Menu Atividade*')
        valor_ = input('Bem vind@ à *LyftIUL* | *Menu Atividade* | Selecione uma das opções: ')
    valor_ = int(valor_)
    while valor_ >= 6:
        print('           **Erro ao abrir o Menu**             ')
        valor_ = input('Tente de novo! | *Menu Atividade* | Selecione uma das opções: ')
        if str.isdigit(valor_):
            valor_ = int(valor_)
        else:
            while str.isdigit(valor_) is False:
                print('           **Erro ao abrir o Menu**             ')
                valor_ = input('Tente de novo! | *Menu Atividade* | Selecione uma das opções: ')
        valor_ = int(valor_)
    valor_ = int(valor_)
    while valor_ != 0:
        # 1. Média de viagens por hora.
        if valor_ == 1:
            print('=====================================')
            print('      MÉDIA DE VIAGENS POR HORA      ')
            print('=====================================')
            a.media_de_viagens_por_hora()
        # 2. Hora do dia com maior número de boleias.
        elif valor_ == 2:
            print('=============================================')
            print('   HORA DO DIA COM MAIOR NÚMERO DE BOLEIAS   ')
            print('=============================================')
            a.hora_do_dia_com_maior_numero_de_boleias()
        # 3. Proporção de viagens ocorridas da parte da manhã.
        elif valor_ == 3:
            print('=========================================')
            print('      PROPORÇÃO DE VIAGENS DE MANHÃ      ')
            print('=========================================')
            a.proporcao_de_viagens_ocorridas_da_parte_da_manha()
        # 4. Ver gráfico que ilustra a atividade por hora.
        elif valor_ == 4:
            print('==================================================')
            print('     GRÁFICO QUE ILUSTRA A ATIVIDADE POR HORA     ')
            print('==================================================')
            a.mostrar_grafico()
        # 5. Ver a matriz que representa a atividade por hora.
        elif valor_ == 5:
            print('==================================================')
            print('      MATRIZ QUE ILUSTRA A ATIVIDADE POR HORA     ')
            print('==================================================')
            a.mostrar_matriz()
            print('===================== MENU *ATIVIDADE* =====================')
            print('1. Média de viagens por hora.')
            print('2. Hora do dia com maior número de boleias.')
            print('3. Proporção de viagens ocorridas na parte da manhã.')
            print('4. Ver gráfico que ilustra a atividade por hora.')
            print('5. Ver a matriz que representa a atividade por hora.')
            print('============================================================')
        valor_ = input('Selecione uma opção do *Menu Atividade* | Introduza 0 para fechar este menu: ')
        while str.isdigit(valor_) is False:
            print('Por favor introduza um número do *Menu Atividade*')
            valor_ = input('Bem vind@ à *LyftIUL* | *Menu Atividade* ! Selecione uma das opções: ')
        valor_ = int(valor_)
        while valor_ >= 6:
            print('           **Erro ao abrir o Menu**             ')
            valor_ = input('Tente de novo! | *Menu Atividade* | Selecione uma das opções: ')
            if str.isdigit(valor_):
                valor_ = int(valor_)
            else:
                while str.isdigit(valor_) is False:
                    print('           **Erro ao abrir o Menu**             ')
                    valor_ = input('Tente de novo! |  *Menu Atividade* | Selecione uma das opções: ')
            valor_ = int(valor_)
        valor_ = int(valor_)
    print(' ***** Menu da *Atividade* Terminado! ***** ')


# UTILIZADORES JÁ REGISTADOS NO SISTEMA
U1 = Utilizador(101010, 'Tiago', 'Lisboa, Entrecampos', 'tiago@gmail.com', '917845612')
U2 = Utilizador(202020, 'Joana', 'Sintra, Monte Abraão', '', '912021234')
U3 = Utilizador(303030, 'António', 'Lisboa, Torres Vedras')
U4 = Utilizador(404040, 'Maria', 'Lisboa, Cascais')
U5 = Utilizador(505050, 'Daniela', 'Lisboa, Mafra', 'daniela@gmail.com', '912345678')
U6 = Utilizador(606060, 'Manuel', 'Lisboa, Sete Rios', 'manuel@gamil.com')
U7 = Utilizador(707070, 'Simão', 'Lisboa, Torres Vedras', '')
U8 = Utilizador(808080, 'Sofia', 'Lisboa, Entrecampos', '', '930123456')
U9 = Utilizador(909090, 'Margarida', 'Lisboa, Parque da Nações', '', '920789456')
U10 = Utilizador(100100100, 'Madalena', 'Setúbal, Barreiro')

g.add_user(U1)
g.add_user(U2)
g.add_user(U3)
g.add_user(U4)
g.add_user(U5)
g.add_user(U6)
g.add_user(U7)
g.add_user(U8)
g.add_user(U9)
g.add_user(U10)

# VIATURAS JÁ REGISTADAS NO SISTEMA
V1 = Viatura('11-AA-11', 101010, 'Tesla Model 3 Azul', 5, )
V2 = Viatura('22-BB-22', 202020, 'Toyota Aygo Cinzento', 4, 15)
V3 = Viatura('33-CC-33', 303030, 'Mazda MX-5 Vermelho', 3, 10)
V4 = Viatura('44-DD-44', 404040, 'Renault Clio Preto', 4, 5)
V5 = Viatura('55-EE-55', 505050, 'Opel Corsa Preto', 5, 10)
V6 = Viatura('66-FF-66', 606060, 'Renault Clio Vermelho', 3, 2)
V7 = Viatura('77-GG-77', 707070, 'Tesla Model S Branco', 4, 17)
V8 = Viatura('88-HH-88', 808080, 'Mercedes GLE Cizento', 5, 5)
V9 = Viatura('99-II-99', 909090, 'Porshe Cayenne Preto', 5, )
V10 = Viatura('100-JJ-100', 100100100, 'Honda Type-R Platinado', 5, 7)

g.add_viatura(V1)
g.add_viatura(V2)
g.add_viatura(V3)
g.add_viatura(V4)
g.add_viatura(V5)
g.add_viatura(V6)
g.add_viatura(V7)
g.add_viatura(V8)
g.add_viatura(V9)
g.add_viatura(V10)

LyftIUL()
