import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Nome do arquivo com os dados
arquivo_csv = "exemplo.csv"

# Carregar os dados do CSV
dados = pd.read_csv(arquivo_csv)

# Extrair a hora do dia da coluna de data e hora
dados['hora'] = pd.to_datetime(dados['created_at']).dt.hour

# Calcular a média do nível de ruído (decibéis) por hora
media_ruido = dados.groupby('hora')['field1'].mean().reindex(range(24), fill_value=np.nan)

# Criar um mapa de calor com os níveis de ruído ao longo do dia
plt.figure(figsize=(10, 3))
plt.imshow([media_ruido], aspect='auto', cmap="inferno", interpolation="nearest")

# Configuração dos eixos
plt.yticks([0], ["CA"])  # Apenas uma linha para o local "Biblioteca"
plt.xticks(range(0, 24, 3), [f"{h}h" for h in range(0, 24, 3)])  # Marcar as horas de 3 em 3
plt.xlabel("Hora do Dia")
plt.ylabel("Local")
plt.title("Nível de Ruído na Biblioteca ao Longo do Dia")

# Adicionar legenda de cores
plt.colorbar(label="Decibéis (dB)")

# Mostrar o gráfico
plt.show()
