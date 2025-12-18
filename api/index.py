import streamlit as st

# 1. IDENTIDAD CORPORATIVA FEE SpA
st.set_page_config(page_title="FEE SpA - Simulador", page_icon="⚡", layout="centered")

# CSS para inyectar colores de marca (Azul #1E3A8A)
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    .stButton>button { 
        background-color: #1E3A8A; 
        color: white; 
        border-radius: 8px;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { background-color: #2563EB; border: none; color: white; }
    h1, h2, h3 { color: #1E3A8A; font-family: 'Segoe UI', sans-serif; }
    .stSelectbox, .stNumberInput { border-radius: 10px; }
    </style>
    """, unsafe_allow_headers=True)

st.title("⚡ FEE SpA")
st.subheader("Simulador Tarifario Profesional 2025")
st.markdown("---")

# 2. BASE DE DATOS TÉCNICA (Todas las regiones)
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
    "Ñuble": {"CGE": 229.5, "Copelec": 231.2},
    "Biobío": {"CGE": 230.4, "Frontel": 233.1},
    "La Araucanía": {"CGE": 235.8, "Codiner": 238.5, "Frontel": 236.2},
    "Los Ríos": {"Saesa": 234.1},
    "Los Lagos": {"Saesa": 235.5, "Crell": 237.8},
    "Aysén": {"Edelaysen": 245.2},
    "Magallanes": {"Edelmag": 248.9}
}

# 3. INTERFAZ DE CÁLCULO
col1, col2 = st.columns(2)
with col1:
    region = st.selectbox("🌎 Región", list(tarifas.keys()))
with col2:
    empresa = st.selectbox("🏢 Distribuidora", list(tarifas[region].keys()))

c1, c2 = st.columns(2)
with c1:
    consumo = st.number_input("💡 Consumo (kWh)", min_value=0.0, value=250.0, step=10.0)
with c2:
    deuda = st.number_input("💸 Saldo Anterior ($)", min_value=0.0, value=0.0)

st.write("") # Espaciador

if st.button("GENERAR INFORME DE COSTOS"):
    val_kwh = tarifas[region][empresa]
    neto = consumo * val_kwh
    iva = neto * 0.19
    total_mes = neto + iva
    total_final = total_mes + deuda
    
    st.markdown("### 📊 Resultado del Análisis")
    res1, res2 = st.columns(2)
    with res1:
        st.metric("Valor kWh", f"${val_kwh}")
        st.write(f"**Monto Neto:** ${int(neto):,}")
    with res2:
        st.write(f"**IVA (19%):** ${int(iva):,}")
        st.info(f"**Total Mes:** ${int(total_mes):,}")
    
    st.success(f"## TOTAL A PAGAR: ${int(total_final):,}")
    st.caption("Cálculo basado en tarifas proyectadas para Diciembre 2025.")

st.markdown("---")
# 4. FIRMA PROFESIONAL
st.markdown("""
    **Desarrollado por Elías Flores Pavez** *Ingeniero (E) Eléctrico | Especialista en Proyectos y Tarifas* **FEE SpA © 2025**
""")
