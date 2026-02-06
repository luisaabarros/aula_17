import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Conectando os dados
try:
    print('Obtendo os dados...\n')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # 'utf-8', 'iso-8859-1', latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Delimitndo variáveis
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Agrupando e quantificando 
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
    print(df_roubo_veiculo.head())

except Exception as e:
    print(f'Erro ao obter dados {e}')


# Obter informações do padrão de roubos de veículos 
try:
    print('\nObtendo informações do padrão de roubos de veículos')

    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # medidas de tendência central
    media = np.mean(array_roubo_veiculo)
    mediana = np.median(array_roubo_veiculo)
    distancia_media_mediana = (media - mediana) / mediana *100

    print('\nMedidas de Tendência Central:')
    print(f'\nMédia: {media:.3f}\nMediana: {mediana:.3f}\nDistância Média e Mediana: {distancia_media_mediana:.3f}')

except Exception as e:
    print(f'Erro ao obter informações...{e}')



# Obtendo medidas estatísticas
try:

    q1 = np.quantile(array_roubo_veiculo, .25)
    q2 = np.quantile(array_roubo_veiculo, .50)
    q3 = np.quantile(array_roubo_veiculo, .75)

    print('\nMedidas de Posição:')
    print(30*'=')
    print(f'Q1: {q1}\nQ2: {q2}\nQ3: {q3}')

    # Menores
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]

    # Maiores
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMenores')
    print(30*'=')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo'))

    print('\nMaiores')
    print(30*'=')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))

    # Medidas de disperção
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude_total = maximo - minimo

    print('\nPrintando Medidas de Dispersão')
    print(f'\nMáximo: {maximo}')
    print(f'\nMínimo: {minimo}')
    print(f'\nAmplitude Total: {amplitude_total}')

    # IQR = intervalo inter quartil - 50%
    iqr = q3 - q1

    print('\nIntervalo Interquartil')
    print(f'\nIQR: {iqr}')

    # Limite Inferior
    limite_inferior = q1 - (1.5 * iqr)

    # Limite Superior
    limite_superior = q3 + (1.5 * iqr)

    print(f'\nLimite Inferior: \n{limite_inferior}\nLimite Superior: \n{limite_superior}')

    # Outliers Inferiores:
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # Outliers Superiores:
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    print('\nOutliers Inferiores:')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não há outliers inferiores.')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by='oubo_veiculo', ascending=True))

    print('\nOutliers Superiores:')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não há outliers superiores.')
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))


except Exception as e:
    print(f'Erro ao obter medidas estatísticas {e}')



try:
    print('Visualizando dados...')

    plt.subplots(2, 2, figsize=(16, 7))

    plt.subplot(2, 2, 1)
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)

    plt.subplot(2, 2, 2)
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=False, showfliers=False)

    plt.subplot(2, 2, 3)
    plt.text(0.1, 0.9, f'Média: {media}', fontsize=12)
    plt.text(0.1, 0.8, f'Mediana: {mediana}', fontsize=12)
    plt.text(0.1, 0.7, f'Distância: {distancia_media_mediana}', fontsize=12)
    plt.text(0.1, 0.6, f'Menor Valor: {minimo}', fontsize=12)
    plt.text(0.1, 0.5, f'Limite Inferior: {limite_inferior}', fontsize=12)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=12)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=12)
    plt.text(0.1, 0.2, f'Limite Superior: {limite_superior}', fontsize=12)
    plt.text(0.1, 0.1, f'Maior Valor: {maximo}', fontsize=12)


    plt.text(0.6, 0.9, f'Amplitude: {amplitude_total}', fontsize=12)
    plt.text(0.6, 0.8, f'IQR: {iqr}', fontsize=12)


    plt.show()


except Exception as e:
    print(f'Erro na plotagem do painél: {e}')





# É A MESMA COISA DE CIMA, MAS COPIEI 2X PARA GRAVAR
# try:
#     # pip install matplotlib
#     print('Visualizando os dados...')

#     plt.subplots(2, 2, figsize=(16, 7) )
#     plt.suptitle('Análise de Boxplot')

#     plt.subplot(2, 2, 1 )
#     plt.boxplot(array_roubo_veiculo, vert=False, showfliers=False, showmeans=True)
#     plt.title('Gráfico Boxplot')

#     plt.subplot(2, 2, 2 )

#     plt.subplot(2, 2, 3 )

#     plt.subplot(2, 2, 4 )

#     plt.show()



# except Exception as e:
#     print(f'Erro ao plotar o gráfico: {e}')
