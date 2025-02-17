import pandas as pd
import matplotlib.pyplot as plt

# Nome do arquivo com os dados
arquivo_csv = "ca.csv"

# Carregar os dados do CSV
dados = pd.read_csv(arquivo_csv)

# Converter a coluna de data e hora para datetime
dados['created_at'] = pd.to_datetime(dados['created_at'])

# Criar uma nova coluna para minutos (desde o início da medição)
tempo_inicial = dados['created_at'].min()
dados['minuto'] = (dados['created_at'] - tempo_inicial).dt.total_seconds() / 60  # Converter para minutos

# Calcular a média do nível de ruído por minuto
media_ruido = dados.groupby('minuto')['field1'].mean()

# Criar o gráfico de linha
plt.figure(figsize=(10, 5))
plt.plot(media_ruido.index, media_ruido.values, marker='o', linestyle='-')

# Adicionar rótulos e título
plt.xlabel("Tempo de Medição (minutos)")
plt.ylabel("Nível de Ruído (dB)")
plt.title("Nível de Ruído ao Longo da Medição")

# Adicionar linha de referência para 80 dB (se necessário)
plt.axhline(y=80, color='r', linestyle='--', label="Alto Ruído (80 dB)")

# Exibir legenda
plt.legend()

# Mostrar o gráfico
plt.grid(True)
plt.show()
