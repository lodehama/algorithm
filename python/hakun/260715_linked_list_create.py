class Node:
	def __init__(self, data):
		self.data = data
		self.link = None


# 첫 번째 노드 생성
p1 = Node(10)

# 두 번째 노드 생성
p2 = Node(20)

# 연결
p1.link = p2

print(p1.data)         # 10
print(p1.link.data)    # 20
print(p2.data)         # 20