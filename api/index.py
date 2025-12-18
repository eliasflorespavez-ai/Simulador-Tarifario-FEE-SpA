import flet as ft
import flet.fastapi as flet_fastapi

def main(page: ft.Page):
    page.title = "FEE SpA - Simulador Profesional"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F1F5F9"
    page.scroll = ft.ScrollMode.AUTO

    # --- Base de datos de tarifas netas (Diciembre 2025) ---
    tarifas_netas = {
        "La Araucanía": {"CGE": 235.8, "Codiner": 238.5, "Frontel": 236.2},
        "Metropolitana": {"Enel": 210.5, "CGE": 215.8, "Colina": 212.0},
        "Valparaíso": {"Chilquinta": 228.4, "CGE": 230.1},
        "Antofagasta": {"CGE": 238.4},
        "Maule": {"CGE": 228.1},
        "Biobío": {"CGE": 230.4, "Frontel": 233.1}
    }

    # --- Funciones de soporte ---
    def cerrar_dlg(e):
        dlg_info.open = False
        page.update()

    dlg_info = ft.AlertDialog(
        title=ft.Text("Información Técnica"),
        content=ft.Text("Monto Neto: Energía + Cargos.\nIVA: 19% del Neto.\nTotal Mes: Neto + IVA.\nTotal a Pagar: Total Mes + Deuda."),
        actions=[ft.TextButton("Entendido", on_click=cerrar_dlg)]
    )
    page.overlay.append(dlg_info)

    def resetear(e):
        input_kwh.value = ""
        input_saldo.value = "0"
        res_card.visible = False
        page.update()

    def calcular(e):
        try:
            val_neto = tarifas_netas[drp_region.value][drp_empresa.value]
            kwh = float(input_kwh.value)
            deuda = float(input_saldo.value)
            neto = kwh * val_neto
            iva = neto * 0.19
            total_mes = neto + iva
            total_final = total_mes + deuda
            res_card.content.controls.clear()
            res_card.content.controls.extend([
                ft.Text("INFORME TÉCNICO FEE SpA", weight="bold", color="#1E3A8A"),
                ft.Divider(),
                ft.Row([ft.Text("Monto Neto:"), ft.Text(f"${int(neto):,}")], alignment="spaceBetween"),
                ft.Row([ft.Text("IVA (19%):"), ft.Text(f"${int(iva):,}")], alignment="spaceBetween"),
                ft.Row([ft.Text("Total del Mes:", weight="bold"), ft.Text(f"${int(total_mes):,}", weight="bold", color="blue")], alignment="spaceBetween"),
                ft.Divider(),
                ft.Row([ft.Text("Saldo Anterior (Deuda):"), ft.Text(f"${int(deuda):,}")], alignment="spaceBetween"),
                ft.Row([
                    ft.Text("TOTAL A PAGAR:", weight="bold", size=18),
                    ft.Text(f"${int(total_final):,}", color="green", size=26, weight="bold")
                ], alignment="spaceBetween"),
                ft.ElevatedButton("NUEVA CONSULTA", icon=ft.Icons.REFRESH, on_click=resetear)
            ])
            res_card.visible = True
            page.update()
        except: pass

    def actualizar_empresas(e):
        drp_empresa.options = [ft.dropdown.Option(emp) for emp in tarifas_netas[drp_region.value].keys()]
        drp_empresa.disabled = False
        drp_empresa.value = list(tarifas_netas[drp_region.value].keys())[0]
        page.update()

    # --- Componentes de UI ---
    drp_region = ft.Dropdown(label="Región", options=[ft.dropdown.Option(r) for r in tarifas_netas.keys()], on_change=actualizar_empresas)
    drp_empresa = ft.Dropdown(label="Empresa", disabled=True)
    input_kwh = ft.TextField(label="Consumo (kWh)", prefix_icon=ft.Icons.BOLT)
    input_saldo = ft.TextField(label="Saldo Anterior ($)", value="0", prefix_icon=ft.Icons.HISTORY)
    res_card = ft.Container(content=ft.Column(), padding=20, bgcolor="white", border_radius=15, visible=False)

    page.add(
        ft.Column([
            ft.Text("FEE SpA", size=32, weight="bold", color="#1E3A8A"),
            ft.Text("Tarifas actualizadas: Diciembre 2025 ✅", size=11, color="green"),
            ft.TextButton("Información Técnica", icon=ft.Icons.INFO, on_click=lambda _: setattr(dlg_info, 'open', True) or page.update()),
            ft.Divider(),
            drp_region, drp_empresa, input_kwh, input_saldo,
            ft.ElevatedButton("SIMULAR FACTURACIÓN", on_click=calcular, style=ft.ButtonStyle(bgcolor="#1E3A8A", color="white", padding=20)),
            res_card,
            ft.Container(height=40),
            ft.Text("Desarrollado por Elías Flores Pavez", size=12, weight="bold", color="#475569"),
            ft.Text("Ingeniero (E) Eléctrico", size=10, italic=True, color="#64748B"),
        ], horizontal_alignment="center")
    )

app = flet_fastapi.app(main)
