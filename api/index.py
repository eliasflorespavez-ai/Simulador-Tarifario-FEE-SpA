import streamlit as st

# 1. Configuración de pantalla
st.set_page_config(page_title="FEE SpA - Simulador", page_icon="⚡")

# Estilo profesional
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    h1, h3 { color: #1E3A8A; }
    </style>
    """, unsafe_allow_headers=True)

st.title("⚡ FEE SpA")
st.subheader("Simulador Tarifario Profesional 2025")

# 2. Base de Datos Maestra
tarifas = {
    "Metropolitana": {"Enel": 210.5, "CGE": 215.8},
    "La Araucanía": {"CGE": 235.8, "Frontel": 236.2, "Codiner": 238.5},
    "Valparaíso": {"Chilquinta": 228.4, "CGE": 230.1},
    "Biobío": {"CGE": 230.4, "Frontel": 233.1},
    "Maule": {"CGE": 228.1},
    "O'Higgins": {"CGE": 225.4},
    "Antofagasta": {"CGE": 238.4}
}

# 3. Lógica de Selección (Evita el KeyError)
region_sel = st.selectbox("Seleccione Región", list(tarifas.keys()))

# Este paso es el que evita que el programa se caiga
opciones_distribuidora = list(tarifas[region_sel].keys())
empresa_sel = st.selectbox("Seleccione Distribuidora", opciones_distribuidora)

consumo = st.number_input("Consumo mensual (kWh)", min_value=0.0, value=250.0)

if st.button("CALCULAR TOTAL"):
    try:
        precio_kwh = tarifas[region_sel][empresa_sel]
        neto = consumo * precio_kwh
        total = neto * 1.19
        
        st.markdown("---")
        st.metric("Total a Pagar (IVA incl.)", f"${int(total):,}")
        st.info(f"Cálculo basado en tarifa de ${precio_kwh} por kWh")
    except Exception as e:
        st.error("Error en el cálculo. Por favor, refresque la página.")

st.markdown("---")
st.caption("Ing. Elías Flores Pavez - FEE SpA 2025")
