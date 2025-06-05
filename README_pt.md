# Análise de Frequência Alélica para Loci Utilizados em Testes de Paternidade

Este projeto realiza a consolidação e análise de dados genotípicos de STRs (Short Tandem Repeats) utilizados em testes de paternidade. O código coleta arquivos `.txt` contendo os dados dos indivíduos, remove replicações técnicas e gera gráficos de frequência alélica por locus.

## 🚀 Objetivo

- Unificar dados genéticos de múltiplos arquivos.
- Eliminar duplicatas técnicas.
- Calcular frequências alélicas por locus.
- Gerar visualizações gráficas por locus genético.

## 🧰 Tecnologias e Bibliotecas

- Python 3
- pandas
- matplotlib
- seaborn

## 📁 Estrutura Esperada dos Arquivos `.txt`

Cada arquivo deve conter as seguintes colunas:

- `Indivíduo`
- `Lócus`
- `Alelo 1`
- `Alelo 2`

Os arquivos devem estar codificados em UTF-8 e separados por tabulação (`.tsv`).


## 📌 Observações
- O script lida com múltiplos arquivos e ignora erros de leitura sem interromper a execução.
- Útil para análises populacionais e validação de painéis de STRs.
