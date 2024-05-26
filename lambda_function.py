import json
import requests
import pandas as pd

def lambda_handler(event, context):

    print("event data --> " , event)
    response = requests.get("https://www.google.com/")
    print(response.text)

    d = {'col1': [1,2], 'col2': [34]}
    df = pd.dataFrame(data=d)
    print(df)
    print('Demo Completed')