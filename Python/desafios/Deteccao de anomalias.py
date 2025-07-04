"""
Desafio: Detecção de Anomalias com IQR e Z-score
Este script implementa um detector de anomalias usando os métodos IQR (Interquartile Range) e Z-score.
    1. Detectar outliers usando IQR
    2. Detectar outliers usando Z-score
    3. Comparar os dois métodos
    4. Gerar relatório detalhado com estatísticas e recomendações

    autor: Wellington M Santos
    linkedin: in/wellington-moreira-santos

    Dependências:
    Python 3.12.4 | NumPy 
"""
import numpy as np
from typing import List, Dict, Any

class DetectorAnomalias:
    """
    Classe para detecção de anomalias usando métodos IQR e Z-score
    """
    
    def __init__(self, dados: List[float]):
        """
        Inicializa o detector com os dados
        
        Args:
            dados: Lista de valores numéricos
        """
        self.dados = np.array(dados)
        self.n = len(dados)
        
        # Estatísticas básicas
        self.media = np.mean(self.dados)
        self.mediana = np.median(self.dados)
        self.desvio_padrao = np.std(self.dados)
        
        # Quartis
        self.q1 = np.percentile(self.dados, 25)
        self.q3 = np.percentile(self.dados, 75)
        self.iqr = self.q3 - self.q1
        
    def detectar_outliers_iqr(self, fator: float = 1.5) -> Dict[str, Any]:
        """
        Detecta outliers usando método IQR (Interquartile Range)
        
        Args:
            fator: Multiplicador para definir os limites (padrão 1.5)
            
        Returns:
            Dicionário com informações sobre outliers
        """
        # Limites para outliers
        limite_inferior = self.q1 - fator * self.iqr
        limite_superior = self.q3 + fator * self.iqr
        
        # Identificar outliers
        outliers_mask = (self.dados < limite_inferior) | (self.dados > limite_superior)
        outliers = self.dados[outliers_mask]
        indices_outliers = np.where(outliers_mask)[0]
        
        # Classificar outliers
        outliers_inferiores = self.dados[self.dados < limite_inferior]
        outliers_superiores = self.dados[self.dados > limite_superior]
        
        return {
            'metodo': 'IQR',
            'limite_inferior': limite_inferior,
            'limite_superior': limite_superior,
            'outliers': outliers.tolist(),
            'indices_outliers': indices_outliers.tolist(),
            'outliers_inferiores': outliers_inferiores.tolist(),
            'outliers_superiores': outliers_superiores.tolist(),
            'total_outliers': len(outliers),
            'percentual_outliers': (len(outliers) / self.n) * 100,
            'fator_usado': fator
        }
    
    def detectar_outliers_zscore(self, threshold: float = 2.0) -> Dict[str, Any]:
        """
        Detecta outliers usando método Z-score
        
        Args:
            threshold: Limiar para considerar outlier (padrão 2.0)
            
        Returns:
            Dicionário com informações sobre outliers
        """
        # Calcular Z-scores
        z_scores = np.abs((self.dados - self.media) / self.desvio_padrao)
        
        # Identificar outliers
        outliers_mask = z_scores > threshold
        outliers = self.dados[outliers_mask]
        indices_outliers = np.where(outliers_mask)[0]
        z_scores_outliers = z_scores[outliers_mask]
        
        # Classificar outliers
        outliers_inferiores = self.dados[(self.dados < self.media) & outliers_mask]
        outliers_superiores = self.dados[(self.dados > self.media) & outliers_mask]
        
        return {
            'metodo': 'Z-score',
            'threshold': threshold,
            'outliers': outliers.tolist(),
            'indices_outliers': indices_outliers.tolist(),
            'z_scores_outliers': z_scores_outliers.tolist(),
            'outliers_inferiores': outliers_inferiores.tolist(),
            'outliers_superiores': outliers_superiores.tolist(),
            'total_outliers': len(outliers),
            'percentual_outliers': (len(outliers) / self.n) * 100,
            'z_scores_todos': z_scores.tolist()
        }
    
    def comparar_metodos(self, fator_iqr: float = 1.5, threshold_zscore: float = 2.0) -> Dict[str, Any]:
        """
        Compara os dois métodos de detecção de anomalias
        
        Args:
            fator_iqr: Fator para método IQR
            threshold_zscore: Threshold para método Z-score
            
        Returns:
            Dicionário com comparação dos métodos
        """
        resultados_iqr = self.detectar_outliers_iqr(fator_iqr)
        resultados_zscore = self.detectar_outliers_zscore(threshold_zscore)
        
        # Outliers em comum
        outliers_iqr = set(resultados_iqr['indices_outliers'])
        outliers_zscore = set(resultados_zscore['indices_outliers'])
        
        outliers_comum = outliers_iqr.intersection(outliers_zscore)
        outliers_apenas_iqr = outliers_iqr - outliers_zscore
        outliers_apenas_zscore = outliers_zscore - outliers_iqr
        
        return {
            'iqr': resultados_iqr,
            'zscore': resultados_zscore,
            'comparacao': {
                'outliers_comum': list(outliers_comum),
                'outliers_apenas_iqr': list(outliers_apenas_iqr),
                'outliers_apenas_zscore': list(outliers_apenas_zscore),
                'concordancia': len(outliers_comum) / max(len(outliers_iqr | outliers_zscore), 1) * 100,
                'total_outliers_iqr': len(outliers_iqr),
                'total_outliers_zscore': len(outliers_zscore),
                'total_outliers_comum': len(outliers_comum)
            }
        }
    
    def gerar_relatorio(self, fator_iqr: float = 1.5, threshold_zscore: float = 2.0) -> str:
        """
        Gera relatório completo da análise de anomalias
        
        Args:
            fator_iqr: Fator para método IQR
            threshold_zscore: Threshold para método Z-score
            
        Returns:
            String com relatório formatado
        """
        comparacao = self.comparar_metodos(fator_iqr, threshold_zscore)
        
        relatorio = f"""
========================================
        RELATÓRIO DE DETECÇÃO DE ANOMALIAS
========================================

📊 ESTATÍSTICAS DESCRITIVAS:
   • Total de observações: {self.n}
   • Média: {self.media:.2f}
   • Mediana: {self.mediana:.2f}
   • Desvio padrão: {self.desvio_padrao:.2f}
   • Q1: {self.q1:.2f}
   • Q3: {self.q3:.2f}
   • IQR: {self.iqr:.2f}

🔍 MÉTODO IQR (Fator: {fator_iqr}):
   • Limite inferior: {comparacao['iqr']['limite_inferior']:.2f}
   • Limite superior: {comparacao['iqr']['limite_superior']:.2f}
   • Outliers detectados: {comparacao['iqr']['total_outliers']}
   • Percentual de outliers: {comparacao['iqr']['percentual_outliers']:.1f}%
   • Valores outliers: {comparacao['iqr']['outliers']}

📈 MÉTODO Z-SCORE (Threshold: {threshold_zscore}):
   • Outliers detectados: {comparacao['zscore']['total_outliers']}
   • Percentual de outliers: {comparacao['zscore']['percentual_outliers']:.1f}%
   • Valores outliers: {comparacao['zscore']['outliers']}

⚖️ COMPARAÇÃO DOS MÉTODOS:
   • Outliers em comum: {comparacao['comparacao']['total_outliers_comum']}
   • Apenas IQR: {comparacao['comparacao']['total_outliers_iqr'] - comparacao['comparacao']['total_outliers_comum']}
   • Apenas Z-score: {comparacao['comparacao']['total_outliers_zscore'] - comparacao['comparacao']['total_outliers_comum']}
   • Taxa de concordância: {comparacao['comparacao']['concordancia']:.1f}%

💡 RECOMENDAÇÕES:
   • IQR é mais robusto para distribuições assimétricas
   • Z-score assume distribuição normal dos dados
   • Para dados não-normais, prefira IQR
   • Para dados normais, ambos métodos são eficazes
   • Concordância alta ({comparacao['comparacao']['concordancia']:.1f}%) indica outliers consistentes

========================================
        """
        
        return relatorio

