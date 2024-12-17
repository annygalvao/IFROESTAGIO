from abc import ABC


class Usuario(ABC):
    def __init__(self, nome : str, senha : str, area : str, periodo: str):
        self._nome = nome
        self._senha = senha
        self._area = area
        self._periodo = periodo


    # Getters
    def get_nome(self):
        return self._nome

    def get_senha(self):
        return self._senha

    def get_area(self):
        return self._area

    def get_periodo(self):
        return self._periodo

    # Setters
    def set_nome(self, nome):  #adicionarNome
        self._nome = nome

    def set_senha(self, senha): #criarSenha
        self._senha = senha

    def set_area(self, area): #escolherArea
        self._area = area

    def set_periodo(self, periodo): #adicionarperiodo
        self._periodo = periodo

class Aluno(Usuario):
    def __init__(self, nome, senha, area, periodo, diasdisponiveis : str, anoEscolar : int, idade : int, contato : int):
        super().__init__(nome, senha, area, periodo)
        self.diasdisponiveis = diasdisponiveis
        self.anoEscolar = anoEscolar
        self.idade = idade
        self.contato = contato
        #dependencia, aluno depende de um orientador para ser orientado
        self.orientador = None

    def adicionarNomeAluno(self):
        self.set_nome()

    def criarSenha(self):
        self.set_senha()
    
    def escolherArea(self):
        self.set_area()

#Adicionado raise 

    def adicionarPeriodo(self):
        try:
            periodo = input("Escreva o periodo do aluno:"). strip()
            if not periodo:
                raise ValueError(" Esse periodo não pode ser vazio!")
            self. set_periodo(periodo)
        except ValueError as e:
            print(f"Erro ao adicionar periodo: {e}")
        finally:
            print("Adicionar periodo concluido!")

    def adicionarDiasDisponiveis(self,diasAdicionais : str):
        self.diasdisponiveis = self.diasdisponiveis + diasAdicionais

    def get_info(self):
        return self._nome,self._area,self._periodo,self.diasdisponiveis,self.anoEscolar,self.idade,self.contato
    
    # dependencia, aluno depende do orientador para receber nota de seu relatorio
    def enviarRelatorio(self, orientadorNome):
        relatorio = input('''Escreva aqui seu relatório:
''')
        orientadorNome.adicionarRelatorio([self._nome, relatorio])

    # dependencia, aluno depende do DepEx para receber o tutorial
    def solicitarTutorial(self,depex):
        print(f"Solicitando tutoria do DepEx, contato: {depex.contato}")
        result = depex.fornecer_tutoria()
        if result:
            print('''Para não ficar muito cansativo vou ensinar agora como fazer um miojo: ferva 300mls de água em uma panela,
quando estiver fervendo coloque o miojo e espere cozinhar por 3 minutos, retire o miojo do fogão, misture bem e sirva''')
        else:
            print('tutorial não liberado')

    def adicionarOrientador(self, orientador):
        self.orientador= orientador   

class Orientador:
    def __init__(self, nome: str, disciplina: str, contato: int):
        self.nome = nome
        self.disciplina = disciplina
        self.contato = contato
        self.termo = False
        self.relatorios = []

#Raise 

    def assinar_termo(self):
        try:
            choice = input('você concorda em assinar este termo? S ou N')
            if choice.upper() == 'S':
                self.termo = True
                print('Termo assinado.')

            else:
                print('Termo não assinado')

        except Exception as e:
            print(f"Ops, ocorreu um problema ao assinar o termo: {e}")

        if "S" in choice.upper():
            self.termo = True
            print('termo assinado')
        else:
            print('termo não assinado')
    
    def orientar_aluno(self, aluno: Aluno):
        aluno.orientador = self

    def adicionarRelatorio(self,relatorio):
        self.relatorios.append(relatorio)
        print('outro relatório para dar nota')

