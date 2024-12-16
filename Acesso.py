from Classes import Aluno, Empresa

def cadastro(lista):
    try:
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

            # Validação para garantir que anoEscolar seja numérico
            while True:
                try:
                    anoEscolar = int(input('Ano escolar: ').strip())  # Tenta converter para int
                    break  # Se a conversão for bem-sucedida, sai do loop
                except ValueError:
                    print("Erro: Ano escolar deve ser um número. Tente novamente, por favor.")

            # Validação para garantir que idade seja numérica
            while True:
                try:
                    idade = int(input('Idade: ').strip())  # Tenta converter para int
                    break  # Se a conversão for bem-sucedida, sai do loop
                except ValueError:
                    print("Erro: Idade deve ser um número. Tente novamente.")

            contato = input('Contato: ').strip()

            aluno_obj = Aluno(nome, senha, area, periodo, diasdisponiveis, anoEscolar, idade, contato)
            print(f"\nCadastro realizado: {aluno_obj.get_info()}")
            lista.append(aluno_obj)

        elif '2' in escolha or 'EMPRESA' in escolha.upper():
            print('''\nEscreva suas informações NESSA ORDEM:
Nome, Senha, Área, Período, Salário, Carga horária, CNPJ e as informações do seu Supervisor:''')

            nome = input('Nome: ').strip()
            senha = input('Senha: ').strip()
            area = input('Área: ').strip()
            periodo = input('Período: ').strip()
            salario = input('Salário: ').strip()
            cargaHoraria = input('Carga horária: ').strip()
            cnpj = input('CNPJ: ').strip()
            Snome = input('Supervisor nome: ').strip()
            Scontato = input('Supervisor contato: ').strip()
            Scargo = input('Supervisor cargo: ').strip()

            empresa_obj = Empresa(nome, senha, area, periodo, salario, 202401, 202412, cargaHoraria, cnpj, Snome, Scontato, Scargo)
            print(f"\nCadastro realizado: {empresa_obj.get_info()}")
            lista.append(empresa_obj)

        else:
            print("\nEscolha inválida. Tente novamente.")

    except Exception as e:
        print(f"\nErro durante o cadastro: {e}")


def logon(lista):
    try:
        print('\nDigite seu login:')
        usuario = input('Usuário: ').strip()
        senha = input('Senha: ').strip()

        for item in lista:
            if isinstance(item, (Aluno, Empresa)):  # Verifica se é Aluno ou Empresa
                if item.get_nome() == usuario and item.get_senha() == senha:
                    print(f"\nVocê está logado:\n{item.get_info()}")
                    return True

        print("\nUsuário ou senha incorretos.")
        return False  # Retorna False em caso de falha no login

    except Exception as e:
        print(f"\nErro durante o login: {e}")
        return False  # Caso ocorra algum erro no login, retorna False
