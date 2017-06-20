from grafo import Grafo
import random 
import heapq
from collections import deque
from operator import itemgetter

"""Funcion para cargar grafo desde un archivo.

Pre:grafo fue creado.Se asume que el archivo a recibir
cumple con el formato especificado en la consigna

Post:Se retornó True si el archivo se pudo abrir,
False en caso contrario
"""
def cargar_grafo(g):
    try:
        archivo = open("youtube.txt")
        #archivo = open(input())
    except IOError:
        print("Error de entrada/salida.")
        return False
    for i,linea in enumerate(archivo):
        #if  i==30: ##para probar cosas
           #break
        if linea[0]!="#" and i!=2:
            vertice1,vertice2 = linea.rstrip("\n").split("\t")
            g.agregar_vertice(vertice1)
            g.agregar_vertice(vertice2)
            g.agregar_arista(vertice1,vertice2)
            #print(vertice1,vertice2)
            continue
        if i==2: #en la tercer linea(para este caso 2 xq i arranca de 0 )leo la cantidad de vertices y aristas:
            cadenas = linea.rstrip("\n").split()
            g.cant_vert = int(cadenas[2])
            g.cant_ari = int(cadenas[4])
            #print(g.cant_vert,g.cant_ari)
    archivo.close()
    return True

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
    while len_cola>0:#len_cola > 0:
        v = cola.popleft()
        len_cola-=1
        for w in g.dic[v]:
            if w not in visitados:
                visitados[w] = True
                orden[w] = orden[v] + 1
                if padre is not None:
                    padre[w]=v
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
def imprimir_camino(s,v,padre):
    pila = []
    u = v
    while u!=s :
        if u not in padre:
            break
        pila.append(u)
        u = padre[u]
    if u!=s:
        print("No existe un camino de"+str(s)+" a "+ str(v) )
        pila.clear()
        return
    print(s,end="")
    len_pila = len(pila)
    while len_pila>0:
        u = pila.pop()
        print("->"+ u,end="")
        len_pila-=1

"""
Pre:
Post:
"""
def camino( id1,id2 ):
    visitados ={}
    padre={}
    orden={}
    orden[id1]=0
    bfs_visitar(id1,visitados,orden,padre)
    imprimir_camino(id1,id2,padre)
    
################################ Main ##################################

g = Grafo(False)
print("cargando grafo")
cargar_grafo(g)
print("listo")
#similares("1","5")
#recomendar("5","4")
distancias("9") 
#camino( "11","1991")

