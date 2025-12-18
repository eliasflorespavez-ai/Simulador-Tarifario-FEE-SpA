import streamlit as st

# 1. Configuración de pantalla y Estilo FEE SpA
st.set_page_config(page_title="FEE SpA - Simulador", page_icon="⚡")

# CSS para Colores Corporativos FEE SpA
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    .stButton>button { 
        background-color: #1E3A8A; 
        color: white; 
        border-radius: 8px; 
        width: 100%; 
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    h1, h3 { color: #1E3A8A; }
    </style>
    """, unsafe_allow_headers=True)

st.title("⚡ FEE SpA")
st.subheader("Simulador Tarifario Profesional 2025")

# 2. Base de Datos Maestra (Jerarquizada)
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

# 3. Lógica Anti-Bloqueo (Selectores dependientes)
region_sel = st.selectbox("🌎 Seleccione Región", list(tarifas.keys()))

# Filtrado dinámico: La lista de distribuidoras cambia según la región
distribuidoras_disponibles = list(tarifas[region_sel].keys())
empresa_sel = st.selectbox("🏢 Seleccione Distribuidora", distribuidoras_disponibles)

# 4. Entradas de datos
col1, col2 = st.columns(2)
with col1:
    consumo = st.number_input("💡 Consumo (kWh)", min_value=0.0, value=250.0, step=10.0)
with col2:
    deuda = st.number_input("💸 Saldo Anterior / Otros ($)", min_value=0.0, value=0.0)

# 5. Cálculo y Resultados
if st.button("GENERAR INFORME DE COSTOS"):
    try:
        valor_kwh = tarifas[region_sel][empresa_sel]
        neto = consumo * valor_kwh
        iva = neto * 0.19
        total_mes = neto + iva
        total_final = total_mes + deuda
        
        st.markdown("---")
        st.markdown(f"### 📊 Resultado para {empresa_sel} ({region_sel})")
        
        res1, res2 = st.columns(2)
        with res1:
            st.metric("Valor kWh", f"${valor_kwh}")
            st.write(f"**Monto Neto:** ${int(neto):,}")
        with res2:
            st.write(f"**IVA (19%):** ${int(iva):,}")
            st.info(f"**Total del Mes:** ${int(total_mes):,}")
        
        st.success(f"## TOTAL FINAL A PAGAR: ${int(total_final):,}")
        
    except Exception as e:
        st.error("Error en la matriz de datos. Por favor, refresque la página.")

st.markdown("---")
st.markdown("**Desarrollado por Elías Flores Pavez**")
st.caption("Ingeniero (E) Eléctrico | FEE SpA © 2025")
