# desafio Python: Limpeza e Validação de Dataset
# autor: Wellington M Santos
# linkedin: in/wellington-moreira-santos


import pandas as pd
import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))

def limpar_e_validar_dados(df):
    """
    Função para limpar e validar dados de clientes.

    Parâmetros:
    df (DataFrame): DataFrame contendo os dados dos clientes.

    Retorna:
    tuple: DataFrame limpo e estatísticas básicas.
    """
    # Removendo registros com dados faltantes
    df_limpo = df.dropna()

    # Aplicando a validação de e-mail e filtrando registros inválidos
    df_limpo = df_limpo[df_limpo['email'].apply(validar_email)]

    # Calculando a média e o desvio padrão dos salários para identificar outliers
    media_salario = df_limpo['salario'].mean()
    desvio_padrao_salario = df_limpo['salario'].std()

    # Definindo limites para outliers (3x acima/abaixo da média)
    limite_inferior = media_salario - 3 * desvio_padrao_salario
    limite_superior = media_salario + 3 * desvio_padrao_salario

    # Filtrando outliers de salário
    df_limpo = df_limpo[(df_limpo['salario'] >= limite_inferior) & (df_limpo['salario'] <= limite_superior)]

    # Calculando estatísticas básicas do dataset limpo
    estatisticas = df_limpo.describe()

    return df_limpo, estatisticas

if __name__ == "__main__":
    import random
    from faker import Faker
    fake = Faker()
    
    # Gerando dados de clientes com Faker
    dados_clientes_faker = []

    for i in range(50):
        nome = fake.name()

        # Gerando emails, alguns inválidos
        if i % 7 == 0:
            email = nome.lower().replace(' ', '.')
        else:
            email = f"{nome.lower().replace(' ', '.')}@exemplo.com"

        # Gerando idades, algumas faltando
        idade = random.randint(18, 70) if i % 5 != 0 else None

        # Gerando salários, alguns outliers
        if i % 10 == 0:
            salario = random.choice([50000, 100000])  # Outliers altos
        elif i % 11 == 0:
            salario = random.choice([500, 1000])  # Outliers baixos
        else:
            salario = random.randint(2000, 20000)

        # Adicionando ao dataset, alguns registros com dados faltantes
        if i % 4 == 0:
            dados_clientes_faker.append({
                "nome": nome,
                "email": email,
                "idade": idade
                # Salário faltando
            })
        else:
            dados_clientes_faker.append({
                "nome": nome,
                "email": email,
                "idade": idade,
                "salario": salario
            })

    # Criando um DataFrame a partir dos dados gerados com Faker
    df_clientes = pd.DataFrame(dados_clientes_faker)

    # Relatórios antes da limpeza
    print("Relatório Antes da Limpeza:")
    print(df_clientes.info())
    print("\nEstatísticas Iniciais:")
    print(df_clientes.describe())

    # Chamando a função para limpar e validar os dados
    df_limpo_result, estatisticas_result = limpar_e_validar_dados(df_clientes)

    # Relatórios após a limpeza
    print("\nRelatório Após a Limpeza:")
    print(df_limpo_result.info())
    print("\nEstatísticas Finais:")
    print(estatisticas_result)

    # Exibindo os primeiros registros dos dados limpos
    print("\nDados Limpos (Primeiros 5):")
    print(df_limpo_result.head())
