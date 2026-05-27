import matplotlib.pyplot as plt

# Variables principales
ventas_totales = 0

cantidad_cafe = 0
cantidad_medialuna = 0
cantidad_torta = 0
cantidad_jugo = 0

ventas_enero = 0
ventas_febrero = 0
ventas_marzo = 0

# Abrimos el archivo de ventas
archivo = open("datos/ventas.csv", "r", encoding="utf-8")

# Saltamos la primera línea porque es el encabezado
archivo.readline()

# Recorremos cada venta del archivo
for linea in archivo:
    datos = linea.strip().split(",")

    fecha = datos[0]
    producto = datos[1]
    cantidad = int(datos[2])
    precio_unitario = int(datos[3])

    total_venta = cantidad * precio_unitario
    ventas_totales = ventas_totales + total_venta

    # Sumar cantidades por producto
    if producto == "Cafe":
        cantidad_cafe = cantidad_cafe + cantidad
    elif producto == "Medialuna":
        cantidad_medialuna = cantidad_medialuna + cantidad
    elif producto == "Torta":
        cantidad_torta = cantidad_torta + cantidad
    elif producto == "Jugo":
        cantidad_jugo = cantidad_jugo + cantidad

    # Sumar ventas por mes
    if fecha[5:7] == "01":
        ventas_enero = ventas_enero + total_venta
    elif fecha[5:7] == "02":
        ventas_febrero = ventas_febrero + total_venta
    elif fecha[5:7] == "03":
        ventas_marzo = ventas_marzo + total_venta

archivo.close()

# Buscar producto más vendido
producto_mas_vendido = "Cafe"
mayor_cantidad = cantidad_cafe

if cantidad_medialuna > mayor_cantidad:
    producto_mas_vendido = "Medialuna"
    mayor_cantidad = cantidad_medialuna

if cantidad_torta > mayor_cantidad:
    producto_mas_vendido = "Torta"
    mayor_cantidad = cantidad_torta

if cantidad_jugo > mayor_cantidad:
    producto_mas_vendido = "Jugo"
    mayor_cantidad = cantidad_jugo

# Guardar resumen
resumen = open("resultados/resumen_ventas.txt", "w", encoding="utf-8")

resumen.write("Resumen del análisis de ventas\n")
resumen.write("Ventas totales: " + str(ventas_totales) + "\n")
resumen.write("Producto más vendido: " + producto_mas_vendido + "\n")
resumen.write("Cantidad vendida del producto más vendido: " + str(mayor_cantidad) + "\n")
resumen.write("\nVentas por mes:\n")
resumen.write("Enero: " + str(ventas_enero) + "\n")
resumen.write("Febrero: " + str(ventas_febrero) + "\n")
resumen.write("Marzo: " + str(ventas_marzo) + "\n")

resumen.close()

# Guardar tabla simple de ventas por mes
tabla = open("resultados/ventas_por_mes.csv", "w", encoding="utf-8")

tabla.write("mes,total_ventas\n")
tabla.write("Enero," + str(ventas_enero) + "\n")
tabla.write("Febrero," + str(ventas_febrero) + "\n")
tabla.write("Marzo," + str(ventas_marzo) + "\n")

tabla.close()

# Crear gráfico simple
meses = ["Enero", "Febrero", "Marzo"]
ventas = [ventas_enero, ventas_febrero, ventas_marzo]

plt.plot(meses, ventas, marker="o")
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Total vendido")
plt.grid(True)
plt.savefig("resultados/grafico_ventas_por_mes.png")
plt.close()

print("Análisis terminado.")
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)
print("Los resultados quedaron guardados en la carpeta resultados.")
