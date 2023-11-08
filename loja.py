import Cliente
class Loja:
    def __init__(self):
        self.estoque = []

    def adicionar_produto(self, produto):
        self.estoque.append(produto)

    def encontrar_produto(self, nome):
        for produto in self.estoque:
            if produto.nome == nome:
                return produto
        return None

    def vender_produto(self, nome, quantidade, cliente):
        produto = self.encontrar_produto(nome)
        if produto:
            produto.vender(quantidade)
            return Cliente.Carrinho(cliente)
        else:
            raise ValueError("Produto não encontrado no estoque.")
