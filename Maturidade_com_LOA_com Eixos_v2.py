# Maturidade com LOA 3D
import pandas as pd
import plotly.express as px

# Mapeamento de Sigla -> Eixo (baseado em eixos_do_mapa.csv)
eixo_por_sigla = {
    'DCPA':     'Cidade e Ambiente',
    'DMAE':     'Cidade e Ambiente',
    'DMLU':     'Cidade e Ambiente',
    'EPTC':     'Cidade e Ambiente',
    'SMMU':     'Cidade e Ambiente',
    'SMOI':     'Cidade e Ambiente',
    'SMSURB':   'Cidade e Ambiente',
    'SMAMUS':   'Cidade e Ambiente',
    'DEMHAB':   'Pessoas e Sociedade',
    'GCA':      'Pessoas e Sociedade',
    'GPD':      'Pessoas e Sociedade',
    'SMIDH':    'Pessoas e Sociedade',
    'SMS':      'Pessoas e Sociedade',
    'SMAS':     'Pessoas e Sociedade',
    'SMED':     'Pessoas e Sociedade',
    'SMEL':     'Pessoas e Sociedade',
    'SMSEG':    'Pessoas e Sociedade',
    'GI':       'Economia e Inovação',
    'SMC':      'Economia e Inovação',
    'SMDETE':   'Economia e Inovação',
    'PREVIMPA': 'Gestão Inteligente',
    'PROCEMPA': 'Gestão Inteligente',
    'GCS':      'Gestão Inteligente',
    'GP/GVP':   'Gestão Inteligente',
    'PGM':      'Gestão Inteligente',
    'SMF':      'Gestão Inteligente',
    'SMAP':     'Gestão Inteligente',
    'SMGOV':    'Gestão Inteligente',
    'SMP':      'Gestão Inteligente',
    'SMPG':     'Gestão Inteligente',
    'SMTC':     'Gestão Inteligente',
    'SMGG':     'Gestão Inteligente',
}

# Ordem e cores dos grupos por eixo temático
ordem_legenda = [
    'Cidade e Ambiente',
    'Pessoas e Sociedade',
    'Economia e Inovação',
    'Gestão Inteligente',
    'Sem Associação',
]

cores = {
    'Cidade e Ambiente':   '#1f77b4',  # Azul
    'Pessoas e Sociedade': '#ff7f0e',  # Laranja
    'Economia e Inovação': '#2ca02c',  # Verde
    'Gestão Inteligente':  '#9467bd',  # Roxo
    'Sem Associação':      '#ffffff',  # Branco
}

# Ler dados
df = pd.read_csv('maturidade-com-loa-inteiros.csv')
df.columns = df.columns.str.strip()

# Classificar cada UT pelo eixo temático
def definir_grupo(ut):
    return eixo_por_sigla.get(ut, 'Sem Associação')

df['grupo'] = df['UT_EntreParenteses'].apply(definir_grupo)

# Criar gráfico
fig = px.scatter_3d(
    df,
    x='3_Orcamento_p',
    y='LOA_p',
    z='MM',
    color='grupo',
    category_orders={'grupo': ordem_legenda},
    color_discrete_map=cores,
    text='UT_EntreParenteses',
    title='Visualização 3D das Amostras'
)

# Ajustar nomes dos eixos
fig.update_layout(
    scene=dict(
        xaxis_title='Maturidade - D. Orçamento (%)',
        yaxis_title='LOA (%)',
        zaxis_title='Maturidade Média (%)'
    )
)

# Estilo dos pontos (borda preta para destacar pontos brancos)
fig.update_traces(
    marker=dict(size=6, line=dict(width=1, color='black'))
)

# Descrição (legenda explicativa)
descricao = """
<b>Legenda dos Eixos Temáticos:</b><br>
🔵 Cidade e Ambiente: DCPA, DMAE, DMLU, EPTC, SMMU, SMOI, SMSURB, SMAMUS<br>
🟠 Pessoas e Sociedade: DEMHAB, GCA, GPD, SMIDH, SMS, SMAS, SMED, SMEL, SMSEG<br>
🟢 Economia e Inovação: GI, SMC, SMDETE<br>
🟣 Gestão Inteligente: PREVIMPA, PROCEMPA, GCS, GP/GVP, PGM, SMF, SMAP, SMGOV, SMP, SMPG, SMTC, SMGG<br>
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
fig.write_html('dashboard_3d_interativo_v4.html')

fig.show()
