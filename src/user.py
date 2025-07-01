'''khoi tao nguoi dung
    admin : người quản lí hệ thống
        + có thể cập nhật trạm và tuyến
    normal_user: 
        + tìm trạm và tuyến
        + in ra đường ngắn nhất
        
'''
from system import System
# các function trong này gọi func từ system
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def view_routes(self):
        pass  # List available routes

    def search_path(self, system, start_station, end_station):
        pass  # Trigger pathfinding using system object, 



class NormalUser(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def view_map(self, system):
        pass  # gọi system to view map


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def add_station(self, system, station_id, station_name):
        pass  # gọi system.add_station

    def remove_station(self, system, station_id):
        pass  # gọi system.remove_station

    def add_route(self, system, route_id, station_list):
        pass  # gọi system.add_route

    def remove_route(self, system, route_id):
        pass  # gọi system.remove_route

    def update_route(self, system, route_id, new_station_list):
        pass  # gọi system.update_route
