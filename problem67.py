from lib2to3.pytree import convert


class Node(object):
    def __init__(self, value, distance = 0):
        self.value = value
        self.distance = distance
        self.attached_node: list[Node] = []

    def attach_node(self, node):

       self.attached_node.append(node)

    def select_farthest_node(self):
        farthest_node: Node = Node(0, 0)
        for node in self.attach_node:
            if node > farthest_node:
                farthest_node = node
        return node

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __ne__(self, other):
        return self.distance != other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

def attach_adjacent(data: list[Node], x: int, y: int, y_max: int):
    actual_node: Node = data[y][x]

    if y + 1 < y_max:
        print(f"Attaching node {(y, x)} to {(y+1, x)}")
        actual_node.attach_node(data[y + 1][x])

        if x - 1 >= 0:
            print(f"Attaching node {(y, x)} to {(y+1, x - 1)}")
            actual_node.attach_node(data[y + 1][x - 1])  

        if x + 1 < len(data[y + 1]):
            print(f"Attaching node {(y, x)} to {(y+1, x + 1)}")
            actual_node.attach_node(data[y + 1][x + 1])

def create_tree(file_name: str) -> Node:
    file = open(file_name)
    lines = file.readlines()
    file.close()

    def load_data(data) -> None:
        for line in lines:
            value = line.replace("\n", "").split(" ")
            for i in range(0, len(value)):
                value[i] = int(value[i])
            data.append(value)

    def convert_to_node(data: list[int]) -> None:
        for y in range(y_size):
            for x in range(len(data[y])):
                data[y][x] = Node(data[y][x])

    
    data: list[list[Node]] = []
    load_data(data)
    
    y_size = len(data)
    convert_to_node(data)

    for y in range(y_size - 1):
        for x in range(len(data[y])):
            attach_adjacent(data, x, y, y_size)

    return data[0][0]

if __name__ == "__main__":
    first_node: Node = create_tree("triangle.txt")

