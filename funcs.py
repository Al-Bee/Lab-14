from node import Node

def print_node_chain(n):
    if n.get_next() == None:
        print(n.get_data())
    else:
        print(n.get_data(), end=' ')
        print_node_chain(n.get_next())

def get_reversed(n):
    if n.get_next() == None:
        return [n.data]
    else:
        return get_reversed(n.get_next()) + [n.data]
    
def get_all_vowels(n):
    if n.get_next() == None:
        return [n.get_vowels()]
    else:
        return [n.get_vowels()] + get_all_vowels(n.get_next())
    
def reverse_node_chain(n):
    nodes = []
    new = []
    while True:
        if n.get_next() != None:
            nodes.append(n.get_data())
            n = n.get_next()
        else:
            nodes.append(n.get_data())
            break
    nodes.reverse()
    for i in range(len(nodes)):
        

    print(nodes)


	
node1 = Node('hello')
node2 = Node('world')
node1.set_next(node2)
result = reverse_node_chain(node1)
#print_node_chain(result)
#print_node_chain(node1)
if not isinstance(result, Node):
    print("result must be an object of the Node class")
