import sys
import comunidades
import itertools
import random
from grafo import Grafo
import heapq
from collections import deque
from operator import itemgetter

"""
Hace una lista de caminos del largo pasado por parámetro, cuyos valores en cada índice son
una cantidad aleatoria de pasos comprendida en el rango también pasado por parámetro.

Post:se retornó lista de caminos

"""

def random_walk_lista_crear( cant_caminos,max_pasos,min_pasos ):
    caminos=[]
    len_caminos = int(cant_caminos)

    while( len_caminos > 0 ):
        caminos.append( random.randint( int(min_pasos),int(max_pasos) ) )
        len_caminos-=1

    return caminos

"""
Cuenta las apariciones de cada vertice en un camino.

Pre: instancia de Grafo creada, diccionario aparecidos creado.

Post: diccionario aparecidos actualizado.
"""

def random_walk_visitar( grafo,origen,len_camino,aparecidos,descartar_ady ):
    u = origen
    
    for pasos in range(0, len_camino):
        #elijo vertice aleatorio   
        v = random.choice( list(grafo.dic[u]) )
        #no cuento las apariciones del origen
        #o de los adyacentes al origen en el caso de que descartar_ady = True    
        if v not in aparecidos and v!=origen:
            if descartar_ady == False: 
                aparecidos[v]=0
            elif grafo.son_adyacentes( origen,v )==False:
                    aparecidos[v]=0
        if v in aparecidos:
            aparecidos[v]+=1
        u=v


"""
Realiza caminos aleatorios en un grafo para el número de vértices pasado por parámetro.

Pre: instancia de Grafo creada, lista de caminos creada 

Post: se retornó diccionario con la cantidad de apariciones de los vértices encontrados.
"""

def random_walk_global(grafo,cant_vertices,cant_caminos,lista_caminos):
    len_caminos = int(cant_caminos)
    aparecidos={}
    contador = 0
    
    for v in grafo.dic:
        for i in range(0,len_caminos):
            len_camino=lista_caminos[i]
            random_walk_visitar( grafo,v,lista_caminos[i],aparecidos,False )
        contador+=1
        if(contador == cant_vertices ):
            break
    
    return aparecidos


"""
Imprime el primer item de cada tupla en una lista

Pre: lista_tuplas fue creada.

"""
def imprimir_clave_lista_tuplas( lista_tuplas,imprimir_coma ):

    for item in lista_tuplas:
        print(str(item[0]),end="")
        if imprimir_coma == True:
            print(",",end="")
        print("\t",end="")
    print("\n")
        

MAX_CAM_SIM_REC =3543
MAX_PASOS_SIM_REC =15
MIN_PASOS_SIM_REC =1

"""
Imprime una cantidad de usuarios similares al usuario pasado por parámetro.

Pre: instancia de Grafo creada, 

"""
def similares( grafo, id_usuario, cant_similares ):
    caminos = MAX_CAM_SIM_REC
    max_pasos = MAX_PASOS_SIM_REC
    min_pasos = MIN_PASOS_SIM_REC
    lista_caminos = random_walk_lista_crear(caminos,max_pasos,min_pasos )
    aparecidos={}
    
    for i in range(0,caminos):
        random_walk_visitar(grafo,id_usuario,lista_caminos[i],aparecidos,False)
        
    mas_similares= heapq.nlargest(int(cant_similares),aparecidos.items(),key=itemgetter(1))
    imprimir_clave_lista_tuplas(mas_similares,False)


"""
Imprime una cantidad de usuarios recomendados al usuario pasado por parámetro

Pre: instancia de Grafo creada, 

"""
def recomendar(grafo,id_usuario, cant_recomendados ):
    caminos = MAX_CAM_SIM_REC
    max_pasos= MAX_PASOS_SIM_REC
    min_pasos = MIN_PASOS_SIM_REC
    lista_caminos = random_walk_lista_crear(caminos,max_pasos,min_pasos )
    aparecidos={}

    for i in range(0,caminos):
        random_walk_visitar( grafo,id_usuario,lista_caminos[i],aparecidos,True )
        
    mas_recomendados = heapq.nlargest(int(cant_recomendados),aparecidos.items(),key=itemgetter(1))
    imprimir_clave_lista_tuplas(mas_recomendados,True)


