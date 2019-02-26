from log_config import create_log

logger = create_log('log.log')


def check_line(coords, index):
    """

    :param coords: массив с координатами точек, заданный пользователем
    :param index: 0: проверяем наличие прямой, || x; 1: проверяем наличие прямой, || x
    :return: 0/1 - факт существования прямой
    """
    logger.debug(f'Функция запущена с входными координатами {coords} по оси {index}')
    copy_coords = coords[:]
    pair_points = []
    for i, point in enumerate(copy_coords):
        list_for_search = copy_coords[:]
        list_for_search.pop(i)
        for j in list_for_search:
            if point[index] == j[index]:
                pair_points.append([point, j])
                copy_coords.remove(j)
    if len(pair_points) == len(coords) / 2:
        logger.debug(f'Есть вероятность, что все точки симметричны по оси {index}')
        index = 0 if index else 1
        avgs = [(pair[0][index] + pair[1][index]) / 2 for pair in pair_points]
        avg = sum(avgs) / len(avgs)

        # if avgs[0] == sum(avgs) / len(avgs):
        if all([i == avg for i in avgs]):
            logger.debug(f'Симметрия найдена по оси {0 if index else 1}')
            return True
        else:
            logger.debug(f'Не совпадает расстояние м/у точками, подозрительными на симметрию,'
                         f' относительно оси {0 if index else 1}')
            return False
    else:
        logger.debug(f'Отсутствуют точки, подозрительные на симметрию,  на оси {index}')
        return False


def run():
    coords = []
    print("Введите четное число координат точек. Для выхода из режима ввода нажмите 'q':")
    while True:
        n = input()
        if n == 'q':
            if len(coords) % 2:
                while n == 'q':
                    print(
                        'Должно быть задано четное число точек!'
                        ' Введите еще одну пару точек, затем выйдите из программы')
                    n = input()
            else:
                if not len(coords):
                    while n == 'q':
                        print('Задан пустой массив. Введите кооординаты точек')
                        n = input()
                else:
                    break
        n = tuple(map(float, n.split()))
        coords.append(n)

    #   Запускаем проверку по OY
    if check_line(coords, 1):
        print('YES')
    else:
    #   Запускаем проверку по OX
        if check_line(coords, 0):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    run()
