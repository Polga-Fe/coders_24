# Exercícios
# Qual o filme com o maior lucro?
# Qual o filme que deu o maior prejuízo
# Faça uma plotagem(gráfico) que mostre a distribuição do budget em relação ao ano do titulo(title_year)
# Uma plotagem do genero do filme.
# Quais os 10 melhores filmes(olha aí a lista de indicação do FDS)
# Qual o Genero mais popular e menos popular?
# Existe relação entre os melhores filme e seu Budget?
# Quem é o melhor diretor? Existe uma relação de custo associado ao melhor diretor? Ou seja, o melhor diretor baseado na sua analise é também o diretor que mais gasta?
# Mostre num gráfico a quantidade de filmes ao passar do ano
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IMPORTAR DATABASE
df_movies = pd.read_csv('tarefas/aula_06/movies.csv', sep='|', names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews', 'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre'])
colunas = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews', 'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

df_movies[colunas] = df_movies[colunas].replace('?', np.nan)
df_movies['num_critic_for_reviews'] = pd.to_numeric(df_movies['num_critic_for_reviews'], errors='coerce')
df_movies['duration'] = pd.to_numeric(df_movies['duration'], errors='coerce')
df_movies['gross'] = pd.to_numeric(df_movies['gross'], errors='coerce')
df_movies['num_user_for_reviews'] = pd.to_numeric(df_movies['num_user_for_reviews'], errors='coerce')
df_movies['budget'] = df_movies['budget'].str.replace(',', '').astype(float, errors='ignore')
df_movies['title_year'] = pd.to_numeric(df_movies['title_year'], errors='coerce')
print(df_movies.head())

# MAIOR LUCRO
df_movies['profit'] = df_movies['gross'] - df_movies['budget']
info_maior_lucro = df_movies.loc[df_movies['profit'].idxmax()]
filme_com_maior_lucro = info_maior_lucro['movie_title'].strip()
lucro_do_filme = info_maior_lucro['profit']
print(f'Filme com maior lucro: {filme_com_maior_lucro}, com um lucro de ${lucro_do_filme:.2f}')

# MENOR LUCRO
info_maior_preju = df_movies.loc[df_movies['profit'].idxmin()]
filme_com_maior_preju = info_maior_preju['movie_title'].strip()
preju_do_filme = info_maior_preju['profit']
print(f'Filme com maior prejuízo: {filme_com_maior_preju}, com um prejuízo de ${preju_do_filme:.2f}')

# DISTRIBUIÇÃO TITULO X ANO
grafico_budgetxyear = df_movies.dropna(subset=['budget', 'title_year'])

plt.figure(figsize=(10, 6))
plt.scatter(x='title_year', y='budget', data=grafico_budgetxyear)
plt.xlabel('Ano do Título')
plt.ylabel('Budget')
plt.title('Distribuição do Ano e Budget do filme')

# GRAFICO GENEROS
grafico_generoxquantidade = df_movies['genre'].value_counts().reset_index()
grafico_generoxquantidade.columns = ['genre', 'quantidade_filmes']

plt.figure(figsize=(10, 6))

plt.bar(grafico_generoxquantidade['genre'], grafico_generoxquantidade['quantidade_filmes'], color='red')
plt.xlabel('Gêneros')
plt.ylabel('Número de Filmes')
plt.title('Distribuição de Gêneros de Filmes')
plt.show()

# GRAFICO MELHORES FILMES
top_10_filmes = df_movies.sort_values(by='imdb_score', ascending=False).head(10)
print(top_10_filmes[['movie_title', 'director_name', 'title_year', 'imdb_score']])

# GENERO MAIS POPULAR
media_por_genero = df_movies.groupby('genre')['profit'].mean()
genero_mais_popular = media_por_genero.idxmax()
genero_menos_popular = media_por_genero.idxmin()

print(f'Gênero mais popular é de {genero_mais_popular}')
print(f'Gênero menos popular é de {genero_menos_popular}')

# GRAFICO BUDGET X PONTUAÇÃO
grafico_scorexbudget = df_movies.dropna(subset=['imdb_score', 'budget'])

plt.figure(figsize=(10, 6))

plt.scatter(x='imdb_score', y='budget', data=grafico_scorexbudget)

plt.xlabel('Pontuação')
plt.ylabel('Budget')
plt.title('Distribuição da Pontuação em relação ao Budget do filme')

# GRAFICO MEDIA X SCORE
media_por_score = df_movies.groupby('director_name')['imdb_score'].mean()
media_por_budget = df_movies.groupby('director_name')['budget'].mean()

melhor_diretor = media_por_score.idxmax()
budget_melhor_diretor = media_por_budget[melhor_diretor]

diretor_maior_budget = media_por_budget.idxmax()
maior_budget = media_por_budget.max()

print(f'Melhor diretor é do {melhor_diretor} e o seu budget de ${budget_melhor_diretor}')
print(f'O maior budget é do {diretor_maior_budget} e seu budget foi de ${maior_budget}')
print('Logo a relação não faz sentido! Maior budget não significa maior budget')

# GRAFICO ANO X FILME
grafico_anoxfilmes = df_movies['title_year'].value_counts().reset_index()
grafico_anoxfilmes.columns = ['title_year', 'quantidade_filmes']

plt.figure(figsize=(10, 6))

plt.bar(grafico_anoxfilmes['title_year'], grafico_anoxfilmes['quantidade_filmes'], color='blue')
plt.xlabel('Ano')
plt.ylabel('Número de Filmes')
plt.title('Distribuição de Filmes por ano')
plt.show()