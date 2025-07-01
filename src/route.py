'''
file khởi tạo thực thể route 
 1 route có các trạm đi qua
 1 route có bao nhiêu xe hoạt động 
'''
class Route:
    def __init__(self, route_id, station_list):
        self.route_id = route_id
        self.station_list = station_list  # Ordered list of station IDs
        self.num_vehicles = 0  # Number of vehicles assigned (optional)

    def update_stations(self, new_station_list):
        #phải check các trạm input có liền kề không
        # check trùng tuyến cũ chưa
        # Update the list of stations in the route
        pass    

    def set_num_vehicles(self, num):
        pass  # Set or update number of vehicles

    def get_info(self):
        pass  # Return route details (stations + vehicles)