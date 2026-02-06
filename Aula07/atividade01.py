import pandas as pd
import numpy as np

try:
    print('Obtendo os dados...\n')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    df_estelionato = df_ocorrencias[['mes_ano', 'estelionato']]

    df_estelionato = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()

    print(df_estelionato)

except Exception as e:
    print(f'Erro ao obter dados: {e}')



try:
    print('Verificando padrão de distribuição:\n')

    array_estelionato = np.array(df_estelionato['estelionato'])
    
    media = np.mean(array_estelionato)
    mediana = np.median(array_estelionato)
    distancia_media_mediana = (media - mediana) / mediana * 100

    print('\nMedidas de Tendência Central:')
    print(f'Média: {media:.2f}\nMediana: {mediana:.2f}\nDistância Média Mediana: {distancia_media_mediana:.2f}')

except Exception as e:
    print(f'Erro 1 {e}')



try:
    print('Quartis:\n')

    q1 = np.quantile(array_estelionato, .25)
    q2 = np.quantile(array_estelionato, .50)
    q3 = np.quantile(array_estelionato, .75)

    print(f'\nQ1: {q1}\nQ2: {q2}\nQ3: {q3}')

except Exception as e:
    print(f'Erro 2 {e}')



try:
    print('\nObtendo maiores e menores:')

    df_estelionato_menores = df_estelionato[df_estelionato['estelionato'] < q1]

    df_estelionato_maiores = df_estelionato[df_estelionato['estelionato'] > q3]

    print('\nMenores:')
    print(df_estelionato_menores.sort_values(by='estelionato').head())

    print('\nMaiores')
    print(df_estelionato_maiores.sort_values(by='estelionato', ascending=False).head())

except Exception as e:
    print(f'Erro ao obter maiores e menores: {e}')



try:
    print('\nObtendo Medidas de Dispersão:\n')
    maximo = np.max(array_estelionato)
    minimo = np.min(array_estelionato)
    amplitude_total = maximo - minimo

    print(f'Máximo: {maximo}\nMínimo: {minimo}\nAmplitude Total: {amplitude_total}')



except Exception as e:
    print(f'Erro ao encontrar medidas de dispersão: {e}')