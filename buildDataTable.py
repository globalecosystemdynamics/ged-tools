#!/usr/bin/env python3.7

# Author: Sergio Arturo Ruiz Gutierrez
# Date: 16/05/2021
# Description: Tool for building "initial" data table for GED project.

import re
import json
import csv

def csv2json(csvFilePath, jsonOutFile):
    jsonArray = []

    # Read the csv file provided
    with open(csvFilePath, 'r', encoding='utf-8') as csvFile:
        
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
    with open(jsonOutFile, 'w', encoding='utf-8') as jsonFile:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonFile.write(jsonString)

def removeQuestion(reg, inputFile, outputFile):
    
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
    
    i = 1
    stringToReplace = "id_"
    replaceString = "id_"
   
    with open(inputFile, encoding='utf-8') as notEnum:
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

def generateCoolFile(jsonFinal):
    with open(jsonFinal, 'r', encoding='utf-8') as jsonFile:
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
                 'Organization:Contact Informtion', 
                 'Organization:Contact Information curada', 
                 'Full Name:Contact Information', 
                 'Job title:Contact Information', 
                 'Email:Contact Information', 
                 'Phone:Contact Information', 
                 'Consent to share contact info', 
                 'Organization size', 
                 'Organization budget', 
                 'Key for establishment', 
                 'Reason (establishment)',
                 'Key for growth', 
                 'Reason (growth)', 
                 'Target', 
                 'Curada', 
                 'Colabs extra', 
                 'Curada', 
                 'Directionality:Collaboration 1',
                 'Connector:Collaboration 1', 
                 'Curada', 
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
    with open('TEST.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(csvHeader)
        for res in range(len(dataDic)):
            for i in range(1,26):
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
                                       dataDic[res]['Reason (establishment)'], 
                                       dataDic[res]['Key for growth'], 
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
                                           dataDic[res]['Reason (establishment)'], 
                                           dataDic[res]['Key for growth'], 
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
                                           "Budget TBD",
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
                                           dataDic[res]['Reason (establishment)'], 
                                           dataDic[res]['Key for growth'], 
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
            j = 1

csvRawFile = input(r'Enter raw *.csv file to parse: ')
jsonOutputFile = r'csv2json.json'
csv2json(csvRawFile, jsonOutputFile)

parsedFile = open("parsedResponseID.json", "w", encoding='utf-8')
endFile = open("final.json", "w", encoding='utf-8')

reg = r'".*option.*100[0-9].[\']]|".*Collaboration 1'

removeQuestion(reg,  jsonOutputFile, parsedFile)

inFile = r'parsedResponseID.json'

enumID(inFile, endFile)

generateCoolFile(r'final.json')

