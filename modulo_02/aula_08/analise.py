import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

people = pd.read_csv("modulo_02/tarefas/aula_08/ifood_people.csv", sep=",")
campaing = pd.read_csv("modulo_02/tarefas/aula_08/ifood_previous_campaing.csv", sep=",")
profile = pd.read_csv("modulo_02/tarefas/aula_08/ifood_purchase_profile.csv", sep=",")

df1 = pd.merge(people, campaing, on = 'ID')
df = pd.merge(df1, profile, on = 'ID')

df['Total_Acepted'] = df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']].sum(axis=1)
df['Age'] = 2024 - df['Year_Birth']

plt.figure(figsize=(10,6))
sns.lineplot(x='Total_Acepted', y='Age', data=df)
plt.title('Relação entre Aceitação de Campanhas e Idade')
plt.show()

# Analisando a relação entre educação e aceitação de campanhas
plt.figure(figsize=(10,6))
sns.barplot(x='Total_Acepted', y='Income', data=df)
plt.title('Relação entre Renda e Aceitação de Campanhas')
plt.show()

# Analisando a relação entre estado civil e aceitação de campanhas
plt.figure(figsize=(10,6))
sns.boxplot(x='Marital_Status', hue='Total_Acepted', data=df)
plt.title('Estado Civil vs Aceitação de Campanhas')
plt.show()

print(df.head())
print(df.describe())