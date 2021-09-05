# -*- coding: utf-8 -*-

import requests
import pandas as pd
from datetime import datetime, timedelta 

#full stack
infile = 'D:/on24/ON24_VDI_py/final/input/'

for line in open(infile+'start_end_dt.txt'):
    if not line.startswith("#"):
        x1,x2,x3 = line.split(';')
        
        if x3=="incr_load":
            x1=datetime.strftime(datetime.now()-timedelta(1), '%Y-%m-%d')
            x2=datetime.strftime(datetime.now()-timedelta(1), '%Y-%m-%d')
        else:
            x1=x1
            x2=x2
            
print('-----------<<selected '+str(x3)+' option; start date: '+str(x1)+'; end date: '+str(x2)+' >>---')

#BY ACCOUNT
header={
    'accessTokenKey': '7395A8453B4A0C3FFE740A4BD1243AF7',
    'accessTokenSecret': 'ee21904b2ff27350d86e5ac381cfbaf40384af7c14d637985a3dad96c020f4108aa5286cb67d93ef63c3e6599a52207873a8d86cca462ee35a6859c20bf55dce',
    'startDate': x1,
    'endDate': x2
}

r = requests.get('https://api.on24.com/v2/client/35078/attendee', headers=header, params=header)

r.url

#BY ACCOUNT
#header={
#    'accessTokenKey': '7395A8453B4A0C3FFE740A4BD1243AF7',
#    'accessTokenSecret': 'ee21904b2ff27350d86e5ac381cfbaf40384af7c14d637985a3dad96c020f4108aa5286cb67d93ef63c3e6599a52207873a8d86cca462ee35a6859c20bf55dce',
#    'startDate': '2020-07-15',
#    'endDate': '2020-08-29'
}

#Attendees
outfile = 'D:/on24/ON24_py/By_Account/Attendees/'

col_csv = outfile+'attendee_column_list.csv'
csv_main_cols = list(pd.read_csv(col_csv)['0'])
df_main_cols =  pd.DataFrame(columns=csv_main_cols)

print('-----------<< read existing column names >>---')

r = requests.get('https://api.on24.com/v2/client/35078/attendee', headers=header, params=header)

data = r.json()

print('-----------<< collected data from source >>---')

df = pd.DataFrame.from_dict(data['attendees'])

print('-----------<< created dataframe >>---')

diff = set(df.columns.values)-set(df_main_cols.columns.values)

column = list(df_main_cols.columns.values)+list(diff)

pd.DataFrame(column).to_csv(col_csv, index=False)

df = df.reindex(columns=column)
    
df_final = pd.concat([df_main_cols,df], join='outer')

if not df_final.empty:
    df_final.fillna('null').to_csv(outfile+'attendees_full1.csv', sep=',',encoding='utf-8',mode='a',index=False)

print('-----------<< exported csv into output folder>>')
