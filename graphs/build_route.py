LON_MIN = 38.9774837690821
LON_MAX = 39.0283642309179
LAT_MIN = 45.0549145480683
LAT_MAX = 45.0908534519317


def check_coords(lon_min, lon_max, lat_min, lat_max):
    restr = f'Долгота от {lon_min} до {lon_max}, широта от {lat_min} до {lat_max}:\n'
    point = tuple(map(float, input(f'Введите координаты точек для построения маршрута.\n {restr}').split()))
    while not ((lon_min <= point[0] <= lon_max) or (lat_min <= point[1] <= lat_max)):
        point = tuple(map(float, input(f'Координаты заданы неверно!\n {restr}').split()))
    return point


coords = [check_coords(LON_MIN, LON_MAX, LAT_MIN, LAT_MAX) for _ in range(2)]
print(coords)






