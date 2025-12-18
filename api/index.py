import streamlit as st

# Configuración de página con identidad FEE SpA
st.set_page_config(page_title="FEE SpA - Simulador", page_icon="⚡", layout="centered")

# CSS para Colores Corporativos (Azul #1E3A8A y Gris #F1F5F9)
st.markdown("""
    <style>
    .stApp { background-color: #F1F5F9; }
    .stButton>button { 
        background-color: #1E3A8A; 
        color: white; 
        border-radius: 5px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    h1, h2, h3 { color: #1E3A8A; }
    </style>
    """, unsafe_allow_headers=True)

st.title("⚡ FEE SpA")
st.subheader("Simulador Tarifario Profesional 2025")
st.write("---")

# Base de datos expandida (puedes seguir agregando valores)
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

# Interfaz de usuario
col1, col2 = st.columns(2)
with col1:
    region = st.selectbox("Seleccione Región", list(tarifas.keys()))
with col2:
    empresa = st.selectbox("Distribuidora", list(tarifas[region].keys()))

consumo = st.number_input("Consumo mensual (kWh)", min_value=0.0, value=250.0, step=10.0)
deuda = st.number_input("Saldo Anterior / Otros cargos ($)", min_value=0.0, value=0.0)

if st.button("CALCULAR TOTAL"):
    valor_kwh = tarifas[region][empresa]
    neto = consumo * valor_kwh
    iva = neto * 0.19
    total_mes = neto + iva
    total_final = total_mes + deuda
    
    st.markdown("### 📊 Informe de Cálculo")
    c1, c2 = st.columns(2)
    c1.metric("Valor kWh", f"${valor_kwh}")
    c1.write(f"**Neto:** ${int(neto):,}")
    c2.write(f"**IVA (19%):** ${int(iva):,}")
    c2.info(f"**Total del Mes:** ${int(total_mes):,}")
    
    st.success(f"## TOTAL A PAGAR: ${int(total_final):,}")

st.write("---")
st.markdown("**Desarrollado por Elías Flores Pavez**")
st.caption("Ingeniero (E) Eléctrico | Proyectos de Normalización y Tarifas")
