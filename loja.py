from carrinho import Carrinho
from produto import Produto
from datetime import datetime
import glob
import os
from utils import clear_and_print, clear_terminal

class Loja:
    def __init__(self, produto = None, carrinho = None):
        self.codigo = self.get_codigo()
        self.produto = produto
        self.carrinho = carrinho
        
    
    def get_codigo(self):
        files = glob.glob("loja-*.txt")
        last_number = 0
        for file in files:
            number = int(file.split("-")[1].split(".")[0])
            if number > last_number:
                last_number = number
        return last_number +1
    
    
    def get_nova_loja(self):
        clear_terminal()
        self.produto = Produto().get_produto()
        clear_terminal()
        self.carrinho = Carrinho().get_carrinho()
        return self
    
    def get_print_buffer(self):
        print_buffer = "** Loja e produtos  **\n\n"
        print_buffer += f"carrinho: {self.carrinho.marca}\n"
        print_buffer += f"produto: {self.produto.marca}\n"
        print_buffer += f"Total: {self.carrinho.preco + self.produto.preco}\n"
        print_buffer += "** ** Obrigado pela preferencia ** **\n"
        return print_buffer
    
    def imprimir(self):
        print_buffer = self.get_print_buffer()
        clear_and_print(print_buffer)
        
    def salvar_arquivo(self):
        print_biffer = self.get_print_buffer()
        
        with open(f"loja-{self.codigo}.txt", "w") as f:
            f.write(print_biffer)
            
    def carregar_loja(self, codigo):
        with open(f"loja-{codigo}.txt", "r") as f:
            clear_and_print(f.read())