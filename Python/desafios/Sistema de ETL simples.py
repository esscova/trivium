"""
Desafio Sistema de ETL simples - implementar um mini pipeline de ETL em Python
    1. leitura de dados de um arquivo CSV simulado 
    2. tratamento de dados: normalizar nomes e convertes datas
    3. escrita de dados em outro arquivo JSON

autor: Wellington M Santos
linkedin: in/wellington-moreira-santos

"""

# dependencias
import pandas as pd
from faker import Faker
import logging

# configurações
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


# função criar dados fakes em csv
def criar_dados_csv(qtd:int=10) -> None:
    fake = Faker('pt_BR')
    dados = []
    logger.info(f"Criando {qtd} registros de dados fakes para clientes")
    for _ in range(qtd):
        nome = fake.name().upper()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%d/%m/%Y')
        email = fake.email()
        telefone = fake.phone_number()
        dados.append([nome, data_nascimento, email, telefone])
    
    cabecalho = ['nome', 'data_nascimento', 'email', 'telefone']
    pd.DataFrame(dados, columns=cabecalho).to_csv('clientes.csv', index=False, encoding='utf-8')
    logger.info("Dados fakes criados e salvos em 'clientes.csv'")

# função pipeline ETL
def pipeline_etl(file_path: str = 'clientes.csv') -> None:
    # 1. leitura de dados
    df = pd.read_csv(file_path, dtype=str)
    logger.info(f"Lendo dados do arquivo: {file_path}")

    # 2. tratamento de dados
    logger.info("Iniciando o tratamento de dados")
    df['nome'] = df['nome'].str.capitalize()
    df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], format='%d/%m/%Y')
    df['data_nascimento'] = df['data_nascimento'].dt.strftime('%Y-%m-%d')
    logger.info("Tratamento de dados concluído")

    # 3. escrita de dados
    df.to_json('clientes.json', orient='records', indent=4, force_ascii=False)
    logger.info("Escrita de dados concluída")

# função principal
def main():
    criar_dados_csv(10)  
    pipeline_etl('clientes.csv')  

if __name__ == '__main__':
    main()
    logger.info("Pipeline ETL concluído com sucesso!")