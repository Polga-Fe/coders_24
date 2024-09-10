# Exercícios
# ======|| Utilizando o DataFrame (alunos3.csv) calcule a média das provas em uma nova coluna chamada (Media_provas) ||======
    # Quem foram os alunos que obtiveram a maior e a menor média
    # Agora una este dataframe com o cadastro_alunos.xlsx
    # Qual a média entre as Media_provas dentro do público feminino? e masculino?
    # Qual a média de idade das pessoas que obtiveram Media_provas maior ou igual a 7?
    # Qual das cidades possui o maior média de Media_provas? E qual é este valor?

import numpy as np
import pandas as pd

# IMPORT ARQUIVO ALUNOS COMO TABELA
df_notas = pd.read_csv('tarefas/aula_05/aulos3.csv', sep=';')

# ORGANIZAR VALORES NA TABELA
df_notas['Prova_1'] = df_notas['Prova_1'].str.replace(',', '.').astype(float)
df_notas['Prova_2'] = df_notas['Prova_2'].str.replace(',', '.').astype(float)
df_notas['Prova_3'] = df_notas['Prova_3'].str.replace(',', '.').astype(float)
df_notas['Prova_4'] = df_notas['Prova_4'].astype(float)

# ADICIONAR MEDIA
df_notas['Media'] = df_notas[['Prova_1', 'Prova_2', 'Prova_3', 'Prova_4']].mean(axis=1)
df_notas = df_notas.round(2)

# MAIOR E MENOR MEDIA
df_maxMedia = df_notas.max()
df_minMedia = df_notas.min()

# IMPORT ARQUIVO CADASTRO_ALUNOS COMO TABELA
df_registro = pd.read_excel('tarefas/aula_05/cadastro_alunos.xlsx')

# JUNTAR DADOS DAS TABELAS
df_alunos = pd.merge(df_registro, df_notas, on='RA')

# MEDIA DAS NOTAS POR SEXO
notasFem = df_alunos[df_alunos['Sexo'] == 'Feminino']
mediaFem = notasFem['Media'].mean(axis=0)

notasMasc = df_alunos[df_alunos['Sexo'] == 'Masculino']
mediaMasc = notasMasc['Media'].mean(axis=0)

# DEFINIR IDADE MEDIA DOS APROVADOS
aprovados = df_alunos[df_alunos['Media'] >= 7]
df_mediaIdade = aprovados['Idade'].mean()

# CIDADES COM MAIOR MEDIA DE APROVADOS
mediaCidade = df_alunos.groupby('Cidade')['Media'].mean()
maxCidade = mediaCidade.idxmax()
maxMediaCidade = mediaCidade.max()


# IMPRIMIR RESULTADOS
print(df_notas, '\n')
print(f'O aluno com MAIOR media foi: \n{df_maxMedia}')
print(f'O aluno com MENOR media foi: \n{df_minMedia}')

print(df_registro, '\n')

print(df_alunos, '\n')
print(f'Média das notas FEMININAS: {mediaFem.round(1)}')
print(f'Média das notas MASCULINAS: {mediaMasc.round(1)}')
print(f'Media da idade dos aprovados: {df_mediaIdade}')
print(f'Cidade com maior media: {maxCidade} \nMedia: {maxMediaCidade.round(2)}')
