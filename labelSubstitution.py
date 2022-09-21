#!/usr/bin/env python3.7
# Copyright (c) 2021 Global Ecosystem Dynamics Initiative
# Author(s): Sergio Arturo Ruiz Gutierrez
# Date: 30/11/2021
# -------------------------------------------------------
# Description:
# Tool to subsitute all the names of the organizations 
# with their corresponding label (acronym) as defined
# by the data science team.
# -------------------------------------------------------
# TODO: 
#       -Automate the consolidated and norm-key file 
#        input.
#       -Document properly each function.
#........................................................

import csv
import json
import pandas as pd

def labelSubstitution(consolidatedFile, labeledDataFile, col2Norm):

    jsonarray = []
    newName = []
    with open(labeledDataFile, 'r', encoding='utf-8') as claveNorm:
        reader = csv.DictReader(claveNorm)
        for row in reader:
            jsonarray.append(row)
    with open(consolidatedFile, 'r', encoding='utf-8') as consolidated:
        dictConsolidated = csv.DictReader(consolidated)
            
        for row in dictConsolidated:
           rowValue = row[col2Norm]
           for dictString in jsonarray:
              if rowValue.lower() == dictString['Label'].lower():
                  newName.append(rowValue)
                  break 
              elif rowValue.lower() == dictString['Espacios'].lower():
                  newName.append(dictString['Label'])
                  break            
              elif rowValue.lower() == dictString['Organización'].lower():
                  newName.append(dictString['Label'])
                  break  
              elif rowValue == 'NA':
                  newName.append(rowValue)
                  break
           else: 
               newName.append('No match')
    return newName

def columnSubstitution(consolidatedFile, labeledDataFile):

    cols2Normalize = ['Organization:Contact Information',
                      'Key for establishment', 
                      'Key for growth', 
                      'Target', 
                      'Colabs extra',
                      'Connector:Collaboration 1']
    consolidated = pd.read_csv(consolidatedFile)
    for col2norm in cols2Normalize:
        newName = labelSubstitution(consolidatedFile, labeledDataFile, col2norm)
        df = pd.DataFrame(newName, columns = [col2norm])
        consolidated[col2norm + ' curada'] = df[col2norm]

    finallyNormalizaed = consolidated.to_csv('consolidated-normalized.csv', index = False, na_rep = 'NA')
    
if __name__ == '__main__':
    
    labeledDataFile  = 'key.csv'
    consolidatedFile = 'consolidated_data.csv'
    columnSubstitution(consolidatedFile, labeledDataFile)
