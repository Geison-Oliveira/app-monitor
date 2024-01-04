import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Função para gerar dados falsos
def gerar_dados_falsos():
    np.random.seed(42)
    data = {
        'Data': pd.date_range(start='2023-01-01', periods=365),
        'CPU': np.random.uniform(50, 100, 365),
        'RAM': np.random.uniform(4, 16, 365),
        'Disco': np.random.uniform(20, 100, 365),
    }
    df = pd.DataFrame(data)
    return df

# Carregar dados do CSV ou gerar dados falsos
nome_arquivo = 'dados_desempenho.csv'
try:
    df = pd.read_csv(nome_arquivo)
except FileNotFoundError:
    st.warning(f'Arquivo {nome_arquivo} não encontrado. Gerando dados falsos...')
    df = gerar_dados_falsos()
    df.to_csv(nome_arquivo, index=False)
    st.success(f'Dados falsos gerados e salvos em {nome_arquivo}')

# Título do aplicativo
st.title('Avaliação de Desempenho do Computador')

# Sidebar para seleção de métrica
metrica_selecionada = st.sidebar.selectbox('Selecione a métrica:', ['CPU', 'RAM', 'Disco'])

# Gráfico de linha interativo
fig = px.line(df, x='Data', y=metrica_selecionada, title=f'{metrica_selecionada} ao longo do tempo')
st.plotly_chart(fig)

# Histograma
fig_hist = px.histogram(df, x=metrica_selecionada, nbins=30, title=f'Histograma de {metrica_selecionada}')
st.plotly_chart(fig_hist)