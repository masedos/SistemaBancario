import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(conta, valor):
    if valor > 0:
        conta.depositar(valor)
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

def sacar(conta, valor):
    if valor > 0:
        conta.sacar(valor)
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta.historico.transacoes:
            print(f"{transacao['tipo']}:\tR$ {transacao['valor']:.2f} - {transacao['data']}")
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuario = PessoaFisica(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        conta = ContaCorrente.nova_conta(usuario, numero_conta)
        usuario.adicionar_conta(conta)
        contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(conta)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario and usuario.contas:
                valor = float(input("Informe o valor do depósito: "))
                depositar(usuario.contas[0], valor)
            else:
                print("\n@@@ Usuário ou conta não encontrada! @@@")

        elif opcao == "s":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario and usuario.contas:
                valor = float(input("Informe o valor do saque: "))
                sacar(usuario.contas[0], valor)
            else:
                print("\n@@@ Usuário ou conta não encontrada! @@@")

        elif opcao == "e":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario and usuario.contas:
                exibir_extrato(usuario.contas[0])
            else:
                print("\n@@@ Usuário ou conta não encontrada! @@@")

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
