class RomaniaMap(object):

	def __init__(self):
		self.coords = coords = {
			'Arad': (45,132),
			'Bucharest': (450,346),
			'Craiova': (256,400),
			'Dobreta': (143,382),
			'Eforie': (661,390),
			'Fagaras':(328,186),
			'Giurgiu':(416,420),
			'Hirsova':(623,317),
			'Iasi': (544,113),
			'Lugoj': (144,280),
			'Mehadia':(148,330),
			'Neamt': (459,70),
			'Oradea': (99,26),
			'Pitesti':(345,294),
			'Rimnicu Vilcea': (231,235),
			'Sibiu': (199,175),
			'Timisoara': (50,237),
			'Urziceni': (523,316),
			'Vaslui': (591,193),
			'Zerind': (69,79)
		}
		self.dictionary = {
			'Arad': [366, [('Zerind', 75), ('Timisoara', 118),('Sibiu',140)]],
			'Bucharest': [0, [('Giurgiu', 90), ('Urziceni', 85),('Fagaras',211),('Pitesti',101)]],
			'Craiova': [160, [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti',138)]],
			'Dobreta': [242, [('Mehadia', 75), ('Craiova',101)]],
			'Eforie': [161, [('Hirsova', 86)]],
			'Fagaras':[178, [('Sibiu', 99), ('Bucharest', 211)]],
			'Giurgiu':[77, [('Bucharest', 90)]],
			'Hirsova':[151, [('Urziceni', 98), ('Eforie', 86)]],
			'Iasi': [226, [('Neamt', 87), ('Vaslui', 92)]],
			'Lugoj': [244, [('Mehadia', 70), ('Timisoara', 111)]],
			'Mehadia': [241, [('Lugoj', 70), ('Dobreta', 75)]],
			'Neamt': [234, [('Iasi', 87)]],
			'Oradea': [380, [('Sibiu', 151), ('Zerind', 71)]],
			'Pitesti': [98, [('Rimnicu Vilcea', 97), ('Craiova', 138),('Bucharest',101)]],
			'Rimnicu Vilcea': [193, [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)]],
			'Sibiu': [253, [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)]],
			'Timisoara': [329, [('Arad', 118), ('Lugoj', 111)], ('Oradea', 151)],
			'Urziceni': [80, [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)]],
			'Vaslui': [199, [('Iasi', 92), ('Urziceni', 142)]],
			'Zerind': [374, [('Arad', 75), ('Oradea', 71)]]
		}
	def get_city_coords(self, key):
		return self.coords[key]
	def get_cities(self):
		return self.dictionary