import sys
import comunidades
import itertools
import random
from grafo import Grafo
import heapq
from collections import deque
from operator import itemgetter


####################################
#CONSTANTES
######################################
MAX_CAMINOS = 335
RAND_MAX_RANGE = 15 #max long del camino
RAND_MIN_RANGE = 1
RAND_STEP = 1
############################


"""
Realiza caminos aleatorios 
Pre:Grafo fue creado y sus vertices son numeros
Post:Devuelve un diccionario con los vertices y su cantidad de apariciones
en todos los caminos que empiezan desde
el vertice que se recibe como parametro.
"""
def random_walks(g,vertice,descartar_ady):
    caminos=[]
    cant_caminos = MAX_CAMINOS
    while( cant_caminos > 0 ):
        caminos.append( random.randrange( RAND_MIN_RANGE,RAND_MAX_RANGE,RAND_STEP ) )
        cant_caminos-=1
    #print(caminos)
    cant_caminos = MAX_CAMINOS
    aparecidos={}
    for i in range(0,cant_caminos):
        u = vertice
        largo_camino=caminos[i]
        #print(largo_camino)
        for pasos in range(0, largo_camino):
            u = random.choice(g.dic[u]) #elijo vertice aleatorio
            if u not in aparecidos and u!=vertice: #no tengo en cuenta al vertice del parametro
                if descartar_ady == False: #se descartan adyacentes cuando busco recomendados
                    aparecidos[u]=0
                elif u not in g.dic[vertice]:
                    aparecidos[u]=0
            if u in aparecidos:
                aparecidos[u]+=1
    #print(aparecidos)
    tam = len(aparecidos)
    #print(tam )
    return aparecidos,tam

"""
"""
def imprimir_clave_lista_tuplas( lista_tuplas ):
    for item in lista_tuplas:
        print(str(item[0]))
        #print(item)

"""
Pre:
Post:
"""
def similares( id_usuario, cant_similares ):
    usuarios = random_walks( g, id_usuario,False )
    mas_similares= heapq.nlargest(int(cant_similares),usuarios.items(),key=itemgetter(1))
    imprimir_clave_lista_tuplas(mas_similares)

"""
Pre:
Post:
"""
def recomendar(id_usuario, cant_recomendados ):
    usuarios = random_walks( g, id_usuario,True )
    mas_recomendados = heapq.nlargest(int(cant_recomendados),usuarios.items(),key=itemgetter(1))
    imprimir_clave_lista_tuplas(mas_recomendados)


############################# 

"""
Pre:
Post:
"""

def bfs_visitar(origen,visitados,orden,padre):
    cola = deque() #creo cola vacia
    cola.append(origen)
    visitados[origen]=True
    len_cola = 1
    while len_cola > 0:#len_cola > 0:
        v = cola.popleft()
        len_cola-=1
        for w in g.dic[v]:
            if w not in visitados:
                visitados[w] = True
                orden[w] = orden[v] + 1
                if padre is not None:
                    padre[w] = v
                cola.append(w)
                len_cola+=1

"""
Pre:
Post:
"""

def distancias(id_usuario): 
    visitados={}
    orden ={}
    orden[id_usuario]=0
    bfs_visitar(id_usuario,visitados,orden,None)
    heap =[]
    dist={}
    for v in orden:
        if orden[v] not in dist:
            dist[orden[v]]=0
        dist[orden[v]]+=1
    for u in dist: 
        heapq.heappush(heap,(u,dist[u])) 
    long = len(dist)
    heapq.heappop(heap) #saco el primer elemento para que no salga el mismo
    long-=1
    while long>0:
        clave,val=heapq.heappop(heap)
        print(clave,val)
        long-=1

#############################

"""
Pre:
Post:
"""
def imprimir_camino(s, v, padre):
	pila = []
	u = v
	while u != s :
		if u not in padre:
			break
		pila.append(u)
		u = padre[u]
	if u != s:
		print("No existe un camino de"+str(s)+" a "+ str(v) )
		pila.clear()
		return
	print(s, end="")
	len_pila = len(pila)
	while len_pila > 0:
		u = pila.pop()
		print(" ->", u, end="")
		len_pila-=1
	print("\n")

"""
Pre:
Post:
"""
def camino(args, g):
	if len(args) != 3:
		print("El comando \"camino\" requiere dos nodos como argumentos.")
		return

	if not g.existe_vertice(int(args[1])):
		print("Vertice ", int(args[1]), " inexistente.")
		return
	if not g.existe_vertice(int(args[2])):
		print("Vertice ", int(args[2]), " inexistente.")
		return

	visitados = {}
	padre = {}
	orden = {}
	id1 = int(args[1])
	id2 = int(args[2])
	orden[id1] = 0
	bfs_visitar(id1,visitados,orden,padre)
	imprimir_camino(id1,id2,padre)

#comunidades----------------------------------------------------------------

MAX_ITERACIONES = 2

def max_freq(grafo, label, v):
	freq = {}
	for u in grafo.adyacentes(v).keys():
		if label[u] not in freq:
			freq[label[u]] = 0
		else:
			freq[label[u]] += 1

	max = -1
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
	
	for i in range(0, MAX_ITERACIONES):

		random.shuffle(vertices)
		for v in vertices:
			label[v] = max_freq(grafo, label, v)
	
	comunidades = {}
	for v in vertices:
		if label[v] not in comunidades:
			comunidades[label[v]] = []
		comunidades[label[v]].append(v)

	for k in sorted(comunidades.keys()):
		if (len(comunidades[k]) > 4 and len(comunidades[k]) < 2000):
			print("\nComunidad ", k)
			for v in sorted(comunidades[k]):
				print(v)
			
	

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

	if len(args) >= 1:
		if(args[0] == "salir"):
			break
		elif(args[0] == "estadisticas"):
			mostrar_estadisticas(g)
		elif(args[0] == "comunidades"):
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
			print("Programa: comando \""  + args[0] + "\" no reconocido. (Tip: ingrese \"ayuda\" para una lista de comandos.)")

