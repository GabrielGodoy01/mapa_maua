import folium
import pandas as pd
from folium.plugins import HeatMap, MarkerCluster
import matplotlib.pyplot as plt
import io
import base64

# Definição de coordenadas para os locais
coordenadas = {
    "ca": (-23.649068, -46.572754),
    "cantina": (-23.648451, -46.574281),
    "fablab": (-23.64916153193695, -46.57292651987969),
    "labw300": (-23.647865, -46.573980),
    "motores": (-23.647091, -46.573561),
    "reitoria": (-23.647213, -46.574267),
    "sala_professores": (-23.648137, -46.572739),
    "salau22": (-23.648283, -46.573975),
    "secretaria": (-23.648324466707592, -46.57265010937414),
}

# Criando o mapa centralizado na biblioteca (poderia ser outro local)
local_inicial = coordenadas["ca"]
mapa = folium.Map(location=local_inicial, zoom_start=15)

# Lista de arquivos CSV
arquivos_csv = ["ca.csv", "cantina.csv", "fablab.csv", "labw300.csv", "motores.csv", "reitoria.csv", "sala_professores.csv", "salau22.csv", "secretaria.csv"]

for arquivo in arquivos_csv:
    nome_local = arquivo.split(".")[0]  # Obtendo o nome do local
    df = pd.read_csv(arquivo)  # Lendo o CSV

    # Convertendo a coluna 'created_at' para datetime
    df['created_at'] = pd.to_datetime(df['created_at'])

    # Extraindo a hora do dia
    df['hora'] = df['created_at'].dt.hour

    # Agrupando por hora e calculando a média dos decibéis
    df_grouped = df.groupby('hora')['field1'].mean().reset_index()

    # Criando um gráfico de linha para a evolução dos decibéis ao longo do dia
    plt.figure(figsize=(10, 5))
    plt.plot(df_grouped['hora'], df_grouped['field1'], marker='o')
    plt.title(f'Evolução dos Decibéis ao Longo do Dia - {nome_local.capitalize()}')
    plt.xlabel('Hora do Dia')
    plt.ylabel('Média de Decibéis')
    plt.grid(True)

    # Salvando o gráfico em uma imagem
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.read()).decode('utf-8')
    plt.close()

    # Criando o HeatMap com peso proporcional ao número de registros
    HeatMap(
        data=[(coordenadas[nome_local][0], coordenadas[nome_local][1], df['field1'].mean())],
        radius=50
    ).add_to(mapa)

    # Adicionando um marcador fixo no local manualmente definido
    popup_content = f"""
    <h3>{nome_local.capitalize()}</h3>
    <p>Média de Decibéis: {df['field1'].mean():.2f} dB</p>
    <img src="data:image/png;base64,{img_base64}" alt="Evolução dos Decibéis" width="300">
    """
    folium.Marker(
        location=coordenadas[nome_local],
        popup=folium.Popup(popup_content, max_width=400),
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mapa)

# Salvando o mapa em HTML
mapa.save("mapa_calor_interativo.html")
print("Mapa gerado: mapa_calor_interativo.html")