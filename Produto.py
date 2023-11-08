class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def vender(self, quantidade_vendida):
        if quantidade_vendida <= self.quantidade:
            self.quantidade -= quantidade_vendida
        else:
            raise ValueError("Quantidade insuficiente em estoque.")

    def repor_estoque(self, quantidade_reposta):
        if quantidade_reposta > 0:
            self.quantidade += quantidade_reposta
        else:
            raise ValueError("Quantidade de reposição inválida.")

    def calcular_valor_total(self):
        return self.preco * self.quantidade