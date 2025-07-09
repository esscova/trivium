"""
@author: Wellington M Santos
@title: Processamento de logs e métricas de acesso web
@description: Este script processa logs de acesso web, extrai métricas relevantes e gera um dashboard textual com informações sobre acessos, erros e possíveis ataques.
@dependencies: Python 3.x | pandas | datetime | re
@usage: Execute o script em um ambiente Python com as dependências instaladas. Certifique-se de ter um arquivo de log chamado "access.log" no mesmo diretório.
@notes: O formato do log deve seguir o padrão comum de logs de servidores web, como Apache ou Nginx.
@version: 1.0
@date: 2025-07-09
"""

# Dependências
import re
from datetime import datetime, timedelta
import pandas as pd

# Funções

# === 1. Função de parsing dos logs ===

def parse_linha_log(linha):
    padrao = r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* \[(?P<timestamp>.*?)\] "(?:GET|POST|PUT|DELETE) (?P<url>\S+) HTTP/.*" (?P<status>\d{3})'
    match = re.match(padrao, linha)
    if match:
        dados = match.groupdict()
        dados["timestamp"] = datetime.strptime(dados["timestamp"], "%d/%b/%Y:%H:%M:%S %z")
        dados["status"] = int(dados["status"])
        return dados
    return None

# === 2. IPs mais ativos ===

def top_ips(df, n=5):
    return df["ip"].value_counts().head(n)

# === 3. Taxa de erro por hora ===

def taxa_erro_por_hora(df):
    df['hora'] = df['timestamp'].dt.strftime('%Hh')
    df['erro'] = df['status'].between(400, 599)
    return df.groupby('hora')['erro'].mean().mul(100).round(2)

# === 4. Detectar possíveis ataques ===

def detectar_ataques(df, limite=100, janela_min=5):
    df_sorted = df.sort_values("timestamp")
    suspeitos = set()

    for ip, grupo in df_sorted.groupby("ip"):
        timestamps = grupo["timestamp"].tolist()
        for i in range(len(timestamps)):
            janela = timestamps[i:i+limite]
            if len(janela) < limite:
                break
            if (janela[-1] - janela[0]) <= timedelta(minutes=janela_min):
                suspeitos.add(ip)
                break

    return suspeitos

# === 5. Dashboard textual ===

def gerar_dashboard(df):
    total = len(df)
    inicio = df["timestamp"].min()
    fim = df["timestamp"].max()

    print("\n==== Relatório de Acessos Web ====\n")
    print(f"Total de requisições: {total}")
    print(f"Período: {inicio} até {fim}\n")

    print("Top 5 IPs mais ativos:")
    for ip, qtd in top_ips(df).items():
        print(f"- {ip} → {qtd} requisições")
    
    print("\nTaxa de erro por hora (4xx + 5xx):")
    taxa_erro = taxa_erro_por_hora(df)
    for hora, taxa in taxa_erro.items():
        print(f"{hora}: {taxa:.2f}%")
    
    suspeitos = detectar_ataques(df)
    if suspeitos:
        print("\nPossíveis ataques detectados:")
        for ip in suspeitos:
            print(f"- {ip} → muitas requisições em poucos minutos")
    else:
        print("\nNenhum padrão de ataque identificado.")

# === MAIN ===

def main():
    try:
        df = pd.read_csv("./data/access.log", sep="\t")
        if df.empty:
            print("Arquivo de log vazio.")
            return
        # Converte tipos
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['status'] = df['status'].astype(int)
        gerar_dashboard(df)
    except FileNotFoundError:
        print("Arquivo de log './data/access.log' nao encontrado.")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo de log: {e}")
        return

if __name__ == "__main__":
    main()
