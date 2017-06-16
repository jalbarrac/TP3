#comment
from grafo import Grafo

#	class	Grafo:
#		def __init__(self, dir):		dir = True para un grafo dirigido, False para uno no dirigido
#			self.dic = {}				diccionario vacio
#			self.dir = dir				direccion
#			self.cant					cantidad

#	quitar vertice
#	agregar vertice
#	quitar arista
#	agregar arista
#	son adyacentes
#	adyacentes
#	cantidad
#	existe vertice
#

#Pruebas sobre un grafo no dirigido
print("Crear grafo no dirigido")
g = Grafo(False)

print("Cantidad de elementos en grafo vacio es 0... OK")			if g.cant_vertices() == 0				else print("Cantidad de elementos en grafo vacio es 0... Error")
print("Agregar vertice '1' es True... OK")							if g.agregar_vertice('1')			else print("Agregar vertice '1' es True... Error")
print("Agregar de nuevo vertice '1' es False... OK")				if not g.agregar_vertice('1')		else print("Agregar de nuevo vertice '1' es False... Error")
print("Cantidad de elementos es 1... OK")							if g.cantidad() == 1				else print("Cantidad de elementos es 1... Error")
print("Agregar vertice '2' es True... OK")							if g.agregar_vertice('2')			else print("Agregar vertice '2' es True... Error")
print("Agregar de nuevo vertice '2' es False... OK")				if not g.agregar_vertice('2')		else print("Agregar de nuevo vertice '2' es False... Error")
print("1 y 2 son adyacentes es False... OK")						if not g.son_adyacentes('1', '2')	else print("1 y 2 son adyacentes es False... Error")
print("Quitar arista entre 1 y 2 es False... OK")					if not g.quitar_arista('1', '2')	else print("Quitar arista entre 1 y 2 es False... Error")
print("Cantidad de elementos es 2... OK")							if g.cantidad() == 2				else print("Cantidad de elementos es 2... Error")
print("Agregar arista entre 1 y 2 es True... OK")					if g.agregar_arista('1', '2')		else print("Agregar arista entre 1 y 2 es True... Error")
print("Agregar arista entre 1 y 2 de nuevo es False... OK")			if not g.agregar_arista('1', '2')	else print("Agregar arista entre 1 y 2 de nuevo es False... Error")
print("1 y 2 son adyacentes es True... OK")							if g.son_adyacentes('1', '2')		else print("1 y 2 son adyacentes es True... Error")
print("Existe vertice 1 es True... OK")								if g.existe_vertice('1')			else print("Existe vertice 1 es True... Error")
print("Existe vertice 2 es True... OK")								if g.existe_vertice('2')			else print("Existe vertice 2 es True... Error")

vertices = g.vertices()

print("Elemento 0 en lista de vertices es 1... OK")					if vertices[0] == '1'				else print("Elemento 0 en lista de vertices es 1... Error")
print("Elemento 1 en lista de vertices es 2... OK")					if vertices[1] == '2'				else print("Elemento 1 en lista de vertices es 2... Error")

ady1 = g.adyacentes('1')
ady2 = g.adyacentes('2')

print("Elemento en lista de adyacencia de 1 es 2... OK")			if ady1[0] == '2'					else print("Elemento en lista de adyacencia de 1 es 2... Error")
print("Elemento en lista de adyacencia de 2 es 1... OK")			if ady2[0] == '1'					else print("Elemento en lista de adyacencia de 2 es 1... Error")
print("Quitar arista entre 1 y 2 es True... OK")					if g.quitar_arista('1', '2')		else print("Quitar arista entre 1 y 2 es True... Error")
print("Quitar arista entre 1 y 2 es False... OK")					if not g.quitar_arista('1', '2')	else print("Quitar arista entre 1 y 2 es False... Error")
print("1 y 2 son adyacentes es False... OK")						if not g.son_adyacentes('1', '2')	else print("1 y 2 son adyacentes es False... Error")
print("Quitar vertice 1 es True... OK")								if g.quitar_vertice('1')			else print("Quitar vertice 1 es True... Error")
print("Quitar vertice 1 de nuevo es False... OK")					if not g.quitar_vertice('1')		else print("Quitar vertice 1 de nuevo es False... Error")
print("Quitar vertice 2 es True... OK")								if g.quitar_vertice('2')			else print("Quitar vertice 2 es True... Error")
print("Quitar vertice 2 de nuevo es False... OK")					if not g.quitar_vertice('2')		else print("Quitar vertice 2 de nuevo es False... Error")

print("Crear grafo dirigido")
h = Grafo(True)

print("Agregar de vertice '1' es True... OK")						if h.agregar_vertice('1')			else print("Agregar vertice '1' es True... Error")
print("Cantidad de elementos es 1... OK")							if h.cant_vertices() == 1				else print("Cantidad de elementos es 1... Error")
print("Agregar vertice '2' es True... OK")							if h.agregar_vertice('2')			else print("Agregar vertice '2' es True... Error")
print("Agregar de nuevo vertice '2' es False... OK")				if not h.agregar_vertice('2')		else print("Agregar de nuevo vertice '2' es False... Error")
print("Agregar arista entre 1 y 2 es True... OK")					if h.agregar_arista('1', '2')		else print("Agregar arista entre 1 y 2 es True... Error")
print("1 y 2 son adyacentes es True... OK")							if h.son_adyacentes('1', '2')		else print("1 y 2 son adyacentes es True... Error")
print("2 y 1 son adyacentes es False... OK")						if not h.son_adyacentes('2', '1')	else print("2 y 1 son adyacentes es False... Error")