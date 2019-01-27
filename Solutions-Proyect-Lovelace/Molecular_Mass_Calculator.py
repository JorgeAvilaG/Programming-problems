#This problem asks for a function to calculate the molecular mass for different compounds.
#This version passes the tests in the Proyect Lovelace but with complex formulas or special nomemclature
#will not work. Example: '(NCH3)3PO2'   'Ph3N'


import csv
import re
#A dictionary is used to load the atomic mass for each element.
elements = {}
with open('periodic_table.csv') as csvfile:
    periodic_table_reader = csv.reader(csvfile, delimiter=',')
    for row in periodic_table_reader:
        elements[row[0]] = float(row[1])
        
#The function uses Regex to identify different elements and the times it appears.        
def molecular_mass(chemical_formula):
    mass = 0
    atoms = re.findall('[A-Z][a-z]?\d*', chemical_formula)
    
    for atom in atoms:
        element = re.search('[A-Z][a-z]?',atom)[0]
        number = re.search('\d+',atom)
        if number:
            number = int(re.search('\d+',atom)[0])           
        else:
            number = 1
        mass += elements[element]*number
    return mass  
