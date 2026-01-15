from classes.Produto import Produto

def menu():
    print()
    print("1 - Listar Produtos")
    print("2 - Adicionar Produto")
    print("3 - Alterar Produto")
    print("4 - Remover Produto")
    print("0 - Sair")
    print()

opcao = 1

while opcao != 0:

    menu()
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            Produto.listarTodos()
        case 2:
            codigo = input('Digite o código: ')
            nome = input('Digite o nome: ')
            quantidade =  input('Digite a quantidade: ')
            valor = input('Digite o valor: ')

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
        case 3:
            Produto.listarTodos()
            selecionado = input('Qual item deseja alterar? ')
            try:
                idx = int(input('Escolha o índice do produto a alterar: '))
            except ValueError:
                print('Índice inválido')
                break

            try:
                existente = Produto.consultar(idx)
            except Exception:
                print('Índice não encontrado')
                break

            print(f"Atual: código={existente.get('codigo')}, nome={existente.get('nome')}, quantidade={existente.get('quantidade')}, valor={existente.get('valor')}")

            codigo = input(f"Novo código [{existente.get('codigo')}]: ") or existente.get('codigo')
            nome = input(f"Novo nome [{existente.get('nome')}]: ") or existente.get('nome')
            quantidade = input(f"Nova quantidade [{existente.get('quantidade')}]: ") or existente.get('quantidade')
            valor = input(f"Novo valor [{existente.get('valor')}]: ") or existente.get('valor')

            # Conversões simples de tipo
            try:
                quantidade = int(quantidade)
            except Exception:
                pass
            try:
                valor = float(valor)
            except Exception:
                pass

            produto = Produto(codigo, nome, quantidade, valor)
            produto.alterar(idx)
        case 4:
            ...
       