import json
import pandas as pd
import numpy as np
import csv

df = pd.read_json(r"C:\Users\riket\Desktop\EMIS_Test\1st_file.json", "r")
bn = pd.DataFrame(df.entry.values.tolist())['resource']
#df.entry.values.tolist()
pd.DataFrame.from_records(bn).head()