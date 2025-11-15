# ui_mockup.py (corregido)
import flet as ft

def sidebar():
    return ft.Column(
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.CircleAvatar(radius=28, content=ft.Text("F", size=20)),
                        ft.Text("Usuario Demo", weight="bold"),
                        ft.Text("Empresa X", size=12, color=ft.Colors.GREY),
                    ],
                    tight=True,
                ),
                padding=ft.padding.all(12),
            ),
            ft.Divider(),
            ft.ListView(
                [
                    ft.ElevatedButton("Carga de datos", on_click=lambda e: None),
                    ft.ElevatedButton("Simulaciones", on_click=lambda e: None),
                    ft.ElevatedButton("Variables externas", on_click=lambda e: None),
                    ft.ElevatedButton("Compras / Reposición", on_click=lambda e: None),
                    ft.ElevatedButton("Dashboard", on_click=lambda e: None),
                    ft.ElevatedButton("IA & Recomendaciones", on_click=lambda e: None),
                ],
                spacing=6,
                padding=ft.padding.only(top=6, left=6, right=6),
            ),
            ft.VerticalDivider(),
            # ft.Spacer() fue reemplazado por Container(expand=True) por compatibilidad
            ft.Container(expand=True),
            ft.Text("v0.1 • Demo", size=11, color=ft.Colors.GREY),
        ],
        spacing=12,
        tight=True,
        width=260,
        scroll=True,
    )

def data_upload_tab():
    sample_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Mes")),
            ft.DataColumn(ft.Text("Ventas")),
            ft.DataColumn(ft.Text("Precio")),
        ],
        rows=[
            ft.DataRow([ft.DataCell(ft.Text("Ene")), ft.DataCell(ft.Text("120")), ft.DataCell(ft.Text("10"))]),
            ft.DataRow([ft.DataCell(ft.Text("Feb")), ft.DataCell(ft.Text("150")), ft.DataCell(ft.Text("10"))]),
            ft.DataRow([ft.DataCell(ft.Text("Mar")), ft.DataCell(ft.Text("80")), ft.DataCell(ft.Text("10"))]),
        ],
        width=800,
    )

    return ft.Column(
        [
            ft.Card(
                ft.Container(
                    ft.Column(
                        [
                            ft.Text("Carga de archivo CSV / Excel", size=16, weight="bold"),
                            ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text("Arrastra aquí o haz click para seleccionar archivo", size=12),
                                                ft.ElevatedButton("Seleccionar archivo"),
                                                ft.Row([ft.ElevatedButton("Validar estructura"), ft.ElevatedButton("Limpiar")]),
                                            ],
                                            tight=True,
                                        ),
                                        padding=ft.padding.all(18),
                                        bgcolor=ft.Colors.LIGHT_BLUE_50,
                                        border_radius=6,
                                        expand=True,
                                    ),
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text("Preview de columnas", weight="bold"),
                                                ft.Text("Columna1, Columna2, Fecha, Cantidad..."),
                                                ft.Divider(),
                                                ft.Text("Errores: Ninguno detectado", color=ft.Colors.GREEN),
                                            ],
                                            tight=True,
                                        ),
                                        padding=ft.padding.all(12),
                                        width=280,
                                    ),
                                ],
                                spacing=16,
                            ),
                        ]
                    )
                ),
                elevation=1,
            ),
            ft.Text("Tabla de datos (vista previa)", weight="bold"),
            ft.Container(content=sample_table, padding=ft.padding.all(6)),
        ],
        spacing=12,
    )

def simulations_tab():
    return ft.Column(
        [
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Simulaciones", size=16, weight="bold"),
                            ft.Text("¿Cuántos escenarios deseas simular? (ej: 3)"),
                            ft.Row(
                                [
                                    ft.TextField(value="3", width=80),
                                    ft.ElevatedButton("Agregar escenario"),
                                    ft.ElevatedButton("Generar gráficos"),
                                ],
                                spacing=8,
                            ),
                            ft.Divider(),
                            ft.Text("Escenarios actuales"),
                            ft.ListView(
                                [
                                    ft.Row([ft.Text("Escenario A"), ft.Text("2.5%")]),
                                    ft.Row([ft.Text("Escenario B"), ft.Text("7.5%")]),
                                    ft.Row([ft.Text("Escenario C"), ft.Text("15%")]),
                                ],
                                height=120,
                            ),
                        ],
                        expand=True,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Gráficos comparativos", weight="bold"),
                                ft.Container(ft.Text("Grafico placeholder (línea por escenario)"), height=240, alignment=ft.alignment.center),
                                ft.Divider(),
                                ft.Text("Resumen rápido"),
                                ft.Text("Ventas totales por escenario: ..."),
                            ]
                        ),
                        width=420,
                    ),
                ],
                spacing=18,
            )
        ],
        spacing=12,
    )

