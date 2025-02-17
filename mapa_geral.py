import folium
import pandas as pd

# Definição de coordenadas para os locais, definidas manualmente
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

# Criando o mapa
local_inicial = coordenadas["cantina"]
mapa = folium.Map(location=local_inicial, zoom_start=15)

# Lista de arquivos CSV
arquivos_csv = [
    "ca.csv", "cantina.csv", "fablab.csv", "labw300.csv", "motores.csv", "reitoria.csv",
    "sala_professores.csv", "salau22.csv", "secretaria.csv"
]

for arquivo in arquivos_csv:
    nome_local = arquivo.split(".")[0]  # Obtendo o nome do local
    df = pd.read_csv(arquivo)  # Lendo o CSV

    # Calculando a média geral dos decibéis
    media_decibeis = df['field1'].sum() / len(df)

    # Definição da cor do marcador com base na média de decibéis
    if media_decibeis > 80:
        cor = "red"
    elif 60 <= media_decibeis <= 80:
        cor = "orange"
    else:
        cor = "green"

    # Criando um marcador simples como bolinha
    folium.CircleMarker(
        location=coordenadas[nome_local],
        radius=10,
        color=cor,
        fill=True,
        fill_color=cor,
        fill_opacity=0.7
    ).add_to(mapa)

# Salvando o mapa em HTML
mapa.save("mapa_decibeis.html")
print("Mapa gerado: mapa_decibeis.html")
