# station.py
''' file khởi tạo trạm
    1 trạm có:
        - các tuyến đi qua
        - các  trạm khác nối với trạm đó
''' 
class Station:
    def __init__(self, station_id, name):
        self.station_id = station_id
        self.name = name
        self.routes = set()  # Routes passing through this station
        self.neighbors = {}  # {neighbor_station_id: weight}

    def add_neighbor(self, neighbor_id, weight):
        pass  # Add neighbor station with weight

    def remove_neighbor(self, neighbor_id):
        pass  # Remove neighbor station

    def add_route(self, route_id):
        pass  # Add a route passing through this station

    def remove_route(self, route_id):
        pass  # Remove a route from this station

    def get_info(self):
        pass  # Return station details