# Libs necessarias
import pandas as pd
import numpy as np

# Lib Gráficas
import matplotlib as plt
import seaborn as sns

# Confg Pandas
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 100)

# Config Matplotlib
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('seaborn-darkgrid')

# Ler os dados
base_dados = pd.read_csv('house_data.csv')
base_dados.shape
base_dados.head()
