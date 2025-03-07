# README

## Project Description
This project is designed to work with parallelepiped parameters. The program reads input data from a JSON file, calculates the characteristics of each figure, generates statistics, and saves the results in separate files.

## Requirements
Before starting, make sure you have Python version 3.8 or higher installed.

## Installation and Running

### 1. Cloning the Repository
First, clone the project repository:
```sh
git clone https://github.com/ErzhanAb/parallelepiped.git
cd parallelepiped
```

### 2. Creating the Output Folder
Before running the program, create an `outputs` folder in the project's root directory:
```sh
mkdir outputs
```

### 3. Running the Program
Run the main script:
```sh
python main.py
```

After executing the script, two files will appear in the `outputs` folder:
- `characteristics.json` — contains the characteristics of all figures
- `statistics.json` — contains the average values of the characteristics

## Project Structure
```
<project_name>/
│── utils/
│   ├── func.py           # Main data processing functions
│── main.py               # Main script of the program
│── parallelepipeds.json  # Input data
│── outputs/              # Folder for output data
│   ├── characteristics.json  # File with figures' characteristics
│   ├── statistics.json       # File with calculated statistics
```
