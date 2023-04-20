with open('receita.txt', 'r') as receita:
    texto = receita.read()
    print(texto)

with open('receita.txt', 'w') as receita:
    receita.write('Hello!!')

while True:
    print('Menu Principal:')
    input('Selecione uma opção para Prosseguir: 1 - Informar receita \n 2 - Alterar receita \n 3 - Excluir receita \n 4 - Listar receita')
