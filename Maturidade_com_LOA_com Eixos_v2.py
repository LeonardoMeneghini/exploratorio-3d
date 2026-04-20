# Rotina para Representação tridimensional  de 3 indicadores

# Importando as bilbiotecas/pacotes
import pandas as pd
import plotly.express as px

# Mapeamento  as siglas das UTs -> Eixo: necessário arquivo .CSV com secretaria/órgão e seu respecitvo eixo estratégico
eixo_por_sigla = {
    'Sigla da Secretaria 1':  'Nome do Eixo Estratégico 1',
    'Sigla da Secretaria  2': 'Nome do Eixo Estratégico 3',
    'Sigla da Secretaria 3':  'Nome do Eixo Estratégico 2',
    'Sigla da Secretaria 4':  'Nome do Eixo Estratégico 2',
}

# Ordem e cores dos grupos por eixo temático
ordem_legenda = [
    'Nome do Eixo Estratégico 1',
    'Nome do Eixo Estratégico 2',
    'Nome do Eixo Estratégico 3',
    'Nome do Eixo Estratégico 4',
    'Sem Associação',
]

cores = {
    'Nome do Eixo Estratégico 1':   '#1f77b4',  # Azul
    'Nome do Eixo Estratégico 2': '#ff7f0e',  # Laranja
    'Nome do Eixo Estratégico 3': '#2ca02c',  # Verde
    'Nome do Eixo Estratégico 4':  '#9467bd',  # Roxo
    'Sem Associação':      '#ffffff',  # Branco
}

# Ler dados de plotagem
df = pd.read_csv('nome do arquivo exportado do BI com dados maturidade.csv')
df.columns = df.columns.str.strip()

# Classificar cada UT pelo eixo temático
def definir_grupo(ut):
    return eixo_por_sigla.get(ut, 'Sem Associação')

df['grupo'] = df['Coluna do CSV com nome da Secretaria'].apply(definir_grupo)

# Criar gráfico
fig = px.scatter_3d(
    df,
    x='Coluna com a Resposta 1',
    y='Coluna com a Resposta 2',
    z='Coluna com a Resposta 3',
    color='grupo',
    category_orders={'grupo': ordem_legenda},
    color_discrete_map=cores,
    text='UT_EntreParenteses',
    title='Visualização 3D das Amostras'
)

# Ajustar nomes dos eixos
fig.update_layout(
    scene=dict(
        xaxis_title='Título da Resposta 1 no eixo X',
        yaxis_title='Título da Resposta 2 no eixo Y',
        zaxis_title='Título da Resposta 3 no eixo Z'
    )
)

# Estilo dos pontos (borda preta para destacar pontos brancos)
fig.update_traces(
    marker=dict(size=6, line=dict(width=1, color='black'))
)

# Descrição (legenda explicativa)
descricao = """
<b>Legenda dos Eixos Temáticos:</b><br>
🔵 Nome do Eixo Estratégico 1: Secretaria 1, Secreatira 2<br>
🟠 Nome do Eixo Estratégico 2: Secreatira 3, Secreatira 4<br>
🟢 Nome do Eixo Estratégico 3: Secreatira 5, Secreatira 6<br>
🟣 Nome do Eixo Estratégico 4: Secreatira 7, Secreatira 8<br>
⚪ Sem Associação
"""

# Layout final
fig.update_layout(
    legend_title_text='Eixos Temáticos',
    margin=dict(l=0, r=0, t=50, b=120),
    annotations=[
        dict(
            text=descricao,
            showarrow=False,
            x=0,
            y=-0.25,
            xref='paper',
            yref='paper',
            align='left'
        )
    ]
)

# Salvar
fig.write_html('nome do arquivo do gráfico.html')

fig.show()
