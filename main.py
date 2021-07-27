import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS carteira (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, saldo REAL NOT NULL, descricao TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS banco (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, saldo REAL NOT NULL, descricao TEXT NOT NULL)")

def mostrarTitulo(titulo):
    print('\n'*250)
    print('='*40)
    print(titulo.center(40))
    print('='*40)

def alternarCarteira():
    mostrarTitulo('CARTEIRAS DISPONÍVEIS')
    print('[1] - Carteira')
    print('[2] - Banco')
    escolherCarteira = int(input('Informe a carteira desejada: '))
    global carteiraSelecionada
    if escolherCarteira == 1:
        carteiraSelecionada = 'carteira'
    elif escolherCarteira == 2:
        carteiraSelecionada = 'banco'

alternarCarteira()

def adicionarConta(descricao, valor, carteira = carteiraSelecionada):
    cursor.execute(f"""INSERT INTO {carteira} (descricao, saldo) VALUES (?, ?)""", (descricao, valor))

def consultarSaldo():
    saldo = cursor.execute(f"""SELECT saldo FROM {carteiraSelecionada}""")
    total = cursor.fetchall()
    soma = 0
    for contas in total:
        soma = soma + contas[0]
    return soma

def consultarRegistros():
    saldo = cursor.execute(f"""SELECT saldo, descricao FROM {carteiraSelecionada}""")
    registros = cursor.fetchall()
    mostrarTitulo('REGISTROS')
    for i in registros:
        print(f'R${i[0]} -> {i[1]}')
    input(" ")


while True:
    print('\n'*250)
    print('='*40)
    print(f'{carteiraSelecionada} > R${consultarSaldo()}'.center(40))
    print('='*40)
    print('Use "1" para adicionar saldo')
    print('Use "2" para remover saldo')
    print('Use "3" para transferir entre contas')
    print('Use "4" para alterar a carteira')
    print('Use "5" para ver registros')
    print('Use "9" para sair e salvar')
    acao = int(input('Informe a ação desejada: '))
    if acao == 1:
        descricaoConta = input('Informe um nome para o crédito: ')
        valorConta = float(input('Informe um valor para o crédito: '))
        adicionarConta(descricaoConta, valorConta, carteiraSelecionada)
        conn.commit()
        print(f'Conta {descricaoConta} de R${valorConta} creditado com sucesso!')
        print('')

    elif acao == 2:
        descricaoConta = input('Informe um nome para o débito: ')
        valorConta = float(input('Informe o valor do débito: '))
        adicionarConta(descricaoConta, -valorConta, carteiraSelecionada)
        conn.commit()
        print(f'Conta {descricaoConta} de -R${valorConta} debitado com sucesso!')

    elif acao == 3:
        mostrarTitulo('TRANSFERÊNCIA ENTRE CONTAS')
        print(f'[1] {carteiraSelecionada} > Carteira')
        print(f'[2] {carteiraSelecionada} > Banco')
        transferirPara = int(input('Informe a conta destino:'))
        valorConta = float(input('Informe o valor da transferência: '))
        if transferirPara == 1:
            adicionarConta(f'Transferência recebida ({carteiraSelecionada} > carteira)', valorConta, 'carteira')
            adicionarConta(f'Transferência enviada ({carteiraSelecionada} > carteira) R$', -valorConta, carteiraSelecionada)
            conn.commit()
        elif transferirPara == 2:
            adicionarConta(f'Transferência recebida ({carteiraSelecionada} > banco)', valorConta, 'banco')
            adicionarConta(f'Transferência enviada ({carteiraSelecionada} > banco) R$', -valorConta, carteiraSelecionada)
            conn.commit()

    elif acao == 4:
        alternarCarteira()

    elif acao == 5:
        consultarRegistros()

    elif acao == 9:
        print('Fechando sistema e salvando..')
        conn.close()
        break

    else:
        print('Informe uma opção válida!')