"""
@autor: Wellinton M Santos
@data: 2025-07-10
@descricao: Sistema OOP para gestao de estoques
@versao: 1.0
@dependencias: random
@observacoes: Este sistema simula a gestão de estoques com funcionalidades de reposição automática,
              simulação de demanda e relatórios de produtos em falta ou excesso.
@uso: Execute o script em um ambiente Python com a biblioteca 'random' disponível.
@exemplo: Veja a seção de testes no final do script para exemplos de uso.
"""
import random

class Produto:
    def __init__(self, nome, categoria, preco, quantidade_minima):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade_minima = quantidade_minima
        self.quantidade_atual = 0
        self.historico_vendas = []

    def registrar_venda(self, quantidade):
        if quantidade > self.quantidade_atual:
            quantidade = self.quantidade_atual  # impede vender mais do que há em estoque
        self.historico_vendas.append(quantidade)
        self.quantidade_atual -= quantidade

    def ponto_reposicao(self):
        if not self.historico_vendas:
            return self.quantidade_minima
        media_vendas = sum(self.historico_vendas[-7:]) / min(7, len(self.historico_vendas))
        return int(media_vendas * 2)  # margem de segurança

    def precisa_repor(self):
        return self.quantidade_atual <= self.ponto_reposicao()

    def __str__(self):
        return (f"{self.nome} | Categoria: {self.categoria} | "
                f"Qtd Atual: {self.quantidade_atual} | Ponto de Reposição: {self.ponto_reposicao()}")

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto, quantidade):
        if produto.nome in self.produtos:
            self.produtos[produto.nome].quantidade_atual += quantidade
        else:
            produto.quantidade_atual = quantidade
            self.produtos[produto.nome] = produto

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome].registrar_venda(quantidade)
        else:
            print(f"Produto '{nome}' não encontrado.")

    def relatorio_falta(self):
        return [p for p in self.produtos.values() if p.precisa_repor()]

    def relatorio_excesso(self):
        return [p for p in self.produtos.values()
                if p.quantidade_atual > p.ponto_reposicao() * 2]

    def simular_demanda(self, nome, tipo, dias=7):
        if nome not in self.produtos:
            print(f"Produto '{nome}' não encontrado.")
            return
        produto = self.produtos[nome]
        for _ in range(dias):
            if tipo == 'alta':
                produto.registrar_venda(random.randint(5, 10))
            elif tipo == 'baixa':
                produto.registrar_venda(random.randint(0, 2))

    def exibir_todos_produtos(self):
        for p in self.produtos.values():
            print(p)

# === TESTE NO MAIN ===
if __name__ == "__main__":
    estoque = Estoque()

    arroz = Produto("Arroz", "Alimento", 25.0, 10)
    feijao = Produto("Feijão", "Alimento", 20.0, 8)
    sabao = Produto("Sabão", "Limpeza", 5.0, 5)

    estoque.adicionar_produto(arroz, 50)
    estoque.adicionar_produto(feijao, 30)
    estoque.adicionar_produto(sabao, 15)

    # Simular vendas manuais
    estoque.remover_produto("Arroz", 12)
    estoque.remover_produto("Feijão", 5)

    # Simular cenários
    estoque.simular_demanda("Feijão", "alta", dias=5)
    estoque.simular_demanda("Sabão", "baixa", dias=5)

    print("\n=== Produtos no Estoque ===")
    estoque.exibir_todos_produtos()

    print("\n=== Produtos em Falta ===")
    for p in estoque.relatorio_falta():
        print(f"- {p.nome} (Qtd Atual: {p.quantidade_atual}, Ponto de Reposição: {p.ponto_reposicao()})")

    print("\n=== Produtos em Excesso ===")
    for p in estoque.relatorio_excesso():
        print(f"- {p.nome} (Qtd Atual: {p.quantidade_atual}, Ponto de Reposição: {p.ponto_reposicao()})")
# === FIM DO CÓDIGO ===