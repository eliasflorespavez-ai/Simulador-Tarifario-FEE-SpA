import streamlit as st

st.set_page_config(page_title="FEE SpA - Simulador", page_icon="⚡")

# Estilo profesional para la interfaz
st.markdown("""
    <style>
    .main { background-color: #F1F5F9; }
    .stButton>button { width: 100%; background-color: #1E3A8A; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_headers=True)

st.title("⚡ FEE SpA")
st.subheader("Simulador Tarifario Profesional")
st.caption("Actualización: Diciembre 2025 ✅")

# Tu base de datos de Ingeniería Eléctrica
tarifas = {
    "La Araucanía": {"CGE": 235.8, "Codiner": 238.5, "Frontel": 236.2},
    "Metropolitana": {"Enel": 210.5, "CGE": 215.8, "Colina": 212.0},
    "Valparaíso": {"Chilquinta": 228.4, "CGE": 230.1},
    "Antofagasta": {"CGE": 238.4},
    "Maule": {"CGE": 228.1},
    "Biobío": {"CGE": 230.4, "Frontel": 233.1}
}

col1, col2 = st.columns(2)
with col1:
    region = st.selectbox("Región", list(tarifas.keys()))
with col2:
    empresa = st.selectbox("Distribuidora", list(tarifas[region].keys()))

kwh = st.number_input("Consumo mensual (kWh)", min_value=0.0, value=250.0)
deuda = st.number_input("Saldo Anterior / Deuda ($)", min_value=0.0, value=0.0)

if st.button("GENERAR INFORME"):
    valor_kwh = tarifas[region][empresa]
    neto = kwh * valor_kwh
    iva = neto * 0.19
    total_mes = neto + iva
    total_final = total_mes + deuda
    
    st.divider()
    st.markdown("### 📊 INFORME TÉCNICO")
    st.write(f"**Monto Neto:** ${int(neto):,}")
    st.write(f"**IVA (19%):** ${int(iva):,}")
    st.info(f"**Total del Mes:** ${int(total_mes):,}")
    st.success(f"**TOTAL A PAGAR: ${int(total_final):,}**")

st.divider()
st.write("**Desarrollado por Elías Flores Pavez**")
st.write("*Ingeniero (E) Eléctrico*")
