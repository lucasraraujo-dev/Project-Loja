class Produto:
    def __init__(self, codigo, nome, preco, quantidade, marca):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo
        self.quantidade = quantidade
        self.marca = marca

    def get_produto(self):
        lista_produtos = [
            Produto(1, "Óleo", 7.80 , 7, "Marca1"),
            Produto(2, "Arroz", 22, 9, "Marca2"),
            Produto(3, "Feijão", 12.50, 6, "Marca3"),
            Produto(4, "Sabão em Pó", 23.40, 12, "Marca4"),
            Produto(5, "Amaciante", 16, 16, "Marca5"),
        ]

        print("Escolha seu produto")
        for produto in lista_produtos:
            print(f"{produto.codigo} -{produto.marca} {produto.nome} {produto.preco} {produto.quantidade}")

        codigo_produto = int(input("Digite o código do Produto: "))
        produto_escolhido = next(filter(lambda produto: produto.codigo == codigo_produto, lista_produtos))
        return produto_escolhido
novo_produto = Produto(None, None, None, None, None).get_produto()
