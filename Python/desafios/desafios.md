# 10 Desafios Python - Para Cientistas de Dados, Analistas de Dados e Engenheiros de Dados

### 1. **Análise de Vendas com Dicionários e Funções**

Crie um programa que receba dados de vendas (produto, quantidade, preço unitário) em formato de dicionário e calcule:

- Total de vendas por produto
- Produto mais vendido (em quantidade)
- Receita total
- Média de preço por categoria de produto

### 2. **Limpeza e Validação de Dataset**

Desenvolva uma função que receba uma lista de dicionários representando dados de clientes (nome, email, idade, salário) e:

- Remova registros com dados faltantes
- Valide formato de emails usando regex
- Identifique e trate outliers de salário (valores 3x acima/abaixo da média)
- Retorne estatísticas básicas do dataset limpo

### 3. **Sistema de ETL Simples**

Implemente um mini pipeline de ETL que:

- **Extract**: Leia dados de um arquivo CSV simulado (crie os dados)
- **Transform**: Normalize nomes (capitalize), converta datas para formato padrão
- **Load**: Salve os dados transformados em um novo arquivo JSON
- Adicione logs de cada etapa do processo

### 4. **Análise de Séries Temporais Básica**

Crie um programa que simule dados de vendas diárias por 30 dias e calcule:

- Média móvel de 7 dias
- Identificação de tendência (crescente/decrescente)
- Dias com vendas acima da média geral
- Previsão simples para o próximo dia usando regressão linear

### 5. **Agrupamento e Agregação de Dados**

Desenvolva um sistema que processe dados de transações bancárias (cliente, tipo_transacao, valor, data) e gere:

- Saldo total por cliente
- Transações agrupadas por tipo e mês
- Top 5 clientes com maior volume de transações
- Relatório de atividade mensal

### 6. **Detecção de Anomalias em Dados**

Implemente um detector de anomalias que:

- Receba uma lista de valores numéricos (ex: temperaturas, vendas)
- Calcule quartis e identifique outliers usando método IQR
- Implemente detecção usando Z-score
- Compare os dois métodos e retorne um relatório

### 7. **Sistema de Recomendação Simples**

Crie um sistema básico de recomendação que:

- Receba dados de avaliações de usuários para produtos (matriz usuário-produto)
- Calcule similaridade entre usuários usando correlação
- Recomende produtos para um usuário baseado em usuários similares
- Implemente filtros por categoria de produto

### 8. **Processamento de Logs e Métricas**

Desenvolva um analisador de logs que:

- Parse logs de acesso web (IP, timestamp, URL, status_code)
- Identifique IPs mais ativos
- Calcule taxa de erro (status 4xx, 5xx) por hora
- Detecte possíveis ataques (muitas requisições do mesmo IP)
- Gere dashboard textual com métricas

### 9. **Otimização de Estoque com Classes**

Implemente um sistema OOP para gestão de estoque que:

- Classe Produto (nome, categoria, preço, quantidade_minima)
- Classe Estoque com métodos para adicionar/remover produtos
- Cálculo de ponto de reposição baseado em histórico de vendas
- Relatório de produtos em falta ou excesso
- Simulação de cenários (alta/baixa demanda)

### 10. **Pipeline de Qualidade de Dados**

Crie um validador de qualidade de dados que:

- Receba dataset com múltiplas colunas (numérica, texto, data)
- Implemente testes de qualidade: completude, unicidade, formato
- Calcule score de qualidade por coluna e geral
- Gere relatório detalhado com sugestões de correção
- Salve resultados em formato estruturado (JSON/CSV)