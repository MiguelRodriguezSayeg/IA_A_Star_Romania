def solve(root_key, cities):
	from node import Node
	import collections
	LAST_NODE_KEY = 'Bucharest'

	visited = collections.deque([])

	#Creating first City Node

	root_items = cities[root_key]

	root = Node(root_key, root_items[0])

	visited.append(root)

	for counter, neighbor in enumerate(root_items[1]):
		root.add_child(Node(neighbor[0],\
			cities[neighbor[0]][0], \
			root_items[1][counter][1],\
			root)) 
	#Solution
	while True:
		if root.children:
			root.children.sort(key=lambda child: child.f)
			if root.children[0].city_name not in [rom_city.city_name for rom_city in visited]:
				root = root.children[0]
				visited.append(root)
				if root.city_name == LAST_NODE_KEY:
					return [visited.popleft().city_name for _ in range (0, len(visited))]
					break
				else:
					root_items=cities[root.city_name]
					for counter, neighbor in enumerate(root_items[1]):
							root.add_child(Node(neighbor[0],\
								cities[neighbor[0]][0], \
								root_items[1][counter][1],\
								root))
			else:
				root.children.pop(0)
		else:
			root = root.parent
			root.parent.children.pop(0)
			visited.pop()


