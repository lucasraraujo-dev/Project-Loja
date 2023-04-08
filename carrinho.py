class Carrinho:
    def __init__(self, codigo=None):
        self.codigo = codigo
        
    def get_carrinho(self):
        listas_carrinhos = [
            Carrinho(1, "Cesta de mão"),
            Carrinho(2, "Carrinho pequeno"),
            Carrinho(3, "Carrinho Medio"),
            Carrinho(4, "Carrinho Grande"),
        ]
        
        print("Escolha o carrinho: ")
        for carrinho in listas_carrinhos:
            print(f"{carrinho.codigo}")
            
        codigo_carrinho = int(input("Dogote o codigo do Carrinho"))
        carrinho_escolhido = next(filter(lambda carrinho: carrinho.codigo == codigo_carrinho, listas_carrinhos))
        return carrinho_escolhido