class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def view_routes(self):
        pass  # List available routes

    def search_path(self, system, start_station, end_station):
        pass  # Trigger pathfinding using system object


class NormalUser(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def view_map(self, system):
        pass  # Call system to view map


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def add_station(self, system, station_id, station_name):
        pass  # Call system.add_station

    def remove_station(self, system, station_id):
        pass  # Call system.remove_station

    def add_route(self, system, route_id, station_list):
        pass  # Call system.add_route

    def remove_route(self, system, route_id):
        pass  # Call system.remove_route

    def update_route(self, system, route_id, new_station_list):
        pass  # Call system.update_route
