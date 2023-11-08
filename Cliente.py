class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []

    def adicionar_item(self, produto, quantidade):
        if quantidade > 0:
            self.items.append((produto, quantidade))
        else:
            raise ValueError("Quantidade de itens inválida.")

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.items:
            total += produto.preco * quantidade
        return total