# adicionado raise

    def avaliar_relatorio(self):
        try:
            avaliar_relatorio = input("Avalie o relatorio do aluno."). strip()
            if not avaliar_relatorio:
                raise ValueError("Avaliação não pode ser vazia!")
            self.set_avaliaar_relatorio(avaliar_relatorio)
        except ValueError as e:
            print(f"Erro ao avaliar relatorio: {e}")
        finally:
            print("Adicionar avaliação concluida!")

        aluno = input('escreva o nome do aluno:')
        

        for relatorio in self.relatorios:
            if aluno in relatorio[0]:
                print(f'relatório do aluno {aluno}: {relatorio[1]}')
                if len(relatorio) == 2:
                    nota = int(input('Dê sua nota para seu relatório de 0 a 100:'))
                    if 0 <= nota <= 100:
                        relatorio.append(nota)
                        return
                    else: 
                        print('nota inválida')
                else:
                    print('Esse relatório já tem nota')
        print('este aluno ainda não fez relatório')
        

class Coordenacao(ABC):
    def __init__(self, setor: str, chefe_do_setor: str):
        self.setor = setor
        self.chefe_do_setor = chefe_do_setor

    def avaliar_plano_de_atividade(self,listaPlano):
        email = input('escreva o email:')

        for plano in listaPlano:
            if email in plano[0]:
                print(f'plano do email {email}: {plano[1]}')
                if len(plano) == 2:
                    nota = int(input('Dê sua nota para seu relatório de 0 a 100:'))
                    plano.append(nota)
                else:
                    print('Esse plano já tem nota')

class DepEx(Coordenacao):
    def __init__(self,setor,chefe_do_setor, contato: int, email: str):
        super().__init__(setor, chefe_do_setor)
        self.contato = contato
        self.email = email
        self.estagiarios = []#objeto do tipo estagiário

    def criar_plano_de_trabalho(self,lista):
        plano = input('''Escreva aqui seu plano:
''')
        lista.append([self.email,plano])

    def fornecer_formulario(self):
        formulario = {
            "Nome Completo": "",
            "Matrícula": "",
            "Curso": "",
            "Período": "",
            "Orientador": "",
            "Assinatura": ""
        }
        print("Formulário fornecido ao aluno. Preencha os campos abaixo:")
        for campo in formulario.keys():
            formulario[campo] = input(f"{campo}: ")
        print("Formulário preenchido com sucesso!")
        return formulario

    def lancar_termo_de_compromisso(self):
        termo = """
        Termo de Compromisso
        ------------------------------------
        Declaro que assumo a responsabilidade de cumprir as atividades
        e normas estabelecidas pelo programa de extensão.
        
        Assinatura: ________________________
        """
        print(termo)
        assinatura = input("Digite seu nome para assinar o termo de compromisso: ")
        if assinatura:
            print(f"Termo de compromisso assinado por {assinatura}.")
        else:
            print("Assinatura não fornecida. Termo não assinado.")

    def fornecer_tutoria(self):
        permissao = input('liberar tutorial para aluno? S ou N')
        if permissao.upper() == 'S':
            return True
        else: 
            return False

class Supervisor:
    def __init__(self, nome: str, contato: int, cargo: str):
        self.nome = nome
        self.contato = contato
        self.cargo = cargo
        self.termo = False

    def supervisionar_aluno(self):
        print('os estagiários estão sendo supervisionados')

    def assinar_termo(self):
        choice = input('você concorda em assinar este termo? S ou N')

        if "S" in choice.upper():
            self.termo = True
            print('termo assinado')
        else:
            print('termo não assinado')
#empresa esta herdando da Classe usuario
class Empresa(Usuario):
    def __init__(self, nome, senha, area, periodo, salario, data_inicial: int, data_final: int, carga_horaria: int, cnpj: int, supervisor_nome, supervisor_contato, supervisor_cargo):
        super().__init__(nome, senha, area, periodo)
        self.salario = salario
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.carga_horaria = carga_horaria
        self.cnpj = cnpj
        # Composição: Empresa cria e "possui" um Supervisor
        self.supervisor = Supervisor(supervisor_nome, supervisor_contato, supervisor_cargo)

    def get_info(self):
        return (f'Empresa: {self._nome}, Área: {self._area}, Período: {self._periodo}, '
                f'Salário Oferecido: {self.salario}, Supervisor: {self.supervisor.nome}')

# Raise
    def criar_senha(self, senha):

        try: 
            senha = input("Digite a senha da empresa:")
            if not senha:
                raise ValueError("Senha não pode ser vazio!")
            self.set_senha(senha)
        except ValueError as e:
            print(f"Erro ao adicionar senha {e}")
        finally:
            print("Tentativa de adicionar senha finalizada!")

    def adicionar_nome(self, nome):
        self.set_nome(nome)
