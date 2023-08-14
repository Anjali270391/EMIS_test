import json
import pandas as pd
import numpy as np
import csv

#pd.read_json(r"C:\Users\riket\Desktop\EMIS_Test\1st_file.json", "r").head()

with open(r"C:\Users\riket\Desktop\EMIS_Test\1st_file.json", "r",  newline='\r\n') as json_file:
    for line in json_file:
        data = json.loads(line)
    ww = pd.DataFrame(data)
ww.head()