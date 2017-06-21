#implementacion de un grafo

# Definicion del TDA Grafo
class Grafo:
	def __init__(self, dir):
			self.dic = {}
			self.dir = dir
			self.cant_vert = 0
			self.cant_ari = 0

# Devuelve True al quitar un vertice o False si el
# vertice no pertenece al grafo.
# Post: el grafo tiene un vertice menos
	def	quitar_vertice(self, v):
			if not self.existe_vertice(v):
				return False

			del self.dic[v]

			for i in self.dic:
				if v in self.dic[i]:
					del self.dic[i][v]
			self.cant_vert -= 1
			return True

# Devuelve True al agregar un vertice al grafo,
# False si el vertice ya pertenece al grafo
	def	agregar_vertice(self, v):
			if self.existe_vertice(v):
				return False

			self.dic[v] = {}
			self.cant_vert += 1
			return True

# Devuelve True si un vertice pertenece al grafo,
# False en caso contrario
	def	existe_vertice(self, v):
			return v in self.dic

# Devuelve la cantidad de vertices en el grafo
	def	cant_vertices(self):
			return self.cant_vert

# Devuelve la cantidad de aristas en el grafo
	def	cant_aristas(self):
			return self.cant_ari

# devuelve la lista de vertices adyacentes al vertice
# pasado por parametro o None si el vertice no existe
	def	adyacentes(self, v):
			if not self.existe_vertice(v):
				return None

			return self.dic[v]

# devuelve True si dos vertices son adyacentes entre si
# False en caso contrario
#en un grafo dirigido, son_adyacentes(v1, v2) es True, pero son_adyacentes(v2, v1) es False
#si v2 es adyacente de v1.
#en un grafo no dirigido, tanto son_adyacentes(v1, v2) como son_adyacentes(v2, v1) son True
#si v2 es adyacente de v1
	def	son_adyacentes(self, v1, v2):
			if not self.existe_vertice(v1) and not self.existe_vertice(v2):
				return false

			uno_con_dos = v2 in self.adyacentes(v1)

			if self.dir:
				return uno_con_dos

			dos_con_uno = v1 in self.adyacentes(v2)

			return uno_con_dos and dos_con_uno

# Devuelve True al agregar una arista entre dos vertices
# Si los vertices son adyacentes o alguno de ellos
# no existe, devuelve False
	def	agregar_arista(self, v1, v2):
			if not self.existe_vertice(v1) or not self.existe_vertice(v2):
				return False

			if self.son_adyacentes(v1,v2):
				return False

			self.dic[v1][v2] = None

			if not self.dir:
				self.dic[v2][v1] = None

			self.cant_ari += 1
			return True

# Devuelve True al quitar una arista entre dos vertices.
# Si los vertices no son adyacentes o alguno de ellos no existe,
# devuelve False
	def	quitar_arista(self, v1, v2):
			if not self.existe_vertice(v1) or not self.existe_vertice(v2):
				return False

			if not self.son_adyacentes(v1,v2):
				return False

			del self.dic[v1][v2]

			if not self.dir:
				del self.dic[v2][v1]

			self.cant_ari -= 1
			return True

#Devuelve una lista con los Vertices del grafo.
	def vertices(self):
		return list(self.dic.keys())

#Proximamente: iterador