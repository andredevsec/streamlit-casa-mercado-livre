import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Dashboard de Análise de Imóveis")

@st.cache_data
def load_data():
    data = pd.read_csv("ml_sale_houses_cleaned.csv")
    data['Preço/m²'] = data['Preço'] / data['Área (m²)']
    bins = [0, 100000, 300000, 500000, 1000000, np.inf]
    labels = ['Muito Barato', 'Barato', 'Médio', 'Caro', 'Muito Caro']
    data['Faixa de Preço'] = pd.cut(data['Preço'], bins=bins, labels=labels)
    return data

data = load_data()

def create_sidebar():
    with st.sidebar:
        st.header("Filtros")
        uf_filter = st.multiselect("Selecione a UF", options=data["UF"].unique(), default=list(data["UF"].unique()))
        destaque_filter = st.radio("Filtrar por Destaque", options=["Todos", "Sim", "Não"])
        preco_range = st.slider("Faixa de Preço", int(data["Preço"].min()), int(data["Preço"].max()), 
                                (int(data["Preço"].min()), int(data["Preço"].max())))
    return uf_filter, destaque_filter, preco_range

def filter_data(data, uf_filter, destaque_filter, preco_range):
    filtered_data = data[(data["UF"].isin(uf_filter)) & (data["Preço"].between(preco_range[0], preco_range[1]))]
    if destaque_filter != "Todos":
        filtered_data = filtered_data[filtered_data["Destaque"] == destaque_filter]
    return filtered_data

def plot_scatter_price_vs_area(filtered_data):
    st.subheader("Relação Preço x Área")
    fig = px.scatter(filtered_data, x='Área (m²)', y='Preço', color='Destaque', title="Preço vs Área")
    st.plotly_chart(fig)

def plot_price_per_area(filtered_data):
    st.subheader("Preço por m²")
    fig = px.scatter(filtered_data, x='Área (m²)', y='Preço/m²', color='Destaque', title="Preço por m² vs Área")
    st.plotly_chart(fig)

def plot_price_comparison_by_uf(filtered_data):
    st.subheader("Comparação entre UF")
    uf_comparativo = filtered_data.groupby('UF').agg({'Preço/m²': 'mean'}).reset_index()
    fig = px.line(uf_comparativo, x='UF', y='Preço/m²', title="Variação do Preço Médio por UF", markers=True)
    fig.update_layout(xaxis=dict(tickangle=-90))
    st.plotly_chart(fig)

def plot_price_distribution(filtered_data):
    st.subheader("Distribuição do Preço")
    price_data = filtered_data['Preço'].value_counts().sort_index()
    st.bar_chart(price_data)

def plot_rooms_distribution(filtered_data):
    st.subheader("Distribuição do Número de Quartos")
    rooms_data = filtered_data['Quartos'].value_counts().sort_index()
    st.bar_chart(rooms_data)

def plot_bathrooms_distribution(filtered_data):
    st.subheader("Distribuição do Número de Banheiros")
    bathrooms_data = filtered_data['Banheiros'].value_counts().sort_index()
    st.bar_chart(bathrooms_data)

def plot_area_distribution(filtered_data):
    st.subheader("Distribuição da Área (m²)")
    area_data = filtered_data['Área (m²)'].value_counts().sort_index()
    st.bar_chart(area_data)

uf_filter, destaque_filter, preco_range = create_sidebar()
filtered_data = filter_data(data, uf_filter, destaque_filter, preco_range)

plot_scatter_price_vs_area(filtered_data)
plot_price_per_area(filtered_data)
plot_price_comparison_by_uf(filtered_data)
plot_price_distribution(filtered_data)
plot_rooms_distribution(filtered_data)
plot_bathrooms_distribution(filtered_data)
plot_area_distribution(filtered_data)
