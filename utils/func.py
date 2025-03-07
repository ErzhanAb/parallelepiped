# ============================================================ Import modules ============================================================ #

import json
import math as mt
from time import sleep



# ============================================================ parallelepipeds.json ============================================================ #

# Function to open 'parallelepipeds.json'
def read_json(file) -> dict:

    '''
    The function takes one argument - a json file to read and returns the file as a dictionary
    '''

    with open(file, 'r') as f:
        p = json.load(f)
    return p



# ============================================================ characteristics ============================================================ #

# Functions for generating the 'characteristics' dictionary
def get_diag(a: float, b: float, c: float) -> float:
  return mt.sqrt(a**2 + b**2 + c**2)

def get_volume(a: float, b: float, c: float) -> float:
  return a*b*c

def get_surface(a: float, b: float, c: float) -> float:
  return 2* (a*b + a*c + b*c)

def get_alpha(a: float, b: float, c: float) -> float:
  return mt.degrees(mt.acos(a/mt.sqrt(a**2 + b**2 + c**2)))

def get_beta(a: float, b: float, c: float) -> float:
  return mt.degrees(mt.acos(b/mt.sqrt(a**2 + b**2 + c**2)))

def get_gamma(a: float, b: float, c: float) -> float:
  return mt.degrees(mt.acos(c/mt.sqrt(a**2 + b**2 + c**2)))

def get_sphr_radius(a: float, b: float, c: float) -> float:
  return mt.sqrt(a**2 + b**2 + c**2) / 2

def get_sphr_volume(a: float, b: float, c: float) -> float:
  return 4/3*mt.pi * (mt.sqrt(a**2 + b**2 + c**2) / 2)**3

def process(a: float, b: float, c: float) -> dict:
  fig_dict = {
    "diag": str(get_diag(a, b, c)),
    "volume": str(get_volume(a, b, c)),
    "surface_area": str(get_surface(a, b, c)), 
    "alpha": str(get_alpha(a, b, c)),
    "beta": str(get_beta(a, b, c)),
    "gamma": str(get_gamma(a, b, c)),
    "radius_described_sphere": str(get_sphr_radius(a, b, c)),
    "volume_described_sphere": str(get_sphr_volume(a, b, c))
  }
  return fig_dict

# Function to create dictionary 'characteristics'
def get_characteristics(a: dict) -> dict:
    
    '''
    The function takes one argument - a dictionary and returns a new generated dictionary after calculations
    '''

    characteristics = {}
    for figure, atr_dict in a.items():
        a = float(atr_dict['a'])
        b = float(atr_dict['b'])
        c = float(atr_dict['c'])
        characteristics[figure] = process(a, b, c)
    return characteristics



# ============================================================ statistics ============================================================ #

# Function to create dictionary 'statistics'
def get_statistics(a: dict) -> dict:
    
    '''
    The function takes one argument - a dictionary and returns a new dictionary containing the average values
    '''
    
    statistics = {
        "avg_diag": [],
        "avg_volume": [],
        "avg_surface_area": [],
        "avg_alpha": [],
        "avg_beta": [],
        "avg_gamma": [],
        "avg_radius_described_sphere": [],
        "avg_volume_described_sphere": []
    }
    for figure in a.values():
        statistics['avg_diag'].append(float(figure['diag']))
        statistics['avg_volume'].append(float(figure['volume']))
        statistics['avg_surface_area'].append(float(figure['surface_area']))
        statistics['avg_alpha'].append(float(figure['alpha']))
        statistics['avg_beta'].append(float(figure['beta']))
        statistics['avg_gamma'].append(float(figure['gamma']))
        statistics['avg_radius_described_sphere'].append(float(figure['radius_described_sphere']))
        statistics['avg_volume_described_sphere'].append(float(figure['volume_described_sphere']))
    statistics = {key: str(round(sum(value) / len(value), 2)) for key, value in statistics.items()}
    return statistics



# ============================================================ characteristics.json и statistics.json ============================================================ #

# Function to create 'characteristics.json' and 'statistics.json' files
def create_json(filename: str, file: dict) -> None:
    
    '''
    The function takes two arguments:
    1) filename - path to create file
    2) file - dictionary from which file is created
    '''
    
    with open(filename, 'w') as f:
        json.dump(file, f, indent = 4)
    print(f'File created in directory: {filename}')



# ============================================================ Outputting messages ============================================================ #

def print_msg() -> None:
    
    '''
    The function outputs program execution information
    '''

    pict_list = ['MY FIRST SCRIPT\n',
                '    *********',
                '   *       **',
                '  *       * *',
                ' *********  *',
                ' *       *  *',
                ' *       *  *',
                ' *       * *',
                ' *********',
              '\nI LOVE PYTHON']
    for i in pict_list:
        sleep(.4)
        print(i)


    characteristics = get_characteristics(read_json('parallelepipeds.json'))
    print()
    print()
    print('================================================================================')
    print(f'Total number of figures: {len(characteristics)}')
    print('================================================================================')
    print()


    statistics = get_statistics(characteristics)
    print()
    print('================================================================================')
    print(f'Average of all main diagonals: {statistics["avg_diag"]}')
    print(f'The average value of all volumes of a parallelogram: {statistics["avg_volume"]}')
    print(f'The average value of all surface areas of a parallelogram: {statistics["avg_surface_area"]}')
    print(f'Average value of all angles "alpha": {statistics["avg_alpha"]}')
    print(f'The average value of all angles is "beta": {statistics["avg_beta"]}')
    print(f'Average value of all angles "gamma": {statistics["avg_gamma"]}')
    print(f'The average value of all radii of the circumscribed sphere: {statistics["avg_radius_described_sphere"]}')
    print(f'The average value of all volumes of the circumscribed sphere: {statistics["avg_volume_described_sphere"]}')
    print('================================================================================')
    print()