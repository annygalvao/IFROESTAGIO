#exceção 
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Usuario(ABC):
    def __init__(self, nome: str, senha: str, area: str, periodo: str):
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
    def set_nome(self, nome):  # adicionarNome
        self._nome = nome

    def set_senha(self, senha):  # criarSenha
        self._senha = senha

    def set_area(self, area):  # escolherArea
        self._area = area

    def set_periodo(self, periodo):  # adicionarperiodo
        self._periodo = periodo


class Aluno(Usuario):
    def __init__(self, nome, senha, area, periodo, diasdisponiveis: str, anoEscolar: int, idade: int, contato: int):
        super().__init__(nome, senha, area, periodo)
        self.diasdisponiveis = diasdisponiveis
        self.anoEscolar = anoEscolar
        self.idade = idade
        self.contato = contato
        self.orientador = None

    #método com exceção
    def adicionarNomeAluno(self):
        try:
            nome = input("Digite o nome do aluno: ").strip()
            if not nome:
                raise InvalidInputError("Nome não pode ser vazio!")
            self.set_nome(nome)
        except InvalidInputError as e:
            print(f"Erro: {e}")
        finally:
            print("Tentativa de adicionar nome finalizada.")

    def criarSenha(self):
        try:
            senha = input("Digite a senha: ").strip()
            if not senha:
                raise InvalidInputError("Senha não pode ser vazia!")
            self.set_senha(senha)
        except InvalidInputError as e:
            print(f"Erro: {e}")
        finally:
            print("Tentativa de criar senha finalizada.")

    def escolherArea(self):
        try:
            area = input("Escolha a área de atuação: ").strip()
            if not area:
                raise InvalidInputError("Área não pode ser vazia!")
            self.set_area(area)
        except InvalidInputError as e:
            print(f"Erro: {e}")
        finally:
            print("Tentativa de escolher área finalizada.")

    def adicionarOrientador(self, orientador):
        self.orientador = orientador

    def get_info(self):
        return self._nome, self._area, self._periodo, self.diasdisponiveis, self.anoEscolar, self.idade, self.contato


class Orientador:
    def __init__(self, nome: str, disciplina: str, contato: int):
        self.nome = nome
        self.disciplina = disciplina
        self.contato = contato
        self.termo = False
        self.relatorios = []

    def assinar_termo(self):
        try:
            choice = input('Você concorda em assinar este termo? S ou N: ')
            if choice.upper() == 'S':
                self.termo = True
                print('Termo assinado.')
            else:
                print('Termo não assinado.')
        except Exception as e:
            print(f"Erro ao assinar o termo: {e}")

    def adicionarRelatorio(self, relatorio):
        try:
            self.relatorios.append(relatorio)
            print('Relatório adicionado.')
        except Exception as e:
            print(f"Erro ao adicionar relatório: {e}")

    def avaliar_relatorio(self):
        try:
            aluno = input('Escreva o nome do aluno: ')
            for relatorio in self.relatorios:
                if aluno in relatorio[0]:
                    print(f'Relatório do aluno {aluno}: {relatorio[1]}')
                    if len(relatorio) == 2:
                        nota = int(input('Dê sua nota para o relatório de 0 a 100: '))
                        if 0 <= nota <= 100:
                            relatorio.append(nota)
                            print(f'Nota dada: {nota}')
                            return
                        else:
                            print('Nota inválida.')
                    else:
                        print('Esse relatório já tem nota.')
            print('Este aluno ainda não fez relatório.')
        except Exception as e:
            print(f"Erro ao avaliar relatório: {e}")


class Coordenacao(ABC):
    def __init__(self, setor: str, chefe_do_setor: str):
        self.setor = setor
        self.chefe_do_setor = chefe_do_setor

    def avaliar_plano_de_atividade(self, listaPlano):
        try:
            email = input('Escreva o email: ')
            for plano in listaPlano:
                if email in plano[0]:
                    print(f'Plano do email {email}: {plano[1]}')
                    if len(plano) == 2:
                        nota = int(input('Dê sua nota para o plano de 0 a 100: '))
                        plano.append(nota)
                    else:
                        print('Esse plano já tem nota.')
        except Exception as e:
            print(f"Erro ao avaliar plano de atividade: {e}")


class DepEx(Coordenacao):
    def __init__(self, setor, chefe_do_setor, contato: int, email: str):
        super().__init__(setor, chefe_do_setor)
        self.contato = contato
        self.email = email
        self.estagiarios = []  # Objeto do tipo estagiário

    def criar_plano_de_trabalho(self, lista):
        try:
            plano = input('Escreva aqui seu plano: ')
            lista.append([self.email, plano])
        except Exception as e:
            print(f"Erro ao criar plano de trabalho: {e}")

    def fornecer_formulario(self):
        try:
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
        except Exception as e:
            print(f"Erro ao fornecer formulário: {e}")

    def lancar_termo_de_compromisso(self):
        try:
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
        except Exception as e:
            print(f"Erro ao lançar termo de compromisso: {e}")

    def fornecer_tutoria(self):
        try:
            permissao = input('Liberar tutorial para aluno? S ou N: ')
            if permissao.upper() == 'S':
                return True
            else:
                return False
        except Exception as e:
            print(f"Erro ao fornecer tutoria: {e}")


class Supervisor:
    def __init__(self, nome: str, contato: int, cargo: str):
        self.nome = nome
        self.contato = contato
        self.cargo = cargo
        self.termo = False

    def supervisionar_aluno(self):
        print('Os estagiários estão sendo supervisionados.')

    def assinar_termo(self):
        try:
            choice = input('Você concorda em assinar este termo? S ou N: ')
            if choice.upper() == 'S':
                self.termo = True
                print('Termo assinado.')
            else:
                print('Termo não assinado.')
        except Exception as e:
            print(f"Erro ao assinar o termo: {e}")


# Classe Empresa que herda de Usuario
class Empresa(Usuario):
    def __init__(self, nome, senha, area, periodo, salario, data_inicial: int, data_final: int, carga_horaria: int, cnpj: int, supervisor_nome, supervisor_contato, supervisor_cargo):
        super().__init__(nome, senha, area, periodo)
        self.salario = salario
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.carga_horaria = carga_horaria
        self.cnpj = cnpj
        self.supervisor = Supervisor(supervisor_nome, supervisor_contato, supervisor_cargo)

    def get_info(self):
        return (f'Empresa: {self._nome}, Área: {self._area}, Período: {self._periodo}, '
                f'Salário Oferecido: {self.salario}, Supervisor: {self.supervisor.nome}')

    def criar_senha(self, senha):
        self.set_senha(senha)

    def adicionar_nome(self, nome):
        self.set_nome(nome)
