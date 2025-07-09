"""
@description: Funções utilitárias para desafios.
"""

# Dependencias
import random
from datetime import datetime, timedelta
import pandas as pd

# função para gerar dados de logs de acesso web e persistir em um arquivo .log
def gerar_logs(n_registros: int=1000) -> None:
    """
        Gera um arquivo de log de acesso web com dados simulados.
        :param n_registros: Número de registros a serem gerados (padrão: 1000)
        :return: None
    """
    ips = [f"192.168.0.{i}" for i in range(1, 21)] + ["10.0.0.1", "172.16.0.1"]
    urls = ["/", "/login", "/home", "/dashboard", "/api", "/produtos", "/busca"]
    status_codes = [200]*80 + [404]*10 + [500]*5 + [403]*5  # 80% sucesso, 20% erro
    now = datetime.now().replace(minute=0, second=0, microsecond=0)

    dados = []
    for _ in range(n_registros):
        ip = random.choice(ips)
        url = random.choice(urls)
        status = random.choice(status_codes)
        delta = timedelta(minutes=random.randint(0, 1440))  # em 24 horas
        timestamp = now - delta
        dados.append({
            "ip": ip,
            "timestamp": timestamp.replace(tzinfo=None),
            "url": url,
            "status": status
        })

    df = pd.DataFrame(dados)
    df.to_csv("./data/access.log", sep="\t", index=False)

if __name__ == "__main__":
    gerar_logs(1000)  # Gera 1000 registros de log
    print("Arquivo de log gerado com sucesso em './data/access.log'.")