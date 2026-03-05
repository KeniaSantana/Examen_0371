import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Participantes"
    page.padding = 20

    titulo = ft.Text("Registro de Participantes",
                    size=30, 
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER)
    
    nombre=ft.TextField(
        label="Nombre",
        hint_text="Ingresa tu nombre"
        
    )
    correo=ft.TextField(
        label="Correo",
        hint_text="Ingresa tu correo"
        
    )

    taller = ft.Dropdown(
        label="Taller de interes",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas")
        ],
        value="Python para Principiantes"
    )
    
    modalidad_pago = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Pago completo", label="Pago completo"),
            ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
            
        ]),
        value="Pago completo"
    )
    
    casilla=ft.Checkbox(
        label="Requiere computadora portatil"
    )
    
    deslizador=ft.Slider(
        min=1,
        max=5,
        divisions=9, 
        value=1,
        label="{value}"
    )
    
    
    lista_eventos = ft.ListView(
        expand=True,
        spacing=10,
        height=200
    )

    resumen = ft.Text(
        size=15,
        color=ft.Colors.RED,
    )
    
    final = ft.Text("Gracias por tu registro",
                    size=20, 
                    weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE,
                    text_align=ft.TextAlign.CENTER)
    
    
    def mostrar_resumen(e):

        texto = f"""
Nombre: {nombre.value}
Correo:{correo.value}
Taller: {taller.value}
Modalidad de Pago: {modalidad_pago.value}
Nivel de Experiencia:{deslizador.value}
"""

        resumen.value = texto
        resumen.color = ft.Colors.RED

        lista_eventos.controls.append(
            ft.Text(texto)
        )
        
    boton = ft.ElevatedButton(
        "Registrar",
        on_click=mostrar_resumen,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
    )

    page.add(
        titulo,
        nombre,
        correo,
        modalidad_pago,
        casilla,
        deslizador,
        final,
        boton,
        ft.Divider(),
        resumen,
        ft.Text("Eventos guardados:"),
        lista_eventos
    )

ft.run(main)