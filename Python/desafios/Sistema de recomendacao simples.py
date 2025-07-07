"""
Desafio: Sistema de Recomendação Simples

    Crie um sistema básico de recomendação que:

    - Receba dados de avaliações de usuários para produtos (matriz usuário-produto)
    - Calcule similaridade entre usuários usando correlação
    - Recomende produtos para um usuário baseado em usuários similares
    - Implemente filtros por categoria de produto

@author: Wellington M Santos
linkedin: in/wellington-moreira-santos

Dependências:
    - numpy
    - pandas
"""
import numpy as np
import pandas as pd

def calcular_similaridade(matriz):
    return matriz.T.corr(method='pearson')

def recomendar_produtos(usuario, matriz, similaridade, n_recomendacoes=5):
    avaliacoes_usuario = matriz.loc[usuario]
    similares = similaridade[usuario].drop(usuario).dropna()
    
    pontuacoes = {}
    for produto in matriz.columns:
        if pd.isna(avaliacoes_usuario[produto]):
            soma_sim = 0
            soma_peso = 0
            for outro_usuario, sim in similares.items():
                nota = matriz.loc[outro_usuario, produto]
                if pd.notna(nota):
                    soma_sim += sim * nota
                    soma_peso += abs(sim)
            if soma_peso > 0:
                pontuacoes[produto] = soma_sim / soma_peso

    return sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)[:n_recomendacoes]

def filtrar_por_categoria(matriz, categorias_dict, categoria):
    produtos_filtrados = [p for p, c in categorias_dict.items() if c == categoria]
    return matriz[produtos_filtrados]

def main():
    # Matriz de avaliações
    matriz = pd.DataFrame({
        'Produto1': [5, 4, np.nan, 2, 1],
        'Produto2': [3, np.nan, 4, 5, 2],
        'Produto3': [np.nan, 2, 5, 3, 4],
    }, index=['U1', 'U2', 'U3', 'U4', 'U5'])

    # Categorias dos produtos
    categorias = {
        'Produto1': 'A',
        'Produto2': 'A',
        'Produto3': 'B'
    }

    # Similaridade entre usuários
    similaridade = calcular_similaridade(matriz)

    # Recomendações para U1
    recomendacoes = recomendar_produtos('U1', matriz, similaridade)
    print(f'Recomendações para U1: {recomendacoes}')

    # Filtro por categoria A
    matriz_filtrada = filtrar_por_categoria(matriz, categorias, 'A')
    print(f'\nMatriz filtrada por categoria A:\n{matriz_filtrada}')

if __name__ == "__main__":
    main()
