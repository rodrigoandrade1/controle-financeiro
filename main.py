import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS carteira (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, saldo INTEGER NOT NULL, descricao TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS banco (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, saldo INTEGER NOT NULL, descricao TEXT NOT NULL)")

carteiraSelecionada = "carteira"

def adicionarConta(descricao, valor):
    cursor.execute("""INSERT INTO carteira (descricao, saldo) VALUES (?, ?)""", (descricao, valor))

def consultarSaldo():
    saldo = cursor.execute("""SELECT saldo FROM CARTEIRA""")
    total = cursor.fetchall()
    soma = 0
    for contas in total:
        soma = soma + contas[0]
    return soma


while True:
    print(f'Saldo({carteiraSelecionada}): R${consultarSaldo()}')
    print('Use "1" para adicionar saldo')
    print('Use "2" para remover saldo')
    print('Use "3" para transferir entre contas')
    print('Use "4" para alterar a carteira')
    print('Use "5" para ver registros')
    print('Use "9" para sair e salvar')
    acao = int(input('Informe a ação desejada: '))
    if acao == 1:
        descricaoConta = input('Informe um nome para o crédito: ')
        valorConta = int(input('Informe um valor para o crédito: '))
        adicionarConta(descricaoConta, valorConta)
        conn.commit()
        print(f'Conta {descricaoConta} de R${valorConta} creditado com sucesso!')
        print('')

    elif acao == 2:
        descricaoConta = input('Informe um nome para o débito: ')
        valorConta = int(input('Informe o valor do débito: '))
        adicionarConta(descricaoConta, -valorConta)
        conn.commit()
        print(f'Conta {descricaoConta} de -R${valorConta} debitado com sucesso!')

    elif acao == 3:
        print('TO-DO')

    elif acao == 4:
        print('TO-DO')

    elif acao == 5:
        print('TO-DO')

    elif acao == 9:
        print('Fechando sistema e salvando..')
        conn.close()
        break
