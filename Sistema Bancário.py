def Extrato(saldo, extrato_list):
    print("================================Extratos=============================")
    if extrato_list:
        for movimento in extrato_list:
            print(movimento)
    else:
        print("Nenhuma operação realizada.")
    print()  # Linha em branco
    print(f"Saldo: R$ {saldo:.2f}")
    print("======================================================================")


def criar_conta_corrente(usuario, numero_conta):
    print("\n" + "=" * 16 + " Criação de Conta Corrente " + "=" * 16)
    agencia = "0001"  # Agência fixa
    conta = {
        "usuario": usuario,
        "agencia": agencia,
        "numero_conta": numero_conta
    }
    print("Conta corrente criada com sucesso!")
    return conta


def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
        extrato.append(f"Depósito falhado: valor inválido R$ {valor:.2f}")
    return saldo


def sacar(saldo, extrato, limite_saque, saques_realizados, saques_diarios):
    if saques_realizados >= saques_diarios:
        print("Limite diário de saques atingido.")
        extrato.append("Tentativa de saque falhada: limite diário atingido.")
        return saldo, saques_realizados

    valor = float(input("Informe o valor do saque: R$ "))
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        extrato.append(f"Saque falhado: saldo insuficiente para R$ {valor:.2f}")
    elif valor > limite_saque:
        print(f"O limite máximo por saque é de R$ {limite_saque:.2f}.")
        extrato.append(f"Saque falhado: valor R$ {valor:.2f} acima do limite de R$ {limite_saque:.2f}")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_realizados += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
        extrato.append(f"Saque falhado: valor inválido R$ {valor:.2f}")
    return saldo, saques_realizados


def cadastrar_usuario(usuarios):
    print("\n" + "=" * 16 + " Cadastro de Usuário (Cliente) " + "=" * 16)
    cpf_input = input("CPF (apenas números serão armazenados): ")
    cpf_numeros = ''.join(filter(str.isdigit, cpf_input))

    # Verifica se já existe um usuário com o CPF informado
    usuario_encontrado = next((usuario for usuario in usuarios if usuario['cpf'] == cpf_numeros), None)
    if usuario_encontrado:
        print("Aviso: CPF encontrado. Usuário vinculado à conta existente.")
        return usuario_encontrado

    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço (formato: logradouro, nro, bairro, cidade/sigla estado): ")

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_numeros,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuario


def listar_contas(contas):
    print()
    for conta in contas:
        usuario = conta.get("usuario", {})
        print(f"Agência: {conta.get('agencia')}")
        print(f"C/C: {conta.get('numero_conta')}")
        print(f"Titular: {usuario.get('nome', 'Desconhecido')}\n")
        print("========================================================================")


def main():
    saldo = 0.0
    limite_saque = 500.0
    saques_diarios = 3
    saques_realizados = 0
    extrato = []
    numero_conta = 1

    usuarios = []  # Lista para armazenar os usuários cadastrados
    contas = []    # Lista para armazenar as contas criadas
    usuario_logado = None  # Usuário atualmente cadastrado ou selecionado

    while True:
        print("\n" + "=" * 16 + " MENU " + "=" * 16)
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Cadastrar Usuário")
        print("5. Criar Conta Corrente")
        print("6. Listar Contas")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo = depositar(saldo, extrato)

        elif opcao == "2":
            saldo, saques_realizados = sacar(saldo, extrato, limite_saque, saques_realizados, saques_diarios)

        elif opcao == "3":
            Extrato(saldo, extrato)

        elif opcao == "4":
            usuario_cadastrado = cadastrar_usuario(usuarios)
            if usuario_cadastrado:
                usuario_logado = usuario_cadastrado

        elif opcao == "5":
            if usuario_logado is None:
                print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
            else:
                conta = criar_conta_corrente(usuario_logado, numero_conta)
                contas.append(conta)
                numero_conta += 1

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Obrigado por utilizar o MENU. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
