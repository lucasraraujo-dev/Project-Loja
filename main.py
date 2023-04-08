from loja import Loja
from utils import *
from cadastro import abrir_cadastro_pecas

def __main__():
    
    chosen_opition = -1
    while chosen_opition != 0:
        clear_terminal()
        chosen_opition = int(input("1. Nova LOJA\n2. Reimprimir Loja criada\n0. Sair: "))
        if chosen_opition == 1:
            nova_loja = Loja().get_nova_loja()
            nova_loja.imprimir()
            nova_loja.salvar_arquivo()
        elif chosen_opition == 2:
            codigo = int(input("Digite o código da Loja"))
            Loja().carregar_loja(codigo)
        elif chosen_opition == 0:
            print("Saindo...")
        else:
            print("Opção inválida")
        pause_terminal()
        
        
if __name__ == "__main__":
    __main__()


