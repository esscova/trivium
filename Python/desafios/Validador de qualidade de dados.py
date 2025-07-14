"""
# Validador de Qualidade de Dados
@author: Wellington M Santos
@date: 2025-07-14
@description: Validador de qualidade de dados para análise de datasets.
@version: 1.1
@dependencies: pandas, json, datetime
@usage: Execute este script para validar a qualidade de um dataset e gerar um relatório.
"""

import pandas as pd
import json
from datetime import datetime

# === Configurações ===
FORMATO_DATA_PADRAO = "%Y-%m-%d"
TERMOS_DATA = ["data", "nascimento", "dia"]

# === Funções de validação ===
def validar_completude(coluna):
    total = len(coluna)
    nulos = coluna.isnull().sum()
    return {
        "total_linhas": total,
        "nulos": nulos,
        "porcentagem_nulos": round((nulos / total) * 100, 2),
        "completo": nulos == 0
    }

def validar_unicidade(coluna):
    duplicados = coluna.duplicated().sum()
    return {
        "duplicados": duplicados,
        "unico": duplicados == 0
    }

def validar_formato_data(coluna):
    def eh_data_valida(valor):
        if pd.isna(valor) or str(valor).strip().lower() in ("", "nan", "none"):
            return False
        try:
            datetime.strptime(str(valor), FORMATO_DATA_PADRAO)
            return True
        except ValueError:
            return False

    validos = coluna.apply(eh_data_valida).sum()
    total = len(coluna)
    invalidos = total - validos

    return {
        "validos": validos,
        "invalidos": invalidos,
        "formato_correto": invalidos == 0
    }

def coluna_parece_data(nome_coluna):
    return any(t in nome_coluna.lower() for t in TERMOS_DATA)

# === Score e sugestões ===
def calcular_score(validacoes):
    total = 0
    pontos = 0
    if "completo" in validacoes.get("completude", {}):
        pontos += int(validacoes["completude"]["completo"])
        total += 1
    if "unico" in validacoes.get("unicidade", {}):
        pontos += int(validacoes["unicidade"]["unico"])
        total += 1
    if "formato_correto" in validacoes.get("formato_data", {}):
        pontos += int(validacoes["formato_data"]["formato_correto"])
        total += 1
    return round(pontos / total, 2) if total > 0 else 0.0

def sugerir_correcao(resultado_coluna):
    sugestoes = []
    if not resultado_coluna["validacoes"]["completude"].get("completo", True):
        sugestoes.append("→ Preencher valores ausentes (média, moda, interpolação, etc.)")
    if not resultado_coluna["validacoes"]["unicidade"].get("unico", True):
        sugestoes.append("→ Remover duplicatas ou criar identificador único")
    if resultado_coluna["validacoes"].get("formato_data", {}).get("formato_correto") is False:
        sugestoes.append(f"→ Padronizar datas no formato {FORMATO_DATA_PADRAO}")
    return sugestoes or ["Nenhuma sugestão necessária."]

# === Geração e salvamento de relatório ===
def gerar_relatorio(df):
    relatorio = {}
    score_total = 0
    total_colunas = len(df.columns)

    for col in df.columns:
        print(f"\n🔍 Coluna: {col}")
        tipo = str(df[col].dtype)
        print(f"Tipo: {tipo}")

        validacoes = {
            "completude": validar_completude(df[col]),
            "unicidade": validar_unicidade(df[col])
        }

        if tipo.startswith("object") and coluna_parece_data(col):
            validacoes["formato_data"] = validar_formato_data(df[col])
        else:
            validacoes["formato_data"] = {"aplicavel": False}

        score = calcular_score(validacoes)
        score_total += score

        print(f"📊 Score: {score:.2f}")

        relatorio[col] = {
            "tipo_dado": tipo,
            "validacoes": validacoes,
            "score": score
        }

    score_geral = round(score_total / total_colunas, 2)
    relatorio["score_geral"] = score_geral
    print(f"\n📈 Score geral do dataset: {score_geral:.2f}")
    return relatorio

def salvar_relatorio(relatorio, formato="json"):
    if formato == "json":
        with open("./data/relatorio_qualidade.json", "w", encoding="utf-8") as f:
            json.dump(relatorio, f, indent=4, default=str)
        print("✅ Relatório salvo como relatorio_qualidade.json")

    elif formato == "csv":
        df_relatorio = pd.DataFrame.from_dict(
            {col: {k: v for k, v in val.items() if k != "validacoes"} for col, val in relatorio.items() if col != "score_geral"},
            orient="index"
        )
        df_relatorio["score"] = df_relatorio["score"].astype(float)
        df_relatorio.to_csv("relatorio_qualidade.csv")
        print("✅ Relatório salvo como relatorio_qualidade.csv")

    else:
        print("Formato de arquivo inválido. Escolha 'json' ou 'csv'.")

# === Execução principal ===
if __name__ == "__main__":
    # Exemplo de dataset
    dados = {
        "ID": [1, 2, None, 4],
        "Nome": ["Ana", "Carlos", "", "Mariana"],
        "Data_Nascimento": ["2000-01-01", "1995-03-15", "invalido", "2005-12-30"],
        "Salario": [3000, 4500, 2500, 7000]
    }
    df = pd.DataFrame(dados)

    relatorio = gerar_relatorio(df)

    for col, resultado in relatorio.items():
        if col != "score_geral":
            resultado["sugestoes"] = sugerir_correcao(resultado)

    salvar_relatorio(relatorio, formato="json")