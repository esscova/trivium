"""
Desafio: Análise de séries temporais básica
    1. Simular vendas diárias por 30 dias
    2. Calcular média móvel de 7 dias
    3. Identificar tendência da série (crescente ou decrescente)
    4. Identificar dias com vendas acima da média geral
    5. Prever vendas para o dia 31 usando regressão linear
    6. Plotar gráfico com vendas diárias, média móvel e média geral

    autor: Wellington M Santos
    linkedin: in/wellington-moreira-santos
    
    Dependências:
    Python 3.12.4
    pandas, numpy, matplotlib, scikit-learn
"""

# dependências
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import logging

# configurações de logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Configurações do matplotlib
plt.style.use('ggplot')

# funções
def simular_vendas(qtd_dias=30, media=200, desvio=30):
    """Simula vendas diárias para um período de 30 dias.
    Parâmetros:
        qtd_dias (int): Número de dias a simular.
        media (float): Média de vendas diárias.
        desvio (float): Desvio padrão das vendas diárias.
    Retorna:
        pd.DataFrame: DataFrame com datas e vendas simuladas.
    """
    logger.info(f"Simulando vendas para {qtd_dias} dias com média {media} e desvio padrão {desvio}.")

    np.random.seed(42)  
    dias = pd.date_range(start='2025-01-01', periods=qtd_dias)
    vendas = np.random.normal(loc=media, scale=desvio, size=qtd_dias).round(2)
    df = pd.DataFrame({'dia': dias, 'vendas': vendas})
    df.set_index('dia', inplace=True)
    return df

def calcular_media_movel(df, janela=7):
    """Calcula a média móvel de 7 dias para as vendas.
    Parâmetros:
        df (pd.DataFrame): DataFrame com as vendas diárias.
        janela (int): Tamanho da janela para a média móvel.
    """
    logger.info(f"Calculando média móvel de {janela} dias.")
    
    if janela < 1:
        raise ValueError("O tamanho da janela deve ser pelo menos 1.")
    df['media_movel_7d'] = df['vendas'].rolling(window=janela).mean()

def identificar_tendencia(df):
    """Identifica a tendência da série temporal de vendas.
    Parâmetros:
        df (pd.DataFrame): DataFrame com as vendas diárias.
    Retorna:
        str: 'crescente' se a tendência for crescente, 'decrescente' se for decrescente.
    """
    logger.info("Identificando tendência da série temporal.")

    X = np.arange(len(df)).reshape(-1, 1)
    y = df['vendas'].values
    modelo = LinearRegression()
    modelo.fit(X, y)
    coef = modelo.coef_[0]
    return "crescente" if coef > 0 else "decrescente", coef, modelo

def dias_acima_da_media(df):
    """Identifica os dias com vendas acima da média geral.
    Parâmetros:
        df (pd.DataFrame): DataFrame com as vendas diárias.
    Retorna:
        tuple: Média geral de vendas e DataFrame com dias acima da média.
    """
    logger.info("Identificando dias com vendas acima da média geral.")

    media_geral = df['vendas'].mean()
    acima = df[df['vendas'] > media_geral]
    return media_geral, acima

def prever_proximo_dia(modelo, dia_index):
    """Prevê as vendas para o dia 31 usando regressão linear.
    Parâmetros:
        modelo (LinearRegression): Modelo de regressão linear treinado.
        dia_index (int): Índice do dia a ser previsto (31).
    Retorna:
        float: Previsão de vendas para o dia 31.
    """
    logger.info(f"Prevendo vendas para o dia {dia_index + 1}.")

    dia_array = np.array([[dia_index]])
    return modelo.predict(dia_array)[0]

def plotar_vendas(df, media_geral):
    """Plota o gráfico de vendas diárias, média móvel e média geral.
    Parâmetros:
        df (pd.DataFrame): DataFrame com as vendas diárias e média móvel.
        media_geral (float): Média geral de vendas.
    """
    logger.info("Plotando gráfico de vendas.")

    df[['vendas', 'media_movel_7d']].plot(figsize=(10, 5), title='Vendas Diárias e Média Móvel de 7 Dias')
    plt.axhline(media_geral, color='red', linestyle='--', label='Média Geral')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    """Função principal que executa o pipeline de análise de séries temporais."""
    logger.info("Iniciando análise de vendas em série temporal.")

    # 1. Simulação
    df = simular_vendas()

    # 2. Média móvel
    calcular_media_movel(df)

    # 3. Tendência
    tendencia, coef, modelo = identificar_tendencia(df)

    # 4. Dias acima da média
    media_geral, acima_media = dias_acima_da_media(df)

    # 5. Previsão para o dia 31
    previsao_dia_31 = prever_proximo_dia(modelo, len(df))

    # Resultados
    print("=== Análise de Vendas em Série Temporal (30 dias) ===\n")
    print(f"1. Média Geral de Vendas: {media_geral:.2f}")
    print(f"2. Tendência da Série: {tendencia} (coeficiente = {coef:.2f})")
    print(f"3. Dias com vendas acima da média ({media_geral:.2f}):")
    
    for data in acima_media.index:
        print(f"{data.strftime('%Y-%m-%d')} -> {df.loc[data, 'vendas']}")
    print(f"\n4. Previsão para o dia 31: {previsao_dia_31:.2f} vendas")

    # 6. Gráfico
    plotar_vendas(df, media_geral)

if __name__ == '__main__':
    main()
