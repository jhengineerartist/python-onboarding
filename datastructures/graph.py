class DirectedEdge:
    '''
    Edges have an origin and a destination node. Edges can also have a weight

    Nodes are referred to by their id. 
    '''

    def __init__(self, origin_node_id, destination_node_id, weight):
        self.origin_id = origin_node_id
        self.destination_id = destination_node_id
        self.weight = weight

    def __repr__(self):
        return f'DirectedEdge({self.origin_id!r}, {self.destination_id!r}, {self.weight})'


class Node:
    '''
    Nodes contain an id, and a dictionary of edges going to neighbor nodes

    The outgoing edges of this node are keyed according to their destination node
    '''

    def __init__(self, id, edges=None):
        self.id = id
        if (edges is not None):
            self.__edges = edges
        else:
            self.__edges = {}

    def __repr__(self):
        return f'Node({self.id!r}, {self.__edges!r})'

    @property
    def destinations(self):
        return self.__edges

    def add_edge(self, edge):
        added = edge.destination_id not in self.__edges.keys()
        if added:
            self.__edges[edge.destination_id] = edge
        return added

    def remove_edge(self, dest_node_id):
        removed = dest_node_id in self.__edges.keys()
        if removed:
            self.__edges.pop(dest_node_id)
        return removed

    def update_edge(self, edge):
        updated = edge.destination_id in self.__edges.keys()
        if updated:
            self.__edges[edge.destination_id] = edge
        return updated


class DirectedGraph:
    def __init__(self, nodes=None):
        if nodes is not None:
            self.__nodes = nodes
        else:
            self.__nodes = {}

    def __repr__(self):
        return f'DirectedGraph({self.__nodes!r})'

    def add_node(self, node_id):
        added = self.__nodes == None or node_id not in self.__nodes.keys()
        if added:
            node = Node(node_id)
            self.__nodes[node_id] = node
        return added

    def add_edge(self, orig_node_id, dest_node_id, weight):
        added = (orig_node_id in self.__nodes.keys() and
                 dest_node_id in self.__nodes.keys())

        edge = DirectedEdge(orig_node_id, dest_node_id, weight)

        # Short circuiting for easier debugging and control
        added = added and self.__nodes[orig_node_id].add_edge(edge)
        return added

    def update_edge(self, orig_node_id, dest_node_id, weight):
        updated = (orig_node_id in self.__nodes.keys() and
                   dest_node_id in self.__nodes.keys())

        edge = DirectedEdge(orig_node_id, dest_node_id, weight)

        updated = updated and self.__nodes[orig_node_id].update_edge(edge)
        return updated

    def remove_edge(self, orig_node_id, dest_node_id):
        removed = (orig_node_id in self.__nodes.keys() and
                   dest_node_id in self.__nodes.keys())

        removed = (removed and
                   self.__nodes[orig_node_id].remove_edge(dest_node_id))
        return removed

    def bfs_path_to_node(self, orig_node_id, dest_node_id):
        '''
        BFS returns a list of all nodes reachable from the origin node in order of least
        steps for each level of depth

        BFS uses a queue to create a list of traveled nodes that are in order of the number
        of edge traversals relative to the starting node 
        '''
        can_path = (orig_node_id in self.__nodes.keys() and
                    dest_node_id in self.__nodes.keys())

        visited_nodes = [orig_node_id]
        if can_path and orig_node_id != dest_node_id:
            visited_nodes = [orig_node_id]
            bfs_queue = [orig_node_id]

            while (len(bfs_queue) > 0):
                current_node_id = bfs_queue.pop(0)
                # BFS adds each neigbor of the current node to the queue. Next iteration will pop the last one
                # that was added
                for neighbor_node_id in self.__nodes[current_node_id].destinations.keys():
                    if neighbor_node_id not in visited_nodes:
                        visited_nodes.append(neighbor_node_id)
                        bfs_queue.append(neighbor_node_id)

        can_path = dest_node_id in visited_nodes

        return can_path, visited_nodes
