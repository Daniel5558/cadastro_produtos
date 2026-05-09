lista_produtos = []

def cadastrar():
    nome_prod = input("Digite o nome do produto: ")
    valor_prod = str(input("Digite o valor do produto: "))
   
   
    produto = {"nome": nome_prod, "valor": valor_prod}
   
   
    lista_produtos.append(produto)
   
    print(f'''
Produto {nome_prod} cadastrado com sucesso!
Valor : {valor_prod}
    ''')
   
def menu():
    while True:
        print('''
SELECIONE UMA OPÇÃO :
======================
1 - CADASTRAR PRODUTO
2 - SAIR
''')
        escolha = int(input())
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            print("\nProdutos cadastrados:")
            if lista_produtos == []:
                print("Nenhum Produto cadastrado !!")
            total = 0
            for produto in lista_produtos:
                print(f"- {produto['nome']}: R$ {produto['valor']}")
            break
menu()
