# analisador_frequencia_alelica.py

import os
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set(style='whitegrid')

def ler_arquivos_txt(pasta):
    todos = []
    erros = []

    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.txt'):
            try:
                df = pd.read_csv(os.path.join(pasta, arquivo), sep='\t')
                df['arquivo'] = arquivo
                todos.append(df)
            except Exception as e:
                print(f"Erro ao ler {arquivo}: {e}")
                erros.append(arquivo)

    return pd.concat(todos, ignore_index=True), erros

def limpar_replicatas(df):
    return df.drop_duplicates(subset=['Indivíduo', 'Lócus', 'Alelo 1', 'Alelo 2'])

def contar_frequencias(df):
    locus_freq = {}
    for locus, grupo in df.groupby('Lócus'):
        alelos = grupo[['Alelo 1', 'Alelo 2']].values.flatten()
        contagem = dict(Counter(alelos))
        total = sum(contagem.values())
        freq = {alelo: round(contagem[alelo]/total, 4) for alelo in contagem}
        locus_freq[locus] = freq
    return locus_freq

def plotar_frequencias(freq_dict, saida='graficos'):
    Path(saida).mkdir(exist_ok=True)
    for locus, freq in freq_dict.items():
        plt.figure(figsize=(10, 5))
        sns.barplot(x=list(freq.keys()), y=list(freq.values()), color='skyblue')
        plt.title(f'Frequência Alélica - {locus}')
        plt.ylabel('Frequência')
        plt.xlabel('Alelo')
        plt.tight_layout()
        plt.savefig(f'{saida}/{locus}_frequencia.png')
        plt.close()

def executar_pipeline(pasta_txt):
    df, erros = ler_arquivos_txt(pasta_txt)
    if erros:
        print("Arquivos com erro:", erros)

    df_limpo = limpar_replicatas(df)
    freq_dict = contar_frequencias(df_limpo)
    plotar_frequencias(freq_dict)
    print("Análise concluída. Gráficos salvos na pasta 'graficos'.")

if __name__ == '__main__':
    pasta = input("Digite o caminho da pasta com os arquivos .txt: ")
    executar_pipeline(pasta)
