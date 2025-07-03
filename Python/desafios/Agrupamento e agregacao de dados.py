"""
    Desafio: Agrupamento e Agregação de Dados
    Este script processa transações bancárias, agrupando e agregando dados para análise.
        1. Calcular saldo total por cliente
        2. Agrupar transações por tipo e mês
        3. Identificar os 5 clientes com maior volume de transações
        4. Gerar relatório de atividade mensal

    autor: Wellington M Santos
    linkedin: in/wellington-moreira-santos
    
    Dependências:
    Python 3.12.4 | Pandas

"""

import pandas as pd

class BankTransactionProcessor:
    def __init__(self, data):
        """Inicializa com DataFrame de transações."""
        self.df = data
        self.df['data'] = pd.to_datetime(self.df['data'])
        self.df['mes_ano'] = self.df['data'].dt.to_period('M')

    def calculate_total_balance(self):
        """Calcula o saldo total por cliente."""
        balance = self.df.groupby('cliente')['valor'].sum().reset_index()
        balance.columns = ['Cliente', 'Saldo_Total']
        return balance.sort_values('Saldo_Total', ascending=False)

    def group_by_type_and_month(self):
        """Agrupa transações por tipo e mês."""
        grouped = self.df.groupby(['mes_ano', 'tipo_transacao']).agg({
            'valor': ['sum', 'count']
        }).reset_index()
        grouped.columns = ['Mes_Ano', 'Tipo_Transacao', 'Valor_Total', 'Quantidade']
        return grouped.sort_values(['Mes_Ano', 'Tipo_Transacao'])

    def top_5_clients_by_volume(self):
        """Identifica top 5 clientes por volume de transações."""
        volume = self.df.groupby('cliente').agg({
            'valor': 'sum',
            'tipo_transacao': 'count'
        }).reset_index()
        volume.columns = ['Cliente', 'Valor_Total', 'Quantidade_Transacoes']
        return volume.sort_values('Quantidade_Transacoes', ascending=False).head(5)

    def monthly_activity_report(self):
        """Gera relatório de atividade mensal."""
        report = self.df.groupby('mes_ano').agg({
            'valor': ['sum', 'mean'],
            'tipo_transacao': ['count', lambda x: x.value_counts().to_dict()]
        }).reset_index()
        report.columns = ['Mes_Ano', 'Valor_Total', 'Valor_Medio', 
                         'Total_Transacoes', 'Distribuicao_Tipos']
        return report

def main():
    # Exemplo de dados
    data = pd.DataFrame({
        'cliente': ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'E'],
        'tipo_transacao': ['Depósito', 'Saque', 'Depósito', 'Saque', 
                          'Depósito', 'Saque', 'Depósito', 'Depósito'],
        'valor': [1000, 500, 2000, 300, 1500, 700, 800, 1200],
        'data': ['2025-01-10', '2025-01-15', '2025-02-01', '2025-02-10',
                 '2025-02-15', '2025-03-01', '2025-03-10', '2025-03-15']
    })

    processor = BankTransactionProcessor(data)

    # relatórios
    print("=== Saldo Total por Cliente ===")
    print(processor.calculate_total_balance())
    
    print("\n=== Transações por Tipo e Mês ===")
    print(processor.group_by_type_and_month())
    
    print("\n=== Top 5 Clientes por Volume ===")
    print(processor.top_5_clients_by_volume())
    
    print("\n=== Relatório de Atividade Mensal ===")
    print(processor.monthly_activity_report())

if __name__ == "__main__":
    main()