import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração inicial do Streamlit
st.set_page_config(page_title="Dashboard Imobiliário", layout="wide")

# Carregar os dados
@st.cache_data
def carregar_dados():
    caminho_arquivo = "ml_sale_houses_cleaned.csv"
    data = pd.read_csv(caminho_arquivo)
    return data

df = carregar_dados()

# Título do dashboard
st.title("📊 Dashboard de Análise Imobiliária")
st.markdown("### Comparação de Preço por Metro Quadrado e Área Média por UF")

# Seleção de UF para análise detalhada
ufs_disponiveis = df["UF"].unique()
uf_selecionada = st.selectbox("Selecione uma UF para análise detalhada:", ufs_disponiveis)

# Filtrar dados por UF
df_filtrado = df[df["UF"] == uf_selecionada]

# Estatísticas gerais da UF selecionada
st.markdown(f"### 📌 Estatísticas Gerais - {uf_selecionada}")
col1, col2, col3 = st.columns(3)
col1.metric("Preço Médio por m²", f"R$ {df_filtrado['Preço'].mean():,.2f}")
col2.metric("Área Média", f"{df_filtrado['Área (m²)'].mean():,.2f} m²")
col3.metric("Quantidade de Imóveis", df_filtrado.shape[0])

# Criar gráfico de distribuição de preços por m²
st.markdown("### 📊 Distribuição de Preço por Metro Quadrado")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df_filtrado["Preço"], bins=30, kde=True, color="blue")
plt.xlabel("Preço por m² (R$)")
plt.ylabel("Frequência")
plt.title(f"Distribuição de Preço por m² - {uf_selecionada}")
st.pyplot(fig)

# Criar gráfico de dispersão entre preço e área
st.markdown("### 📈 Relação entre Área e Preço Total")
fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(x=df_filtrado["Área (m²)"], y=df_filtrado["Preço"], alpha=0.5)
plt.xlabel("Área (m²)")
plt.ylabel("Preço por m² (R$)")
plt.title(f"Área vs. Preço - {uf_selecionada}")
st.pyplot(fig)

# Exibir tabela com os dados filtrados
st.markdown("### 📋 Tabela de Dados")
st.dataframe(df_filtrado[["UF", "Preço", "Área (m²)", "Quartos", "Banheiros"]].sort_values(by="Preço", ascending=False))