# Exemplo de uso
if __name__ == "__main__":
    # Dados de exemplo (temperaturas)
    temperaturas = [
        20.5, 21.2, 19.8, 22.1, 20.9, 21.5, 19.9, 22.3, 20.7, 21.8,
        35.2,  # outlier superior
        22.0, 21.1, 20.3, 21.9, 20.8, 21.6, 22.2, 20.4, 21.3,
        5.1,   # outlier inferior
        21.7, 20.6, 22.4, 21.0, 20.2, 21.4, 19.7, 22.5, 20.1, 21.8
    ]
    
    # Criar detector
    detector = DetectorAnomalias(temperaturas)
    
    # Gerar relatório
    print(detector.gerar_relatorio())
    
    # Exemplo com dados de vendas
    print("\n" + "="*50)
    print("EXEMPLO COM DADOS DE VENDAS")
    print("="*50)
    
    vendas = [
        1200, 1350, 1180, 1420, 1290, 1380, 1150, 1450, 1320, 1390,
        2800,  # outlier superior (promoção especial)
        1410, 1250, 1330, 1370, 1280, 1400, 1460, 1240, 1360,
        300,   # outlier inferior (dia de greve)
        1430, 1270, 1440, 1300, 1220, 1410, 1170, 1480, 1210, 1390
    ]
    
    detector_vendas = DetectorAnomalias(vendas)
    print(detector_vendas.gerar_relatorio())
    
    # Comparação detalhada
    print("\n" + "="*50)
    print("ANÁLISE DETALHADA - TEMPERATURAS")
    print("="*50)
    
    comparacao = detector.comparar_metodos()
    
    print(f"Outliers detectados por IQR: {comparacao['iqr']['indices_outliers']}")
    print(f"Valores: {[temperaturas[i] for i in comparacao['iqr']['indices_outliers']]}")
    
    print(f"\nOutliers detectados por Z-score: {comparacao['zscore']['indices_outliers']}")
    print(f"Valores: {[temperaturas[i] for i in comparacao['zscore']['indices_outliers']]}")
    
    print(f"\nOutliers em comum: {comparacao['comparacao']['outliers_comum']}")
    print(f"Valores: {[temperaturas[i] for i in comparacao['comparacao']['outliers_comum']]}")