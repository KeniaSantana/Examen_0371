nombre = ft.TextField(label="Nombre")

    tipo_evento = ft.Dropdown(
        label="Tipo de Evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunion")
        ],
        value="Conferencia"
    )

    modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial"
    )

    inscripcion = ft.Checkbox(label="¿Requiere inscripción previa?")

    cantidad_horas = ft.Slider(
        min=1,
        max=10,
        divisions=9, 
        value=1,
        label="{value}"
    )


    fecha_texto = ft.Text("No se ha seleccionado fecha")

    def seleccionar_fecha(e):
        fecha = date_picker.value
        if fecha:
            fecha_texto.value = f"Fecha seleccionada: {fecha.strftime('%d/%m/%Y')}"
            page.update()

    date_picker = ft.DatePicker(on_change=seleccionar_fecha)
    page.overlay.append(date_picker)

    boton_fecha = ft.ElevatedButton(
        "Seleccionar fecha",
        on_click=lambda e: page.open(date_picker)
    )

    lista_eventos = ft.ListView(
        expand=True,
        spacing=10,
        height=200
    )

    resumen = ft.Text(
        size=15,
        color=ft.Colors.PINK,
    )

    def mostrar_resumen(e):


        if not nombre.value:
            resumen.value = "Error: El nombre no puede estar vacío."
            resumen.color = ft.Colors.RED
            page.update()
            return

        texto = f"""
Nombre: {nombre.value}
Evento: {tipo_evento.value}
Modalidad: {modalidad.value}
Inscripcion: {"Sí" if inscripcion.value else "No"}
Cantidad De Horas: {int(cantidad_horas.value)}
{fecha_texto.value}
"""

        resumen.value = texto
        resumen.color = ft.Colors.PINK

        lista_eventos.controls.append(
            ft.Text(texto)
        )