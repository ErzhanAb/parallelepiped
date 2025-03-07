# Import modules
import json
from utils.func import read_json
from utils.func import get_characteristics
from utils.func import get_statistics
from utils.func import create_json
from utils.func import print_msg


# Reading file 'parallelepipeds.json'
p = read_json('parallelepipeds.json')


# Creating and generating the 'characteristics' dictionary
characteristics = get_characteristics(p)


# Creating and generating the 'statistics' dictionary
statistics = get_statistics(characteristics)


# Outputting program execution messages
print_msg()


# Creating json files
create_json('outputs/characteristics.json', characteristics)
create_json('outputs/statistics.json', statistics)