def variables_tab():
    return ft.Column(
        [
            ft.Text("Variables externas", size=16, weight="bold"),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Lista de variables"),
                            ft.ListView(
                                [
                                    ft.Row([ft.Text("Clima"), ft.Text("+/- % por mes")]),
                                    ft.Row([ft.Text("Campañas"), ft.Text("Efecto puntual")]),
                                    ft.Row([ft.Text("Ferias"), ft.Text("Efecto mes X")]),
                                ],
                                height=180,
                            ),
                            ft.ElevatedButton("Añadir variable"),
                        ]
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Curva de estacionalidad", weight="bold"),
                                ft.Container(ft.Text("Curva placeholder"), height=260, alignment=ft.alignment.center),
                            ]
                        ),
                        width=420,
                    ),
                ],
                spacing=18,
            ),
        ],
        spacing=12,
    )

def purchases_tab():
    return ft.Column(
        [
            ft.Text("Módulo de cálculo de compras", size=16, weight="bold"),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.TextField(label="Tiempo de entrega (días)", value="60", width=220),
                            ft.TextField(label="Cantidad mínima de compra", value="100", width=220),
                            ft.TextField(label="Stock mínimo (meses)", value="2", width=220),
                            ft.TextField(label="Stock inicial", value="250", width=220),
                            ft.ElevatedButton("Calcular", width=160),
                        ],
                        spacing=8,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Resultado (preview)"),
                                ft.DataTable(
                                    columns=[ft.DataColumn(ft.Text("Mes")), ft.DataColumn(ft.Text("Comprar")), ft.DataColumn(ft.Text("Stock Final"))],
                                    rows=[
                                        ft.DataRow([ft.DataCell(ft.Text("Ene")), ft.DataCell(ft.Text("0")), ft.DataCell(ft.Text("200"))]),
                                        ft.DataRow([ft.DataCell(ft.Text("Feb")), ft.DataCell(ft.Text("100")), ft.DataCell(ft.Text("150"))]),
                                    ],
                                ),
                            ]
                        ),
                        width=520,
                    ),
                ],
                spacing=18,
            ),
        ],
        spacing=12,
    )

def dashboard_tab():
    kpi_cards = ft.Row(
        [
            ft.Card(ft.Container(ft.Column([ft.Text("Ventas proyectadas"), ft.Text("$12,345")]), padding=12), width=220),
            ft.Card(ft.Container(ft.Column([ft.Text("Costo proyectado"), ft.Text("$3,210")]), padding=12), width=220),
            ft.Card(ft.Container(ft.Column([ft.Text("Rotación stock"), ft.Text("1.8x")]), padding=12), width=220),
        ],
        spacing=12,
    )
    return ft.Column(
        [
            ft.Text("Dashboard", size=18, weight="bold"),
            kpi_cards,
            ft.Row(
                [
                    ft.Container(ft.Text("Grafico por escenario (placeholder)"), height=260, expand=True),
                    ft.Container(ft.Text("Curva estacionalidad (placeholder)"), height=260, width=420),
                ],
                spacing=12,
            ),
            ft.Divider(),
            ft.Text("Tabla de ventas proyectadas"),
            ft.Container(ft.Text("Tabla placeholder"), height=160),
            ft.Divider(),
            ft.Text("Recomendaciones automáticas"),
            ft.Container(ft.Text("- Comprar más en marzo\n- Revisar proveedor A"), padding=12),
        ],
        spacing=12,
    )

def ia_tab():
    return ft.Column(
        [
            ft.Text("IA & Recomendaciones", size=16, weight="bold"),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Switch(label="Activar sugerencias automáticas", value=True),
                            ft.ElevatedButton("Analizar histórico"),
                        ],
                        spacing=8,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Predicción de crecimiento"),
                                ft.Text("+7.4% (estimado)"),
                                ft.Divider(),
                                ft.Text("Outliers detectados"),
                                ft.Text("- 2024-05: pico anómalo"),
                            ]
                        ),
                        width=420,
                    ),
                ],
                spacing=18,
            )
        ],
        spacing=12,
    )

def main(page: ft.Page):
    page.title = "SalesLab - Mockup demo"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 12
    page.window_width = 1200
    page.window_height = 800

    tabs_content = {
        "Carga de datos": data_upload_tab(),
        "Simulaciones": simulations_tab(),
        "Variables": variables_tab(),
        "Compras": purchases_tab(),
        "Dashboard": dashboard_tab(),
        "IA": ia_tab(),
    }

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[ft.Tab(text=k) for k in tabs_content.keys()],
        on_change=lambda e: page.update(),
    )

    content_area = ft.Column([tabs, ft.Divider(), tabs_content["Carga de datos"]], expand=True)

    # Handle tab switching crudely: we replace content on tab click
    def switch_tab(e):
        selected = tabs.tabs[e.control.selected_index].text
        content_area.controls[2] = tabs_content[selected]
        page.update()

    tabs.on_change = switch_tab

    page.add(
        ft.Row(
            [
                sidebar(),
                ft.VerticalDivider(width=12),
                ft.Container(content_area, expand=True, padding=12),
            ],
            spacing=12,
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
