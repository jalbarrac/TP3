import sys
from grafo import Grafo

def mostrar_estadisticas(grafo):

	print("Estadisticas: ")

	vertices = grafo.cant_vertices()
	aristas = grafo.cant_aristas()

	print("Cantidad de vertices: ", vertices)
	print("Cantidad de aristas: ", aristas)

	promedio = aristas / vertices

	print("Promedio grado de entrada de cada vertice: ", promedio)
	print("Promedio grado de salida de cada vertice: ", promedio)

	densidad = (2 * aristas)/(vertices * (vertices - 1))

	print("Densidad del grafo: ", densidad)
	

archivo = sys.argv[1]
g = Grafo(False)

print("Ingrese 'Salir' para salir.")
print("Cargando grafo... ")

with open(archivo, 'r') as datos:
	for i in (0, 4):
		next(datos)
	for linea in datos:
		vtcs = linea.split()

		g.agregar_vertice(vtcs[0])
		g.agregar_vertice(vtcs[1])
		g.agregar_arista(vtcs[0], vtcs[1])

	datos.close()

print("Grafo cargado en memoria.")

comando = input().lower()
while(comando != "salir"):
	if(comando == "estadisticas"):
		mostrar_estadisticas(g);

	comando = input()