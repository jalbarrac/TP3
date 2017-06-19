from grafo import Grafo
import random 
import heapq

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
#CONSTANTES (otra manera de definirlos?)//calibrar mejor los valores
######################################
MAX_CAMINOS = 335
RAND_MAX_RANGE = 15 #max long del camino
RAND_MIN_RANGE = 1
RAND_STEP = 1
############################


"""
Realiza caminos aleatorios 

Pre:Grafo fue creado y sus vertices son numeros

Post:Devuelve una lista con la cantidad de apariciones
de cada vertice en todos los caminos que empiezan desde
el vertice que se recibe como parametro. Por defecto
se ignora el vertice recibido por parametro.También
se pueden ignorar sus adyacentes si se setea el tercer
parámetro en True
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
Recibe un diccionario lo ordena por valor de mayor a menor utilizando
un heap y retorna las n-tuplas mayores.
Pre: diccionario fue creado, sus valores son numericos y sólo existe
un tipo de par clave-valor
Post: se retornó lista de tuplas
"""
def ordenar_y_devolver_mayores( diccionario, tam_dic ,n ):
    heap = []
    heap_aux =[]
    #bueno, basicamente es hacer push y después pop (lo vi en la lista de correos),
    #no encontré otra forma de atacar el problema con el heap
    for u in diccionario:
        heapq.heappush(heap_aux,(diccionario[u],u))
    tam_heap = tam_dic
    while tam_heap > 0 :
        valor,clave = heapq.heappop(heap_aux)
        heapq.heappush(heap,(valor,clave))
        tam_heap-=1
    del(heap_aux)
    #no sé bien cual es la complejidad de heapq.nlargest
    mayores = heapq.nlargest(int(n),heap)
    return mayores

"""
Pre:
Post:
"""
def similares( id_usuario, cantidad_similares ):
    usuarios,len_usuarios = random_walks( g, id_usuario,False )
    similares_mayores = ordenar_y_devolver_mayores(usuarios,len_usuarios,cantidad_similares)
    print(similares_mayores) #el print este es de prueba

"""
Pre:
Post:
"""
def recomendar(id_usuario, cantidad_recomendados ):
    usuarios,len_usuarios = random_walks( g, id_usuario,True )
    recomendados_mayores = ordenar_y_devolver_mayores(usuarios, len_usuarios, cantidad_recomendados )
    print(recomendados_mayores) #el print este es de prueba

################################ Main ##################################

g = Grafo(False)
cargar_grafo(g)
similares("1","13")