"""
Realiza recorrido BFS desde un vertice pasado por parámetro.
Calcula la distancia mínima entre el vértice de origen y los otros vértices
que se encuentran en un grafo no pesado.

Pre: instancia de Grafo creada
Post: se retornó diccionario con la distancia de cada vértice en el recorrido.
"""

def bfs_visitar(grafo,origen ):
    visitados={}
    orden ={}
    orden[origen]=0
    cola = deque() 
    cola.append(origen)
    visitados[origen]=True
    len_cola = 1

    while len_cola>0:
        v = cola.popleft()
        len_cola-=1

        for w in grafo.dic[v]:
            if w not in visitados:
                visitados[w] = True
                orden[w] = orden[v] + 1
                cola.append(w)
                len_cola+=1
    return orden


"""
Reconstruye un camino mínimo desde un vertice de origen hasta otro en un
grafo no pesado

Pre: instancia de Grafo creada

Post: se  imprimió por pantalla el camino entre los vertices si éste existe.
En caso contrario se retornó False
"""
def reconstruir_camino(grafo,origen,v,dist_min,dist_actual):

    if dist_actual>dist_min:
        return False
    
    for adyacente in grafo.dic[v]:
        if adyacente == origen:
            print(origen,end="")
            if dist_min == 1:
                print("->"+v+"\n",)
            return True
        if reconstruir_camino(grafo,origen,adyacente,dist_min,dist_actual+1) is True:
            print("->"+ adyacente,end="")
            if dist_actual == 1:
                print("->"+v+"\n",)
            return True
        
    return False


"""
Calcula el camino minimo entre dos usuarios y lo imprime en pantalla

Pre: instancia de Grafo creada,

"""

def camino( args,g ):
	if len(args) != 3:
		print("El comando \"camino\" requiere dos nodos como argumentos.")
		return
	if not g.existe_vertice(int(args[1])):
		print("Vertice ", int(args[1]), " inexistente.")
		return
	if not g.existe_vertice(int(args[2])):
		print("Vertice ", int(args[2]), " inexistente.")
		return
	orden = bfs_visitar(g,id1)
	if reconstruir_camino(g,id1,id2,orden[id2],1) is False:
        	print("No existe camino de "+id1+" a "+id2)


MAX_CAM_CENT = 10
MAX_PASOS_CENT = 130
MIN_PASOS_CENT = 50
CANT_VERTICES = 400

"""
Obtiene los usuarios mas centrales a través de sucesivos random walks.

"""
def centralidad( grafo, cant_centrales ):
	caminos = MAX_CAM_CENT
	max_pasos = MAX_PASOS_CENT
	min_pasos = MIN_PASOS_CENT
	lista_caminos = random_walk_lista_crear(caminos,max_pasos,min_pasos )
	cant = CANT_VERTICES
	aparecidos=random_walk_global( grafo, cant,caminos,lista_caminos )
	mas_centrales = heapq.nlargest(int(cant_centrales),aparecidos.items(),key=itemgetter(1))
	imprimir_clave_lista_tuplas(mas_centrales, False )
    

"""
Calcula la cantidad de usuarios que están en cada una de
las distancias posibles del usuario pasado por parámetro

Pre: instancia de grafo fue creada

Post: cantidad de usuarios y distancias impresas por pantalla
"""

def distancias(grafo,id_usuario): 
    orden = bfs_visitar(grafo,id_usuario)
    heap =[]
    dist={}

    for v in orden:
        if orden[v] not in dist:
            dist[orden[v]]=0
        dist[orden[v]]+=1

    for u in dist: 
        heapq.heappush(heap,(u,dist[u]))
        
    long = len(dist)
    heapq.heappop(heap) 
    long-=1

    while long>0:
        clave,val=heapq.heappop(heap)
        print(clave,val)
        long-=1 
	
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

