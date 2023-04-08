from utils import clear_terminal
import json


class Pecas:
    def __init__(self, id=None, nome=None, cor=None,material=None ):
        self.id = id
        self.nome = nome
        self.cor = cor
        self.material = material
        
    def __str__(self):
        return f"id: {self.id}\nNome: {self.nome}\nCor: {self.cor}\nMaterial: {self.material}"
    
    def get_nova_peca(self):
        clear_terminal()
        self.nome = input("Digite o nome da Peça: ")
        self.cor = input("Digite a cor escolhida")
        self.material = input("Digite o material escolhido")
        self.id = self.get_novo_id()
        return self
    
    def get_novo_id(self):
        try:
            with open("pecas.Json", "r") as file:
                pecas = json.load(file)
                ultimo_id = 0
                for peca in pecas:
                    if peca["id"] >ultimo_id:
                        ultimo_id = peca["id"]
                return ultimo_id + 1
        except Exception as e:
            return 1
        
    def carregar_peca(self, codigo):
        with open("peca.Json", "r") as file:
            pecas = json.load(file)
            for peca in pecas:
                if peca["id"] == codigo:
                    self.id = peca["id"]
                    self.nome = peca["nome"]
                    self.cor = peca["cor"]
                    self.material = peca["material"]
                    break
            else:
                print("Peça não encontrada!")
                return
        return self
    
    def excluir_peca(self, codigo):
        with open("pecas.Json", "r") as file:
            pecas = json.load(file)
            for peca in pecas:
                if peca["id"] == codigo:
                    pecas.remove(peca)
                    break
            else:
                print("Peça não encontrada!")
                return
        with open("pecas.Json", "w") as file:
            json.dump(pecas, file)
            
    def listar_pecas(self):
        with open("pecas.json", "r") as file:
            pecas = json.load(file)
            for peca in pecas:
                print(f"{'-' * 80}\nId: {peca['id']}  | Nome: {peca['nome']}  |  Cor: {peca['cor']}  |  Material: {peca['material']}  |\n{'-' * 80}")
                
    def salvar_arquivo(array_pecas):
        with open("pecas.Json", "w") as file:
            json.dump(array_pecas, file)
            
    def carregar_pecas():
        pecas = []
        try:
            with open("pecas.Json", "r") as file:
                pecas = json.load(file)
        except Exception as e:
            pass
        return pecas
    
    
    def abrir_cadastro_pecas():
        clear_terminal()
        print("Cadastro de Peças")
        chosen_opition = -1
        while chosen_opition != 0:
            chosen_opition = int(input("Escolha uma opção: \n1. Nova Peça\n2. Editar peça\n3. Excluir Peça\n4. Listar Peças\n0. Voltar: "))
            if chosen_opition == 1:
                nova_peca = Pecas().get_nova_peca()
                
                pecas = carregar_pecas()
                pecas.append(nova_peca.__dict__)
                
                salvar_arquivo(pecas)
            elif chosen_opition == 2:
                codigo = int(input("Digite o código da Peça"))
                peca = Pecas().carregar_peca(codigo)
                if peca is not None: