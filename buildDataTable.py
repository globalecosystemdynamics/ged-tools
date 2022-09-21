#!/usr/bin/env python3.7
# Copyright (c) 2021 Global Ecosystem Dynamics Initiative
# Author(s): Sergio Arturo Ruiz Gutierrez
# Date: 16/05/2021
# --------------------------------------------------------
# Description: 
# Tool for building ecosystem directory or "consolidated" 
# from data gathered from ALchemer surveys.
#---------------------------------------------------------


"""

Import required modules. 

re:   Regular Expression Python module. Used for matching 
      header patterns in ALchemer's *.csv survey data.
json: JSON Python module to handle JSON operations.
csv:  CSV Python module to handle CSV operations.

"""
import re
import json
import csv
import os

def csv2json(csvFilePath, jsonOutFile):
    """
    Parses the ALchemer *.csv output to JSON structure for better handling of
    data values.

    Params:
    csvFilePath: Path to ALchemer *.csv file to parse.
    jsonOutFile: Name of the new JSON output file.

    Output:
    JSON file with json structures for each of the participants of the ALchemer
    survey.

    """
    jsonArray = []

    # Read the csv file provided
    with open(csvFilePath, 'r') as csvFile:
        
        #load csv file using csv module's dic reader
        csvReader = csv.DictReader(csvFile)

        # Convert each csv row into python dict data structure
        for row in csvReader:
            # Add the generated dict structure to our jsonArray variable
            jsonArray.append(row)

    # After we have the complete array of dictionaries we can 
    # convert the jsonArray data into a JSON string/structure
    # then save this structure to a file to ease the manipulation of data
    # as well as having the data in an alternate portable way
    with open(jsonOutFile, 'w') as jsonFile:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonFile.write(jsonString)

def removeQuestion(reg, inputFile, outputFile):
    """
    
    Removes the all the question headers and substitutes each 
    of them with an "id_" prefix. 

    Params:
    reg: Regular expression string.
    inputfile: JSON file from csv2json(csvFilePath, jsonOutFile)
    outputFile: Name of new JSON file with "id_" prefix 
                substitution.

    Returns:
    outputFile

    """
    regCompile = re.compile(reg)
    substitutionString = "\"id_"    
  
    with open(inputFile) as notClean:
        for line in notClean:
            if regCompile.match(line) != None:
                outputFile.write(line)
            else:
                regline = re.sub(reg, substitutionString, line)
                outputFile.write(regline)
        outputFile.close()


def enumID(inputFile, outputFile):
    """
    Enumerates each "id_" prefix to identify each question by
    a number identifier rather than the custom ALchemer output.

    Params: 
    inputFile: JSON file from removeQuestion(reg, inputFile, outputFile)
    outputFile: Name of the enumerated "id_" JSON output file.

    Returns:
    outputFile: Eumerated "id_" JSON output file. 

    """
    i = 1
    stringToReplace = "id_"
    replaceString = "id_"
   
    with open(inputFile) as notEnum:
        for line in notEnum:
            if stringToReplace in line:
                if i == 110:
                    finalString = line.replace(stringToReplace, replaceString + str(i))
                    outputFile.write(finalString)
                    i = 1
                else: 
                    finalString = line.replace(stringToReplace, replaceString + str(i))
                    outputFile.write(finalString)
                    i = i + 1 
            else:
                outputFile.write(line)
        outputFile.close()

# Meat and potatoes
def generateCoolFile(jsonFinal):
    """
    Generates consolidated file.

    Params:
    jsonFinal: Name of the JSON file from enumID(inputFile, outputFile)

    Returns:
    consolidated_data.csv: CSV consolidated.

    """
    with open(jsonFinal, 'r') as jsonFile:
        dataDic = json.load(jsonFile)
        for i in range(len(dataDic)):
            for key in dataDic[i]:
                if dataDic[i][key] == "":
                    dataDic[i][key] = "NA"
                    
    csvHeader = ['Response ID',
                 'Bloque', 
                 'Time Started', 
                 'Date Submitted', 
                 'Status',
                 'Contact ID',
                 'Legacy Comments',
                 'Comments',
                 'Language',
                 'Referer',
                 'SessionID',
                 'User Agent', 
                 'Tags', 
                 'IP Adress', 
                 'Longitud', 
                 'Latitude',
                 'Country', 
                 'City', 
                 'State/Region', 
                 'Postal', 
                 'Organization:Contact Information', 
                 'Organization:Contact Information curada', 
                 'Full Name:Contact Information', 
                 'Job title:Contact Information', 
                 'Email:Contact Information', 
                 'Phone:Contact Information', 
                 'Consent to share contact info', 
                 'Organization size', 
                 'Organization budget', 
                 'Key for establishment',
                 'Key for establishment curada',
                 'Reason (establishment)',
                 'Key for growth',
                 'Key for growth curada',
                 'Reason (growth)', 
                 'Target', 
                 'Target curada', 
                 'Colabs extra', 
                 'Colabs extra curada', 
                 'Directionality:Collaboration 1',
                 'Connector:Collaboration 1', 
                 'Connector:Collaboration 1 curada', 
                 'Sought-after value:Collaboration 1', 
                 'Otro:Sought-after value:Collaboration 1', 
                 'Interactions required:Collaboration 1', 
                 'Formal agreement:Collaboration 1', 
                 'Budget allocated:Collaboration 1',
                 'Human resources allocated:Collaboration 1', 
                 'Success:Collaboration 1', 
                 'Reason (success):Collaboration 1', 
                 'Strength:Collaboration 1']
        
    j = 1
    with open('consolidated_data.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(csvHeader)
        for res in range(len(dataDic)):
            for i in range(1,26):
                try:
                    if j <= 110:
                        thewriter.writerow([dataDic[res]['Response ID'], 
                                           str(i), 
                                           dataDic[res]['Time Started'],
                                           dataDic[res]['Date Submitted'], 
                                           dataDic[res]['Status'], 
                                           dataDic[res]['Contact ID'],
                                           dataDic[res]['Legacy Comments'], 
                                           dataDic[res]['Comments'], 
                                           dataDic[res]['Language'],
                                           dataDic[res]['Referer'], 
                                           dataDic[res]['SessionID'], 
                                           dataDic[res]['User Agent'], 
                                           dataDic[res]['Tags'], 
                                           dataDic[res]['IP Address'], 
                                           dataDic[res]['Longitude'], 
                                           dataDic[res]['Latitude'], 
                                           dataDic[res]['Country'], 
                                           dataDic[res]['City'], 
                                           dataDic[res]['State/Region'], 
                                           dataDic[res]['Postal'], 
                                           dataDic[res]['Organization:Contact Information'],
                                           "Falta Curar", 
                                           dataDic[res]['Full Name:Contact Information'], 
                                           dataDic[res]['Job title:Contact Information'], 
                                           dataDic[res]['Email:Contact Information'], 
                                           dataDic[res]['Phone:Contact Information'], 
                                           dataDic[res]['Consent to share contact info'], 
                                           dataDic[res]['Organization size'], 
                                           dataDic[res]['Organization budget'], 
                                           dataDic[res]['Key for establishment'],
                                           "Falta Curar",
                                           dataDic[res]['Reason (establishment)'], 
                                           dataDic[res]['Key for growth'],
                                           "Falta Curar",
                                           dataDic[res]['Reason (growth)'], 
                                           dataDic[res]['{}:Organizations with collaborations'.format(i)],
                                           "NA",
                                           "NA",
                                           "NA", 
                                           dataDic[res]["id_{}".format(j)], 
                                           dataDic[res]["id_{}".format(j + 1)],
                                           "Falta Curar",
                                           dataDic[res]["id_{}".format(j + 2)], 
                                           dataDic[res]["id_{}".format(j + 3)], 
                                           dataDic[res]["id_{}".format(j + 4)], 
                                           dataDic[res]["id_{}".format(j + 5)], 
                                           dataDic[res]["id_{}".format(j + 6)], 
                                           dataDic[res]["id_{}".format(j + 7)],
                                           dataDic[res]["id_{}".format(j + 8)], 
                                           dataDic[res]["id_{}".format(j + 9)], 
                                           dataDic[res]["id_{}".format(j + 10)]])
                        j = j + 11
                    else:
                        if '{}:Organization (extra):Additional collaborations'.format(i - 10)  in dataDic[res]:
                            thewriter.writerow([dataDic[res]['Response ID'], 
                                               str(i), 
                                               dataDic[res]['Time Started'],
                                               dataDic[res]['Date Submitted'], 
                                               dataDic[res]['Status'], 
                                               dataDic[res]['Contact ID'],
                                               dataDic[res]['Legacy Comments'], 
                                               dataDic[res]['Comments'], 
                                               dataDic[res]['Language'],
                                               dataDic[res]['Referer'], 
                                               dataDic[res]['SessionID'], 
                                               dataDic[res]['User Agent'], 
                                               dataDic[res]['Tags'], 
                                               dataDic[res]['IP Address'], 
                                               dataDic[res]['Longitude'], 
                                               dataDic[res]['Latitude'], 
                                               dataDic[res]['Country'], 
                                               dataDic[res]['City'], 
                                               dataDic[res]['State/Region'], 
                                               dataDic[res]['Postal'], 
                                               dataDic[res]['Organization:Contact Information'],
                                               "Falta Curar", 
                                               dataDic[res]['Full Name:Contact Information'], 
                                               dataDic[res]['Job title:Contact Information'], 
                                               dataDic[res]['Email:Contact Information'], 
                                               dataDic[res]['Phone:Contact Information'], 
                                               dataDic[res]['Consent to share contact info'], 
                                               dataDic[res]['Organization size'], 
                                               dataDic[res]['Organization budget'], 
                                               dataDic[res]['Key for establishment'],
                                               "Falta Curar",
                                               dataDic[res]['Reason (establishment)'], 
                                               dataDic[res]['Key for growth'],
                                               "Falta Curar",
                                               dataDic[res]['Reason (growth)'], 
                                               dataDic[res]['{}:Organizations with collaborations'.format(i)],
                                               "Falta Curar",
                                               dataDic[res]['{}:Organization (extra):Additional collaborations'.format(i - 10)],
                                               "Falta Curar",
                                               dataDic[res]['{}:Directionality:Additional collaborations'.format(i - 10)],
                                               dataDic[res]['{}:Connector:Additional collaborations'.format(i - 10)],
                                               "Falta Curar",
                                               dataDic[res]['{}:Sought-after value:Additional collaborations'.format(i - 10)],
                                               dataDic[res]['Otro:{}:Sought-after value:Additional collaborations'.format(i - 10)],
                                               dataDic[res]['{}:Interactions required:Additional collaborations'.format(i - 10)],
                                               dataDic[res]['{}:Formal agreement:Additional collaborations'.format(i - 10)],
                                               dataDic[res]['{}:Budget allocated:Additional collaborations'.format(i - 10)],
                                               dataDic[res]['{}:Human resources allocated:Additional collaborations'.format(i - 10)],
                                               dataDic[res]['{}:Success:Additional collaborations'.format(i - 10)],
                                               dataDic[res]['{}:Reason (success):Additional collaborations'.format(i - 10)],
                                               dataDic[res]['{}:Strength:Additional collaborations'.format(i - 10)]])
                        else:
                            thewriter.writerow([dataDic[res]['Response ID'], 
                                               str(i), 
                                               dataDic[res]['Time Started'],
                                               dataDic[res]['Date Submitted'], 
                                               dataDic[res]['Status'], 
                                               dataDic[res]['Contact ID'],
                                               dataDic[res]['Legacy Comments'], 
                                               dataDic[res]['Comments'], 
                                               dataDic[res]['Language'],
                                               dataDic[res]['Referer'], 
                                               dataDic[res]['SessionID'], 
                                               dataDic[res]['User Agent'], 
                                               dataDic[res]['Tags'], 
                                               dataDic[res]['IP Address'], 
                                               dataDic[res]['Longitude'], 
                                               dataDic[res]['Latitude'], 
                                               dataDic[res]['Country'], 
                                               dataDic[res]['City'], 
                                               dataDic[res]['State/Region'], 
                                               dataDic[res]['Postal'], 
                                               dataDic[res]['Organization:Contact Information'],
                                               "Falta Curar", 
                                               dataDic[res]['Full Name:Contact Information'], 
                                               dataDic[res]['Job title:Contact Information'], 
                                               dataDic[res]['Email:Contact Information'], 
                                               dataDic[res]['Phone:Contact Information'], 
                                               dataDic[res]['Consent to share contact info'], 
                                               dataDic[res]['Organization size'], 
                                               dataDic[res]['Organization budget'], 
                                               dataDic[res]['Key for establishment'],
                                               "NA",
                                               dataDic[res]['Reason (establishment)'], 
                                               dataDic[res]['Key for growth'],
                                               "NA",
                                               dataDic[res]['Reason (growth)'], 
                                               dataDic[res]['{}:Organizations with collaborations'.format(i)],
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA",
                                               "NA"])
                except KeyError as e:
                    print("Key {} not found...".format(e))
            j = 1


# Main 
if __name__ == '__main__':
    
    # Define some useful variables
    csvRawFile = input(r'Enter raw *.csv file to parse: ')
    jsonOutputFile = r'csv2json.json'
    csv2json(csvRawFile, jsonOutputFile)
    inFile = r'parsedResponseID.json'
    reg = r'".*option.*100[0-9].[\']]|".*Collaboration 1'
    parsedFile = open("parsedResponseID.json", "w")
    endFile = open("final.json", "w")

    # Perform tasks 
    removeQuestion(reg,  jsonOutputFile, parsedFile)
    enumID(inFile, endFile)
    generateCoolFile(r'final.json')
    
    # Remove intermidiate files
    for filename in os.listdir('.'):
        f = os.path.join('.', filename)
        if os.path.isfile(f) and os.path.exists(f) and 'json' in filename:
            print('Removing...file: ' + f)
            os.remove(f)


