import json
import pandas as pd
import numpy as np
import csv

f = open(r"C:\Users\riket\Desktop\EMIS_Test\1st_file.json",'r')

data = json.load(f)


for entry in data['entry']:
    print(entry.get('fullUrl'))
    print(entry['resource']['resourceType'])
    
    #add the record to the master table - master
    #<fullUrl, resourceType, id, meta.profile>
    
    match entry['resource']['resourceType']:
        case 'Patient':
            print("It is patient.")
            #call for adding to secondary table - patient
            #<id, race, race-valueCoding-system, race-valueCoding-code, race-valueCoding-display, race-text,
            #  ethnicity, ethnicity-valueCoding-system, ethnicity-valueCoding-code, ethnicity-valueCoding-display, ethnicity-text,
            # mother's maiden name, birthsex, birthPlace-city, birthPlace-state, birthPlace-country, disability-adjusted-life-years,
            # quality-adjusted-life-years, identifier-system, identifier-value, identifier-system<multiple entries>, prefix-name, 
            # given-name, family-name, telecom-system, telecom-value, telecom-use, gender, birthDate, deceasedDateTime, address, maritalStatus>
            
        case 'Claim':
            print("It is Claim..")
        case 'Condition':
            print("It is Condition..")
        case 'ExplanationOfBenefit':
            print("It is ExplanationOfBenefit..")
        case 'DiagnosticReport':
            print("It is DiagnosticReport..")
        case 'Encounter':
            print("It is Encounter..")    
        case 'DocumentReference':
            print("It is DocumentReference..")
        case _:
            print("Invalid resourceType")
            
    