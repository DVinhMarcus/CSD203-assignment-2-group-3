#file tạo graph để quản lí station
# chỉ cần áp dụng các function của graph  như bình thường


class Graph:
    def __init__(self):
        self.vertices = {}  # {vertex_id: {neighbor_id: weight}}

    # --- Graph construction ---
    def add_vertex(self, vertex_id):
        pass  # TODO: implement

    def remove_vertex(self, vertex_id):
        pass  # TODO: implement

    def add_edge(self, source_id, dest_id, weight=1):
        pass  # TODO: implement

    def remove_edge(self, source_id, dest_id):
        pass  # TODO: implement

    # --- Graph queries ---
    def get_adjacent_vertices(self, vertex_id):
        pass  # TODO: implement

    def get_edge_weight(self, source_id, dest_id):
        pass  # TODO: implement

    def get_vertices(self):
        pass  # TODO: implement

    def get_edges(self):
        pass  # TODO: implement

    # --- Pathfinding / traversal ---
    def find_shortest_path(self, start_id, end_id):
        pass  # TODO: implement Dijkstra

    def find_path_min_hops(self, start_id, end_id):
        pass  # TODO: implement BFS

    def dfs_traversal(self, start_id):
        pass  # TODO: implement DFS

    def bfs_traversal(self, start_id):
        pass  # TODO: implement BFS

    # --- Utility ---
    def print_adjacency_list(self):
        pass  # TODO: implement

    def is_connected(self):
        pass  # TODO: optional, check connectivity

    def has_cycle(self):
        pass  # TODO: optional, check for cycles
