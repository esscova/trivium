
# dados
vendas = [
    {'produto': 'Notebook', 'categoria': 'Eletrônicos', 'quantidade': 2, 'preco_unitario': 2500.00},
    {'produto': 'Smartphone', 'categoria': 'Eletrônicos', 'quantidade': 5, 'preco_unitario': 1800.00},
    {'produto': 'Camiseta', 'categoria': 'Vestuário', 'quantidade': 10, 'preco_unitario': 50.00},
    {'produto': 'Notebook', 'categoria': 'Eletrônicos', 'quantidade': 1, 'preco_unitario': 2600.00},
    {'produto': 'Camiseta', 'categoria': 'Vestuário', 'quantidade': 4, 'preco_unitario': 55.00},
]

# 1. total de vendas por produto
total_por_produto = {}
quantidade_por_produto = {}
receita_total = 0
precos_por_categoria = {}

for venda in vendas:
    produto = venda['produto']
    categoria = venda['categoria']
    quantidade = venda['quantidade']
    preco = venda['preco_unitario']
    total_venda = quantidade * preco
    
    # soma total por produto
    total_por_produto[produto] = total_por_produto.get(produto, 0) + total_venda
    
    # soma qtd por produto
    quantidade_por_produto[produto] = quantidade_por_produto.get(produto, 0) + quantidade

    # receita total
    receita_total += total_venda

    # preços por categoria
    if categoria not in precos_por_categoria:
        precos_por_categoria[categoria] = []
    precos_por_categoria[categoria].append(preco)

# 2. produto mais vendido em qtd
mais_vendido = max(quantidade_por_produto, key=quantidade_por_produto.get)

# 3. receita total já foi calculada

# 4. media de preço p/ categoria
media_preco_categoria = {}
for categoria, precos in precos_por_categoria.items():
    media = sum(precos) / len(precos)
    media_preco_categoria[categoria] = round(media, 2)

# resultados #
print("\n1. Total de vendas por produto:")
for produto, total in total_por_produto.items():
    print(f"   {produto}: R$ {total:.2f}")

print(f"\n2. Produto mais vendido em quantidade: {mais_vendido} ({quantidade_por_produto[mais_vendido]} unidades)")

print(f"\n3. Receita total: R$ {receita_total:.2f}")

print("\n4. Média de preço por categoria:")
for categoria, media in media_preco_categoria.items():
    print(f"   {categoria}: R$ {media:.2f}")

