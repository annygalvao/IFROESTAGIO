# Integrantes: Aryela Freitas Souza, Anny Maria Almeida Galvão, Livia Gabrielle Ambrosio Dias e Thayná Guarati de Oliveira
# Turma: 2°A Informática matutino

from Acesso import logon, cadastro
from Classes import Empresa, Aluno, DepEx, Orientador

# Inicialização da lista DB com instâncias corretas

DB = [
    Empresa('LuminaEletro', 'iluminatudo', 'eletrotécnica', 'tarde', '3000', 202401, 202412, 20, 123456789, "Carlos", 11987654321, "Engenheiro"),
    Empresa('SublimeVolt', 'senhatop', 'eletrotécnica', 'manhã', '3500', 202401, 202412, 20, 987654321, "Maria", 11912345678, "Engenheira"),
    Empresa('BioQuimica', 'admin', 'química', 'tarde', '4000', 202401, 202412, 20, 1234567789, "Rafael", 6914749151, "Chefe de Setor"),
    Empresa('QuímicaSolutions', 'senhasecreta', 'química', 'manhã', '4500', 202401, 202412, 20, 987654321, "Renata", 6914794724, "Coordenadora"),
    Empresa('IfroPro', 'senhaetudo', 'informática', 'tarde', '5000', 202401, 202412, 20, 246801357, "Thiago", 6984625495, "Supervisor"),
    Empresa('CiberSoluções', 'senha', 'informática', 'manhã', '5500', 202401, 202412, 20, 135792468, "Júlia", 6992053618, "Gerente de TI"),
    Empresa('BuildArt', 'BuildArt', 'edificações', 'tarde', '6000', 202401, 202412, 20,123098746 , "Marcelo", 6905670193, "Engenheiro Civil"),
    Empresa('InnovaEdifica', 'EdificaInnova', 'edificações', 'manhã', '6500', 202401, 202412, 20, 120934875, "Marta", 6975930935, "Arquiteta"),
    Aluno('Thayná', 'senhadathayna', 'informática', 'manhã', 'segunda', 2, 17, 11987651234),
    Aluno('Anny', 'senhadaanny', 'química', 'tarde', 'terça', 2, 17, 11987659876),
    Aluno('Lívia', 'senhadalivia', 'edificações', 'manhã', 'quarta', 2, 17,6912345678),
    Aluno('Aryela', 'senhadaaryela', 'eletrotécnica', 'tarde', 'quinta', 2, 17, 6909876543)
]

# Instâncias adicionais

depex = DepEx("Coordenação de Extensão", "Chefe de Extensão", 11987651234, "depex@ifro.edu.br")
orientador = Orientador("Dr. João", "Informática", 11912344321)

planoDeAtividade = []

Permission = False

while True:
    print('''
Menu Principal (digite o número da ação)
--------------
1 - Cadastro
2 - Login
3 - Ações do Aluno
4 - Ações da Empresa
5 - Ações do DepEx
6 - Ações do Orientador
7 - Sair
    ''')

    choice = input('Escolha uma opção: ').strip()

    if choice == '1':
        cadastro(DB)
    elif choice == '2':
        Permission = logon(DB)
    elif choice == '3' and Permission:
        aluno_nome = input("Digite o nome do aluno: ")
        aluno = next((a for a in DB if isinstance(a, Aluno) and a.get_nome() == aluno_nome), None)
        if aluno:
            print('''
Ações do Aluno
--------------
1 - Enviar Relatório ao Orientador
2 - Solicitar Tutorial ao DepEx
            ''')
            aluno_action = input("Escolha uma ação: ")
            if aluno_action == '1':
                aluno.enviarRelatorio(orientador)
            elif aluno_action == '2':
                aluno.solicitarTutorial(depex)
            else:
                print("Opção inválida.")
        else:
            print("Aluno não encontrado.")
    
    elif choice == '4' and Permission:
        empresa_nome = input("Digite o nome da empresa: ")
        empresa = next((e for e in DB if isinstance(e, Empresa) and e.get_nome() == empresa_nome), None)
        if empresa:
            print('''

Ações da Empresa
----------------
1 - Ver informações da Empresa
2 - Criar nova Senha
            ''')
            empresa_action = input("Escolha uma ação: ")
            if empresa_action == '1':
                print(empresa.get_info())
            elif empresa_action == '2':
                nova_senha = input("Digite a nova senha: ")
                empresa.criar_senha(nova_senha)
                print("Senha atualizada com sucesso!")
            else:
                print("Opção inválida.")
        else:
            print("Empresa não encontrada.")

    elif choice == '5' and Permission:
        print('''
        
Ações do DepEx
--------------
1 - Fornecer Formulário
2 - Lançar Termo de Compromisso
3 - Criar Plano de Trabalho
        ''')
        depex_action = input("Escolha uma ação: ")
        if depex_action == '1':
            depex.fornecer_formulario()
        elif depex_action == '2':
            depex.lancar_termo_de_compromisso()
        elif depex_action == '3':
            depex.criar_plano_de_trabalho(planoDeAtividade)
        else:
            print("Opção inválida.")

    elif choice == '6' and Permission:
        print('''
        
Ações do Orientador
-------------------
1 - Avaliar Relatório de Aluno
2 - Assinar Termo de Compromisso
        ''')
        orientador_action = input("Escolha uma ação: ")
        if orientador_action == '1':
            orientador.avaliar_relatorio()
        elif orientador_action == '2':
            orientador.assinar_termo()
        else:
            print("Opção inválida.")

    elif choice == '7' and Permission:
        print("Saindo do sistema. Obrigado!")
        break
    else:
        print("\nfaça Login primeiro1")
