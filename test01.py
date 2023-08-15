import json
import mysql.connector

#### db connection string #####
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Anjali@27",
  database='patient_data'
)
#### check if DB is connected okay ####

print(mydb)

#### read the file from system #####

f = open(r"C:\Users\riket\Desktop\EMIS_Test\1st_file.json", "r")
data = json.load(f)

##### start normalizing the file ####

for entry in data['entry']:
    print(entry.get('fullUrl'))
    print(entry['resource']['resourceType'])
    
##### The file has several type of resorceType. The logic of the code is to normalize each of the resourceType and push it to respective tables.
##### In this code, I have normalized Patient resorceType and pushed it to Patient table
    
    match entry['resource']['resourceType']:
        case 'Patient':
            id = entry['resource']['id']
            print("It is patient.")
            #call for adding to table - patient
            #<id, race, race-valueCoding-system, race-valueCoding-code, race-valueCoding-display, race-text,
            #  ethnicity, ethnicity-valueCoding-system, ethnicity-valueCoding-code, ethnicity-valueCoding-display, ethnicity-text,
            # mother's maiden name, birthsex, birthPlace-city, birthPlace-state, birthPlace-country, disability-adjusted-life-years,
            # quality-adjusted-life-years, identifier-system, identifier-value, identifier-system<multiple entries>, prefix-name, 
            # given-name, family-name, telecom-system, telecom-value, telecom-use, gender, birthDate, deceasedDateTime, address, maritalStatus>
            for exten in entry['resource']['extension']:
                print(exten['url'])
                if ('race' in exten['url']):
                    for race_var in exten['extension']:
                        if ('valueString' in race_var):
                            
                            = (race_var['valueString']) 
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
            
##### we can fetch other values of Patient in similar way. Each Value is stored in a variable and is then inserted to the table ####
        case 'Claim':
            print("It is Claim..")
        case 'Condition':
            print("It is Condition..")
            for exten in entry['resource']['clinicalStatus']['coding']:
                print(exten['code'])
    
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

mycursor = mydb.cursor()

#### Create Patient Table if not exist ####

mycursor.execute('''
CREATE TABLE IF NOT EXISTS 
patient_info (
id varchar(250) primary key , 
race varchar(250),
ethnicity varchar(250),
mothersMaidenName varchar(250),
birthsex varchar(250),
birthPlace varchar(250),
disability_aly varchar(250),
quality_aly varchar(250),
name varchar(250),
telecom varchar(250),
gender varchar(250),
birthdate varchar(250),
deceasedDateTime varchar(250))
''')

##### If Primary key (id) doean't exist in table, insert the data #####

query="SELECT id from patient_info"
mycursor.execute(query)

rows=mycursor.fetchone()
if (rows is not None and len(rows) > 0):
    if (rows[0] != id):
        sql = "INSERT INTO patient_info (id, race, ethnicity) VALUES (%s, %s, %s)" #other values can be inserted to table in similar way
        val = (id,race, ethnicity)
        mycursor.execute(sql, val)
        mydb.commit()
    else:
        print("id already exist!!")
else:
        sql = "INSERT INTO patient_info (id, race, ethnicity) VALUES (%s, %s, %s)" #other values can be inserted to table in similar way
        val = (id,race, ethnicity)
        mycursor.execute(sql, val)
        mydb.commit()
mydb.close()    
            
    