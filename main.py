# Импорт модулей
import json
from utils.func import read_json
from utils.func import get_characteristics
from utils.func import get_statistics
from utils.func import create_json
from utils.func import print_msg


# Чтение файла 'parallelepipeds.json'
p = read_json('parallelepipeds.json')


# Создание и генерация словаря 'characteristics'
characteristics = get_characteristics(p)


# Создание и генерация словаря 'statistics'
statistics = get_statistics(characteristics)


# Вывод сообщений о выполнении программы
print_msg()


# Создание json файлов
create_json('outputs/characteristics.json', characteristics)
create_json('outputs/statistics.json', statistics)