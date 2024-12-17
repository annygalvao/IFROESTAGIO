from Classes import Aluno, Empresa


def cadastro(lista):
    print('''Qual seu tipo de usuário:
1 - Aluno
2 - Empresa''')

    escolha = input('R: ').strip()

    if '1' in escolha or 'ALUNO' in escolha.upper():
        print('''\nEscreva suas informações NESSA ORDEM:
Nome, Senha, Área, Período, Dias Disponíveis, anoEscolar, idade, contato:''')


        nome = input('Nome: ').strip()
        senha = input('Senha: ').strip()
        area = input('Área: ').strip()
        periodo = input('Período: ').strip()
        diasdisponiveis = input('Dias Disponíveis: ').strip()
        anoEscolar = input('Ano escolar: ').strip()
        while True:
            try:
                idade = int(input('Idade: '))
                break 
            except ValueError:
                    print ("Ocorreu um erro! Insira um número inteiro válido.")
        while True:
            try:
                contato = int(input('Contato: '))
                break
            except ValueError:
                print ("Ocorreu um erro! Insira um número inteiro válido.")
            

        aluno_obj = Aluno(nome, senha, area, periodo, diasdisponiveis,anoEscolar,idade,contato)
        print(f"\nCadastro realizado: {aluno_obj.get_info()}")
        lista.append(aluno_obj)

    elif '2' in escolha or 'EMPRESA' in escolha.upper():
        print('''\nEscreva suas informações NESSA ORDEM:
    Nome, Senha, Área, Período, Salário, Carga horária, CNPJ e as info do seu Supervisor:''')

        nome = input('Nome: ').strip()
        senha = input('Senha: ').strip()
        area = input('Área: ').strip()
        periodo = input('Período: ').strip()
        

        while True:   
            try:
                salario = int(input('Salário oferecido: '))
                if salario < 300:
                    raise Exception ("O salário não pode ser inferior a 300 reais")
                break 
            except:
                print("O salário não pode ser inferior a 300 reais")
                
        while True:
            try:
                cargaHoraria = int(input('Carga hóraria: ')) 
                break
            except ValueError: 
                print ("Insira dígitos numéricos válidos")
            finally: 
                print("Para concluir o cadastro")
         

        cnpj = input('CNPJ: ').strip()
        Snome = input('Supervisor nome: ').strip()
        Scontato = input('Supervisor contato: ').strip()
        Scargo = input('Supervisor carg: ').strip()
            
        empresa_obj = Empresa(nome, senha, area, periodo, salario,202401,202412,cargaHoraria,cnpj,Snome,Scontato,Scargo)
        print(f"\nCadastro realizado: {empresa_obj.get_info()}")
        lista.append(empresa_obj)

    else:
        print("\nEscolha inválida. Tente novamente.")


def logon(lista):
    print('\nDigite seu login:')
    usuario = input('Usuário: ').strip()
    senha = input('Senha: ').strip()

    for item in lista:
        if isinstance(item, Aluno) or isinstance(item, Empresa):
            if item.get_nome().strip() == usuario and item.get_senha().strip() == senha:
                print(f"\nVocê está logado:\n{item.get_info()}")
                return True

    print("\nUsuário ou senha incorretos.")
