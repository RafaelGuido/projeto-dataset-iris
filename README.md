# Projeto

## Visualização da Informação

### Esse projeto consiste em apresentar uma implementação, em Python, da visualização de informações presentes em um dataset usando ao menos três técnicas.

## Passo a passo

### Instalar o Python e VSCode:

- [python.org](https://www.python.org)
- [code.visualstudio.com](https://code.visualstudio.com)

### Instalar Extensões Necessárias no VSCode:

- Instale a extensão "Python" da Microsoft.

### Criar um Novo Projeto:

- Crie uma nova pasta para o projeto em seu computador.
- Abra essa pasta no VSCode.

### Configurar um Ambiente Virtual (opcional, mas recomendado):

- Abra o terminal integrado no VSCode.
- Navegue até a pasta do projeto e crie um ambiente virtual: 
  ```sh
  python -m venv venv
  ```
- Ative o ambiente virtual no Windows: 
  ```sh
  .\venv\Scripts\activate
  ```
- Ative o ambiente virtual no MacOS/Linux: 
  ```sh
  source venv/bin/activate
  ```

### Instalar as Bibliotecas Necessárias:

- Com o ambiente virtual ativado, instale as bibliotecas necessárias usando o terminal:
  ```sh
  pip install pandas matplotlib seaborn plotly networkx geopandas
  ```

### Criar o Arquivo de Código:

- Crie um novo arquivo Python (.py) na pasta do projeto. Por exemplo, `visualization_project.py`.

### Escrever o Código de Visualização:

- Copie e cole o exemplo de código fornecido no arquivo `visualization_project.py`.

```python
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
```

### Executar o Código:

- No terminal integrado do VSCode, certifique-se de que seu ambiente virtual está ativado.

- Execute o arquivo de código:
  ```sh
  python visualization_project.py
  ```

### Informações:

- O dataset de exemplo utilizado no código é o famoso dataset "Iris", que é amplamente utilizado para demonstração em ciência de dados e aprendizado de máquina. Ele contém informações sobre três espécies de flores íris: Setosa, Versicolour e Virginica. Para cada espécie, o dataset inclui medições de quatro características:

- 1- Comprimento da sépala (sepal_length)
- 2- Largura da sépala (sepal_width)
- 3- Comprimento da pétala (petal_length)
- 4- Largura da pétala (petal_width)
- 5- Espécie (species)

- Aqui está um exemplo das primeiras linhas do dataset Iris:

| sepal_length | sepal_width | petal_length | petal_width | species |
| ------------ | ----------- | ------------ | ----------- | ------- |
| 5.1          | 3.5	     | 1.4	        | 0.2	      | setosa  |
| 4.9	       | 3.0	     | 1.4	        | 0.2	      | setosa  |
| 4.7	       | 3.2	     | 1.3	        | 0.2	      | setosa  |
| 4.6	       | 3.1	     | 1.5	        | 0.2	      | setosa  |
| 5.0          | 3.6	     | 1.4	        | 0.2	      | setosa  |

### Utilizando um Dataset Diferente:

- Se você possui um dataset específico ou deseja utilizar um dataset sobre outro tema, você pode fazer o upload do arquivo CSV correspondente e substituir a linha de código onde o dataset Iris é carregado.

### Ajustes Finais

-  Dependendo da natureza do seu dataset, você precisará ajustar as visualizações para que sejam apropriadas. Por exemplo:

- Se o seu dataset tiver datas, use essas datas para visualizações temporais.
- Se o seu dataset tiver dados geográficos (latitudes e longitudes), use esses dados para visualizações geográficas.
- Se tiver dados hierárquicos, ajuste as visualizações hierárquicas para refletir essa estrutura.
