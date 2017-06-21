import sys
import comunidades
import itertools
import random
from grafo import Grafo

MAX_ITERACIONES = 100

def max_freq(grafo, label, v):
	freq = {}
	for u in grafo.adyacentes(v):
		if label[u] not in freq:
			freq[label[u]] = 0
		else:
			freq[label[u]] += 1

	max = 0
	maxlabel = 0
	for clave, valor in freq.items():
		if valor > max:
			max = valor
			maxlabel = clave
	
	return maxlabel



def label_propagation(grafo):
	label = {}
	vertices = grafo.vertices()

	for i, v in enumerate(sorted(vertices)):
		label[v] = i + 1

	#for v in sorted(label.keys()):
	#	print(v, label[v])

	
	for i in (0, MAX_ITERACIONES):

		random.shuffle(vertices)
		for v in vertices:
			label[v] = max_freq(grafo, label, v)

	for l in label:
		print(l)



#estadisticas--------------------------------------------------------

def mostrar_estadisticas(grafo):

	print("Estadisticas: ")

	vertices = grafo.cant_vertices()
	aristas = grafo.cant_aristas()

	print("Cantidad de vertices: ", vertices)
	print("Cantidad de aristas: ", aristas)

	promedio = 2 * aristas / vertices

	print("Promedio grado de entrada de cada vertice: ", promedio)
	print("Promedio grado de salida de cada vertice: ", promedio)

	densidad = (2 * aristas)/(vertices * (vertices - 1))
	print("Densidad del grafo: ", densidad)



#Programa principal

if (len(sys.argv) < 2):
	print("Programa: ruta de archivo no especificada")
	raise SystemExit

archivo = sys.argv[1]
g = Grafo(False)

print("Ingrese 'Salir' para salir.")
print("Cargando grafo... ")

with open(archivo, 'r') as arch:
	datos = itertools.islice(arch, 4, None)
	for linea in datos:
		vtcs = linea.split()

		g.agregar_vertice(int(vtcs[0]))
		g.agregar_vertice(int(vtcs[1]))
		g.agregar_arista(int(vtcs[0]), int(vtcs[1]))

	arch.close()

print("Grafo cargado en memoria.")


while(True):
	comando = input().lower()
	args = comando.split()

	if(len(args) == 1):
		if(args[0] == "salir"):
			break
		elif(args[0] == "estadisticas"):
			mostrar_estadisticas(g)
		elif(args[0] == "comunidades"):
			#comunidades(args, g)
			label_propagation(g)
		elif(args[0] == "distancias"):
			distancias(args, g)
		elif(args[0] == "centralidad"):
			centralidad(args, g)
		elif(args[0] == "camino"):
			camino(args, g)
		elif(args[0] == "recomendar"):
			recomendar(args, g)
		elif(args[0] == "similares"):
			similares(args, g)
		else:
			print("Programa: comando \""  + args[0] + "\" no reconocido.")

