import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()


class SistemaBancario:
    def __init__(self):
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
banco = SistemaBancario()

continuar = True

while continuar:
    print('----- Sistema Bancário da DIO.ME -----')
    print('1. Depositar')
    print('2. Sacar')
    print('3. Extrato')
    print('4. Sair')

    opcao = input('Selecione uma opção: ')

    if opcao == '1':
        valor_deposito = float(input('Informe o valor do depósito: '))
        banco.depositar(valor_deposito)
    elif opcao == '2':
        valor_saque = float(input('Informe o valor do saque: '))
        banco.sacar(valor_saque)
    elif opcao == '3':
        banco.extrato()
    elif opcao == '4':
        continuar = False
        print('Saindo...')
    else:
        print('Opção inválida. Tente novamente.')
