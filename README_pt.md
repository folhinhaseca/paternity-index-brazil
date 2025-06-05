{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "29e3d75e",
   "metadata": {},
   "source": [
    "# Análise de Frequência Alélica para Loci Utilizados em Testes de Paternidade\n",
    "\n",
    "Este projeto realiza a consolidação e análise de dados genotípicos de STRs (Short Tandem Repeats) utilizados em testes de paternidade. O código coleta arquivos `.txt` contendo os dados dos indivíduos, remove replicações técnicas e gera gráficos de frequência alélica por locus.\n",
    "\n",
    "## 🚀 Objetivo\n",
    "\n",
    "- Unificar dados genéticos de múltiplos arquivos.\n",
    "- Eliminar duplicatas técnicas.\n",
    "- Calcular frequências alélicas por locus.\n",
    "- Gerar visualizações gráficas por locus genético.\n",
    "\n",
    "## 🧰 Tecnologias e Bibliotecas\n",
    "\n",
    "- Python 3\n",
    "- pandas\n",
    "- matplotlib\n",
    "- seaborn\n",
    "\n",
    "## 📁 Estrutura Esperada dos Arquivos `.txt`\n",
    "\n",
    "Cada arquivo deve conter as seguintes colunas:\n",
    "\n",
    "- `Indivíduo`\n",
    "- `Lócus`\n",
    "- `Alelo 1`\n",
    "- `Alelo 2`\n",
    "\n",
    "Os arquivos devem estar codificados em UTF-8 e separados por tabulação (`.tsv`).\n",
    "\n",
    "\n",
    "## 📌 Observações\n",
    "- O script lida com múltiplos arquivos e ignora erros de leitura sem interromper a execução.\n",
    "- Útil para análises populacionais e validação de painéis de STRs."
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
