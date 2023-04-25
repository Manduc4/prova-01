
textMenu = 'Selecione uma opção para Prosseguir: \n 1 - Informar receita \n 2 - Alterar receita \n 3 - Excluir receita \n 4 - Listar receita \n 5 - Informar despesa \n 6 - Alterar despesa \n 7 - Excluir despesa \n 8 - Listar despesa \n \n --> '

# RECEITA ===============================================================================================

def informarReceita():
    receita = input('Valor: ')
    data = input('Informe o mes e o ano (mm/aaaa): ')
    payload = '\n' + data + ' ' + receita
    with open('receita.txt', 'a') as file:
        file.write(payload)


def alterarReceita():
    lines = []
    newLines = []
    data_a_alterar = (
        input('Informe o mes e ano que deseja alterar a receita (mm/aaaa): '))
    novo_valor = 0
    with open('receita.txt', 'r') as file:
        lines = file.read().split('\n')
    for line in lines:
        data = ''
        valor = ''
        if (len(line) > 0):
            data = line.split(' ')[0]
            valor = line.split(' ')[1]
            if (data == data_a_alterar):
                print('Data encontrada')
                novo_valor = input('Insira a nova receita: ')
                newLines.append('\n' + data + ' ' + novo_valor)
            else:
                newLines.append('\n' + data + ' ' + valor)
    if (novo_valor != 0):
        with open('receita.txt', 'w') as file:
            file.writelines(newLines)
    print('newLines: ', newLines)


def excluirReceita():
    lines = []
    newLines = []
    data_a_excluir = (
        input('Informe o mes e ano que deseja alterar a receita (mm/aaaa): '))
    data_encontrada = False
    with open('receita.txt', 'r') as file:
        lines = file.read().split('\n')
    for line in lines:
        if (len(line) > 0):
            data = line.split(' ')[0]
            if (data == data_a_excluir):
                data_encontrada = True
            else:
                newLines.append('\n' + data + ' ' + line[1])
    if (data_encontrada):
        with open('receita.txt', 'w') as file:
            file.writelines(newLines)
    else:
        print('Data não encontrada.')


def listarReceita():
    with open('receita.txt', 'r') as file:
        print(file.read())


# END RECEITA ===============================================================================================

# DESPESAS ===============================================================================================

def informarDespesa():
    valor = input('Valor: ')
    data = input('Informe o mes e o ano (mm/aaaa): ')
    payload = '\n' + data + ' ' + valor
    with open('despesas.txt', 'a') as file:
        file.write(payload)


def alterarDespesa():
    lines = []
    newLines = []
    data_a_alterar = (
        input('Informe o mes e ano que deseja alterar a despesa (mm/aaaa): '))
    novo_valor = 0
    with open('despesas.txt', 'r') as file:
        lines = file.read().split('\n')
    for line in lines:
        data = ''
        valor = ''
        if (len(line) > 0):
            data = line.split(' ')[0]
            valor = line.split(' ')[1]
            if (data == data_a_alterar):
                print('Data encontrada')
                novo_valor = input('Insira a nova despesa: ')
                newLines.append('\n' + data + ' ' + novo_valor)
            else:
                newLines.append('\n' + data + ' ' + valor)
    if (novo_valor != 0):
        with open('despesas.txt', 'w') as file:
            file.writelines(newLines)
    print('newLines: ', newLines)


def excluirDespesa():
    lines = []
    newLines = []
    data_a_excluir = (
        input('Informe o mes e ano que deseja alterar a despesa (mm/aaaa): '))
    data_encontrada = False
    with open('despesas.txt', 'r') as file:
        lines = file.read().split('\n')
    for line in lines:
        if (len(line) > 0):
            data = line.split(' ')[0]
            if (data == data_a_excluir):
                data_encontrada = True
            else:
                newLines.append('\n' + data + ' ' + line[1])
    if (data_encontrada):
        with open('despesas.txt', 'w') as file:
            file.writelines(newLines)
    else:
        print('Data não encontrada.')


def listarDespesa():
    with open('despesas.txt', 'r') as file:
        print(file.read())

# END DESPESAS ===============================================================================================

while True:
    print(' \n   Menu Principal \n')
    selected = str(input(textMenu))
    if (len(selected) == 0):
        print('Informar a opção é Obrigatório. \n')
    if (selected != '1') and (selected != '2') and (selected != '3') and (selected != '4') and (selected != '5') and (selected != '6') and (selected != '7') and (selected != '8'):
        print('Opção inválida! \n')
    else:
        if (selected == '1'):
            informarReceita()
        if (selected == '2'):
            alterarReceita()
        if (selected == '3'):
            excluirReceita()
        if (selected == '4'):
            listarReceita()
        if (selected == '5'):
            informarDespesa()
        if (selected == '6'):
            alterarDespesa()
        if (selected == '7'):
            excluirDespesa()
        if (selected == '8'):
            listarDespesa()
