import streamlit as st

# 1. Configuración de pantalla y Estilo FEE SpA
st.set_page_config(page_title="FEE SpA - Simulador", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    .stButton>button { background-color: #1E3A8A; color: white; border-radius: 8px; width: 100%; font-weight: bold; }
    h1, h3 { color: #1E3A8A; }
    </style>
    """, unsafe_allow_headers=True)

st.title("⚡ FEE SpA")
st.subheader("Simulador Tarifario Profesional 2025")

# 2. Base de Datos Maestra
tarifas = {
    "Arica y Parinacota": {"CGE": 242.5},
    "Tarapacá": {"CGE": 240.1},
    "Antofagasta": {"CGE": 238.4},
    "Atacama": {"CGE": 237.2},
    "Coquimbo": {"CGE": 232.5},
    "Valparaíso": {"Chilquinta": 228.4, "CGE": 230.1},
    "Metropolitana": {"Enel": 210.5, "CGE": 215.8, "Colina": 212.0},
    "O'Higgins": {"CGE": 225.4},
    "Maule": {"CGE": 228.1},
    "Ñuble": {"Copelec": 231.2, "CGE": 229.5},
    "Biobío": {"CGE": 230.4, "Frontel": 233.1},
    "La Araucanía": {"CGE": 235.8, "Frontel": 236.2, "Codiner": 238.5},
    "Los Ríos": {"Saesa": 234.1},
    "Los Lagos": {"Saesa": 235.5, "Crell": 237.8},
    "Aysén": {"Edelaysen": 245.2},
    "Magallanes": {"Edelmag": 248.9}
}

# 3. Lógica Dinámica (Aquí se evita el error)
# Usamos una "llave" única para que el sistema sepa que cambió la región
region_sel = st.selectbox("🌎 Seleccione Región", list(tarifas.keys()))

# Filtrado de distribuidoras: SOLO las que pertenecen a la región seleccionada
distribuidoras_disponibles = list(tarifas[region_sel].keys())
empresa_sel = st.selectbox("🏢 Seleccione Distribuidora", distribuidoras_disponibles)

# 4. Entradas
col1, col2 = st.columns(2)
with col1:
    consumo = st.number_input("💡 Consumo (kWh)", min_value=0.0, value=250.0)
with col2:
    deuda = st.number_input("💸 Saldo Anterior ($)", min_value=0.0, value=0.0)

# 5. Cálculo
if st.button("GENERAR INFORME"):
    try:
        valor_kwh = tarifas[region_sel][empresa_sel]
        neto = consumo * valor_kwh
        iva = neto * 0.19
        total_final = neto + iva + deuda
        
        st.markdown("---")
        st.metric("TOTAL A PAGAR", f"${int(total_final):,}")
        
        with st.expander("Ver desglose técnico"):
            st.write(f"Tarifa aplicada: ${valor_kwh} por kWh")
            st.write(f"Monto Neto: ${int(neto):,}")
            st.write(f"IVA (19%): ${int(iva):,}")
    except:
        st.error("Error de sincronización. Por favor, cambie de región nuevamente.")

st.markdown("---")
st.caption("Ing. Elías Flores Pavez - FEE SpA 2025")
