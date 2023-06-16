import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.conta_corrente = None

    def criar_conta_corrente(self):
        self.conta_corrente = ContaCorrente(self)

    def obter_saldo(self):
        if self.conta_corrente is not None:
            return self.conta_corrente.saldo
        else:
            return 0.0


class ContaCorrente:
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0.0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.depositos.append(valor)
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if self.saldo >= valor and valor <= 500.00 and len(self.saques) < 3:
            self.saques.append(valor)
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif valor > 500.00:
            print('O valor máximo de saque é R$ 500.00.')
        elif len(self.saques) >= 3:
            print('Você já realizou o limite máximo de saques diários.')
        else:
            print('Saldo insuficiente para realizar o saque.')

    def extrato(self):
        print('Extrato:')
        if len(self.depositos) == 0 and len(self.saques) == 0:
            print('Não foram realizadas movimentações.')
        else:
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')


# Programa principal
usuarios = []

continuar = True

while continuar:
    print('----- Sistema Bancário da DIO.ME -----')
    print('1. Criar usuário')
    print('2. Criar conta corrente')
    print('3. Depositar')
    print('4. Sacar')
    print('5. Extrato')
    print('6. Sair')

    opcao = input('Selecione uma opção: ')

    if opcao == '1':
        nome_usuario = input('Informe o nome do usuário: ')
        usuario = Usuario(nome_usuario)
        usuarios.append(usuario)
        print(f'Usuário "{nome_usuario}" criado com sucesso.')
    elif opcao == '2':
        nome_usuario = input('Informe o nome do usuário: ')
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.nome == nome_usuario:
                usuario_encontrado = usuario
                break
        if usuario_encontrado is None:
            print(f'Usuário "{nome_usuario}" não encontrado.')
        else:
            usuario_encontrado.criar_conta_corrente()
            print(f'Conta corrente criada para o usuário "{nome_usuario}".')
    elif opcao == '3':
        nome_usuario = input('Informe o nome do usuário: ')
        valor_deposito = float(input('Informe o valor do depósito: '))
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.nome == nome_usuario:
                usuario_encontrado = usuario
                break
        if usuario_encontrado is None:
            print(f'Usuário "{nome_usuario}" não encontrado.')
        else:
            if usuario_encontrado.conta_corrente is None:
                print(f'O usuário "{nome_usuario}" não possui uma conta corrente.')
            else:
                usuario_encontrado.conta_corrente.depositar(valor_deposito)
    elif opcao == '4':
        nome_usuario = input('Informe o nome do usuário: ')
        valor_saque = float(input('Informe o valor do saque: '))
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.nome == nome_usuario:
                usuario_encontrado = usuario
                break
        if usuario_encontrado is None:
            print(f'Usuário "{nome_usuario}" não encontrado.')
        else:
            if usuario_encontrado.conta_corrente is None:
                print(f'O usuário "{nome_usuario}" não possui uma conta corrente.')
            else:
                usuario_encontrado.conta_corrente.sacar(valor_saque)
    elif opcao == '5':
        nome_usuario = input('Informe o nome do usuário: ')
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.nome == nome_usuario:
                usuario_encontrado = usuario
                break
        if usuario_encontrado is None:
            print(f'Usuário "{nome_usuario}" não encontrado.')
        else:
            if usuario_encontrado.conta_corrente is None:
                print(f'O usuário "{nome_usuario}" não possui uma conta corrente.')
            else:
                usuario_encontrado.conta_corrente.extrato()
    elif opcao == '6':
        continuar = False
        print('Saindo...')
    else:
        print('Opção inválida. Tente novamente.')
