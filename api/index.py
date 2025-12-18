import streamlit as st
import os
import sys

# 1. Configuración de página (Debe ser lo primero)
st.set_page_config(page_title="FEE SpA - Simulador", page_icon="⚡")

def main():
    st.title("⚡ FEE SpA")
    st.subheader("Simulador Tarifario Profesional")
    
    # Tu base de datos de tarifas (Simplificada para la prueba)
    tarifas = {"La Araucanía": 235.8, "Metropolitana": 210.5}
    
    region = st.selectbox("Seleccione Región", list(tarifas.keys()))
    kwh = st.number_input("Consumo (kWh)", min_value=0.0, value=100.0)
    
    if st.button("CALCULAR"):
        total = kwh * tarifas[region]
        st.success(f"Total Neto: ${int(total):,}")
    
    st.divider()
    st.write("Ing. Elías Flores Pavez - FEE SpA")

# 2. EL BYPASS: Esto es lo que evita el error FUNCTION_INVOCATION_FAILED
if __name__ == "__main__":
    main()
