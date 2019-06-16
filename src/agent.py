from node import Node
import collections

class Agent(object):
	def __init__(self, map):
		self.visited = collections.deque([])
		self.TARGET_CITY_KEY = 'Bucharest'
		self.map = map
		self.cities = map.get_cities()
		self.root = None
		self.isFinished = False
	def solve(self, root_key, cities):
		#Creating first City Node

		self.root = Node(root_key, self.cities[root_key][0])

		self.visited.append(self.root)

		for counter, neighbor in enumerate(self.cities[root_key][1]):
			self.root.add_child(Node(neighbor[0],\
				self.cities[neighbor[0]][0], \
				self.cities[root_key][1][counter][1],\
				self.root)) 
		#Solution
		while self.isFinished is False:
			if self.root.children:
				self.root.children.sort(key=lambda child: child.f)
				if self.root.children[0].city_name not in [rom_city.city_name for rom_city in self.visited]:
					self.root = self.root.children[0]
					self.visited.append(self.root)
					if self.root.city_name == self.TARGET_CITY_KEY:
						self.isFinished = True
					else:
						for counter, neighbor in enumerate(self.cities[self.root.city_name][1]):
								self.root.add_child(Node(neighbor[0],\
									self.cities[neighbor[0]][0], \
									self.cities[self.root.city_name][1][counter][1],\
									self.root))
				else:
					self.root.children.pop(0)
			else:
				self.root = self.root.parent
				self.root.parent.children.pop(0)
				self.visited.pop()
		path = [self.visited.popleft().city_name for _ in range (0, len(self.visited))]
		self.visited = collections.deque([])
		self.root = None
		self.isFinished = False
		return path


