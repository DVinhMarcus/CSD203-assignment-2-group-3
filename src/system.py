from graph import Graph
from user import User
from AVL import AVL

class System:
    def __init__(self):
        pass  # Initialize graph, AVL trees for users/routes, etc.

    # --- User management ---
    def add_user(self, user_id, user_data):
        pass  # Add user to AVL tree

    def remove_user(self, user_id):
        pass  # Remove user from AVL tree

    def add_admin(self, admin_id, admin_data):
        pass  # Add admin to AVL tree

    def remove_admin(self, admin_id):
        pass  # Remove admin from AVL tree

    # --- Route management ---
    def add_route(self, route_id, station_list):
        pass  # Add route to AVL tree, update graph edges

    def remove_route(self, route_id):
        pass  # Remove route from AVL tree, update graph

    def update_route(self, route_id, new_station_list):
        pass  # Update existing route with new stations

    # --- Station / bus stop management ---
    def add_station(self, station_id, station_data):
        pass  # Add station to graph

    def remove_station(self, station_id):
        pass  # Remove station from graph

    # --- Search / user features ---
    def find_shortest_path(self, start_station, end_station):
        pass  # Call graph's Dijkstra

    def find_min_transfer_path(self, start_station, end_station):
        pass  # Call graph's BFS

    def view_map(self):
        pass  # Call graph traversal or print adjacency list

    # --- Utility ---
    def load_test_data(self):
        pass  # Load sample stations/routes/users

    def save_system_state(self):
        pass  # Save current system to file (optional)

    def load_system_state(self):
        pass  # Load system state from file (optional)
