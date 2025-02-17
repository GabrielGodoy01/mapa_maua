import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Caminho do arquivo CSV
file_path = "biblioteca.csv"

# Carregar os dados do CSV
df_biblioteca = pd.read_csv(file_path)

# Convertendo a coluna de tempo para o formato de hora
df_biblioteca['hora'] = pd.to_datetime(df_biblioteca['created_at']).dt.hour

# Agrupando por hora e calculando a média de decibéis
biblioteca_db = df_biblioteca.groupby('hora')['field1'].mean().reindex(range(24), fill_value=np.nan)

# Criando um espectrograma com os dados da biblioteca
plt.figure(figsize=(10, 3))
plt.imshow([biblioteca_db], aspect='auto', cmap="inferno", interpolation="nearest")

# Configurações do eixo
plt.yticks([0], ["Biblioteca"])
plt.xticks(range(0, 24, 3), [f"{h}h" for h in range(0, 24, 3)])
plt.xlabel("Hora do Dia")
plt.ylabel("Local")
plt.title("Mapa de Calor de Nível de Ruído na Biblioteca (dB)")

# Adicionando barra de cor
plt.colorbar(label="Decibéis (dB)")

# Exibir o gráfico
plt.show()
