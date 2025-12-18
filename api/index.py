import streamlit as st

# 1. Configuración de pantalla
st.set_page_config(page_title="FEE SpA", page_icon="⚡")

# 2. Base de datos
tarifas = {
    "La Araucanía": {"CGE": 235.8, "Frontel": 236.2},
    "Metropolitana": {"Enel": 210.5, "CGE": 215.8},
    "Biobío": {"CGE": 230.4, "Frontel": 233.1},
    "Valparaíso": {"Chilquinta": 228.4, "CGE": 230.1}
}

# 3. Interfaz
st.title("⚡ FEE SpA")
st.subheader("Simulador Tarifario 2025")

# Selección segura
region = st.selectbox("Región", list(tarifas.keys()))
empresa = st.selectbox("Distribuidora", list(tarifas[region].keys()))

consumo = st.number_input("Consumo (kWh)", min_value=0.0, value=200.0)

if st.button("CALCULAR"):
    val = tarifas[region][empresa]
    total = consumo * val * 1.19 # Incluye IVA
    st.success(f"Total Estimado (IVA incl.): ${int(total):,}")

st.markdown("---")
st.write("Ing. Elías Flores Pavez")
