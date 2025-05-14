import streamlit as st
import pandas as pd
import joblib

# Carregar modelo salvo
model = joblib.load("random_forest_best_model.pkl")

# Título principal
st.set_page_config(page_title="Previsão de Imóveis", page_icon="🏡")
st.title("🏠 Previsão de Preço de Imóveis")
st.markdown("Preencha os dados abaixo para obter a estimativa do **preço de venda** de um imóvel.")

st.markdown("---")

# Organizar os inputs em colunas
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("📐 Área (em pés²)", min_value=500, max_value=10000, value=1000, step=200)
    bedrooms = st.selectbox("🛏️ Quartos", [1, 2, 3, 4, 5, 6])
    bathrooms = st.selectbox("🛁 Banheiros", [1, 2, 3, 4])
    stories = st.selectbox("🏢 Andares", [1, 2, 3, 4])
    parking = st.selectbox("🚗 Vagas de estacionamento", [0, 1, 2, 3])
    mainroad = st.selectbox("🚧 Estrada principal?", ["Sim", "Não"])

with col2:
    guestroom = st.selectbox("🛋️ Quarto de hóspedes?", ["Sim", "Não"])
    basement = st.selectbox("🏚️ Porão?", ["Sim", "Não"])
    hotwaterheating = st.selectbox("🔥 Aquecimento de água?", ["Sim", "Não"])
    airconditioning = st.selectbox("❄️ Ar condicionado?", ["Sim", "Não"])
    prefarea = st.selectbox("📍 Área preferencial?", ["Sim", "Não"])
    furnishingstatus = st.selectbox("🪑 Mobiliado", ["Sem mobília", "Semi-mobiliado", "Totalmente mobiliado"])

st.markdown("---")

# Mapear variáveis categóricas
map_sim_nao = {"Sim": 1, "Não": 0}
map_furnishing = {
    "Sem mobília": 0,
    "Semi-mobiliado": 1,
    "Totalmente mobiliado": 2
}

    # Criar DataFrame com os dados de entrada
input_data = pd.DataFrame([[
    area,
    bedrooms,
    bathrooms,
    stories,
    map_sim_nao[mainroad],
    map_sim_nao[guestroom],
    map_sim_nao[basement],
    map_sim_nao[hotwaterheating],
    map_sim_nao[airconditioning],
    parking,
    map_sim_nao[prefarea],
    map_furnishing[furnishingstatus]
]], columns=[
    'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
    'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
    'parking', 'prefarea', 'furnishingstatus'
])

# Botão para fazer a previsão
if st.button("🔍 Prever Preço do Imóvel", type='secondary', use_container_width=True):

    # Fazer previsão
    predicted_price = model.predict(input_data)[0]

    # Exibir resultado
    st.success(f"💰 O preço previsto para este imóvel é: **$ {predicted_price:,.2f} milhões**")
