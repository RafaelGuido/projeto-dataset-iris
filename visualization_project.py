import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import networkx as nx
import geopandas as gpd

# Carregar o dataset (substitua pelo seu dataset)
# dataset = pd.read_csv('data/seu_dataset.csv')

# Exemplo usando um dataset público
dataset = sns.load_dataset('iris')

# Visualização com gráficos da Estatística Descritiva
plt.figure(figsize=(10, 6))
sns.countplot(x='species', data=dataset)
plt.title('Distribuição das Espécies')
plt.show()

# Visualização de Informação Temporal (exemplo fictício, ajustar conforme seu dataset)
plt.figure(figsize=(10, 6))
sns.lineplot(data=dataset)
plt.title('Visualização Temporal (exemplo fictício)')
plt.show()

# Visualização de Informação Geográfica (ajuste conforme seu dataset)
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# world.plot()
# plt.title('Mapa Coroplético (exemplo fictício)')
# plt.show()

# Visualização de Informação Hierárquica
fig = px.treemap(dataset, path=['species'], values='sepal_length')
fig.update_layout(title='Treemap das Espécies por Comprimento das Sépalas')
fig.show()

# Visualização de Redes e Grafos (exemplo fictício, ajustar conforme seu dataset)
G = nx.karate_club_graph()
nx.draw(G, with_labels=True)
plt.title('Grafo Node-Link (exemplo fictício)')
plt.show()