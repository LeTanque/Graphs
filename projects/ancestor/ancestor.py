# Write a function:
# given the dataset and the ID of an individual in the dataset,
# returns their earliest known ancestor –
#
# the one at the farthest distance from the input individual.
#
# If there is more than one ancestor tied for "earliest",
# return the one with the lowest numeric ID.
#
# If the input individual has no parents, the function should return -1.
#
# * The input will not be empty.
# * There are no cycles in the input.
# * There are no "repeated" ancestors – if two individuals are connected,
#   it is by exactly one path.
# * IDs will always be positive integers.
# * A parent may have any number of children.


class Stack():
    def __init__(self):
        self.stack = []

    def add(self, value):
        if type(value) is int:
            self.stack.append([value])
        else:
            self.stack.append(value)

    def pop(self):
        if self.total_size() > 0:
            return self.stack.pop(0)
        else:
            return None

    def print_stack(self):
        if self.total_size() > 0:
            for item in self.stack:
                return item
        else:
            print("   ###   no stack")

    def total_size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}
        self.earliest = {}
        # self.counter = 0
        # self.longest_chain = 1

    def add_family(self, family):
        # Add both vertices in each node
        for node in family:
            for vertex in node:
                if vertex not in self.vertices:
                    self.vertices[vertex] = set()
        # Build edges in reverse. We want to know
        # who the parents are, not the children
        for node in family:
            if node[0] in self.vertices and node[1] in self.vertices:
                self.vertices[node[1]].add(node[0])
            else:
                raise IndexError("That vertex does not exist!")

    # def get_ancestors(self, vertId):
    #     self.counter += 1
    #     if self.counter > self.longest_chain:
    #         self.longest_chain = self.counter
    #     if len(self.vertices[vertId]) is 0:
    #         self.counter = 0
    #         return "no parents"
    #     return self.vertices[vertId]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    stack = Stack()
    # stop = False
    max_length = 1
    earliest_ancestor = -1
    iterations = 0

    # Create our graph from ancestors
    if len(graph.vertices) is 0:
        graph.add_family(ancestors)

    # print('>>> Vertices: \n', graph.vertices, "\n")

    if len(graph.vertices[starting_node]) == 0:
        return earliest_ancestor

    # This is a Breadth First Traversal
    #
    # Add the starting node to the stack
    #
    # As we add nodes to the stack, we are logging
    # the longest chain and earliest ancestor
    #
    # Our end condition is when we pop the stack
    # and there are no more relatives in vertices
    stack.add(starting_node)

    while stack.total_size() > 0:
        iterations += 1
        path = stack.pop()
        treetop = path[-1]
        # # This console will show the alternate paths taken
        # print('\ntreetop, path, iterations: ', treetop, path, iterations)

        # If the current path is longer than the max length,
        # set the counters (earliest_ancestor and max_length)
        if len(path) >= max_length:
            # print('   len(path) x max_length: ', len(path), max_length)
            earliest_ancestor = treetop
            max_length = len(path)

        for relative in graph.vertices[treetop]:
            # List is required here in order to make a new copy of
            # the path list.
            # Without list(), we only take one path.
            path_copy = list(path)
            path_copy.append(relative)
            stack.add(path_copy)

    print('\n   earliest_ancestor: ', earliest_ancestor)
    print('   iterations: ', iterations, "\n")
    return earliest_ancestor


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(test_ancestors, 6)
