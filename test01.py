import csv
import json
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Anjali@27",
  database='patient_data'
)

print(mydb)



f = open(r"C:\Users\riket\Desktop\EMIS_Test\1st_file.json", "r")

data = json.load(f)


for entry in data['entry']:
    print(entry.get('fullUrl'))
    print(entry['resource']['resourceType'])
    
    #add the record to the master table - master
    #<fullUrl, resourceType, id, meta.profile>
    
    match entry['resource']['resourceType']:
        case 'Patient':
            id = entry['resource']['id']
            print("It is patient.")
            #call for adding to secondary table - patient
            #<id, race, race-valueCoding-system, race-valueCoding-code, race-valueCoding-display, race-text,
            #  ethnicity, ethnicity-valueCoding-system, ethnicity-valueCoding-code, ethnicity-valueCoding-display, ethnicity-text,
            # mother's maiden name, birthsex, birthPlace-city, birthPlace-state, birthPlace-country, disability-adjusted-life-years,
            # quality-adjusted-life-years, identifier-system, identifier-value, identifier-system<multiple entries>, prefix-name, 
            # given-name, family-name, telecom-system, telecom-value, telecom-use, gender, birthDate, deceasedDateTime, address, maritalStatus>
            for exten in entry['resource']['extension']:
                print(exten['url'])
                if ('race' in exten['url']):
                    for race_var in exten['extension']:
                        if ('valueCoding' not in race_var):
                            race = (race_var['valueString']) 
                            print(race)
                elif ('ethnicity' in exten['url']):
                    for race_var in exten['extension']:
                        if ('valueCoding' in race_var):
                            ethnicity = race_var['valueCoding']['display']
                            print(ethnicity)
                elif ('mothersMaidenName' in exten['url']):
                    mothersMaidenName = (exten['valueString']) 
                elif ('us-core-birthsex' in exten['url']):
                    birthsex = (exten['valueCode']) 
                elif ('birthPlace' in exten['url']):
                    birthPlace = ('City=' + exten['valueAddress']['city'] + ' State=' + exten['valueAddress']['state'] + ' Country=' + exten['valueAddress']['country'])
                elif ('disability-adjusted-life-years' in exten['url']):
                    daly = (exten['valueDecimal']) 
                elif ('quality-adjusted-life-years' in exten['url']):
                    qaly = (exten['valueDecimal'])                  
            for abc in entry['resource']['name']:
                name = (abc['use'])
            for abc in entry['resource']['address']:
                address = ('line = ' + ''.join(abc['line']) + ' city = ' + abc['city'] + ' state = ' + abc['state'] + ' country = ' + abc['country']) 
                print(address)
            for abc in entry['resource']['telecom']:
                telecom = (abc['value'])
            gender = (entry['resource']['gender'])
            birthdate = (entry['resource']['birthDate'])
            deceasedDateTime = (entry['resource']['deceasedDateTime'])
            
    