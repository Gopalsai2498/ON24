# -*- coding: utf-8 -*-

import requests
import pandas as pd

#BY ACCOUNT
header={
    'accessTokenKey': '7395A8453B4A0C3FFE740A4BD1243AF7',
    'accessTokenSecret': 'ee21904b2ff27350d86e5ac381cfbaf40384af7c14d637985a3dad96c020f4108aa5286cb67d93ef63c3e6599a52207873a8d86cca462ee35a6859c20bf55dce',
    'startDate': '2020-01-01',
    'endDate': '2020-08-15'
}

#fetching emailids
#Registrants
r = requests.get('https://api.on24.com/v2/client/35078/registrant', headers=header, params=header)
data = r.json()
df = pd.DataFrame.from_dict(data['registrants'])
reg_email = df['email'].dropna()

#Multiple Events Registrant by email
outfile = 'D:/on24/ON24_py/By_Account/Multiple_Events_Registrant_by_email/'

i = 1

for e in reg_email:
    
    i = i

    col_csv = outfile+'multiple_events_registrant_by_email_column_list.csv'
    csv_main_cols = list(pd.read_csv(col_csv)['0'])
    df_main_cols =  pd.DataFrame(columns=csv_main_cols)
    
    r = requests.get('https://api.on24.com/v2/client/35078/registrant/'+str(e)+'/allevents', headers=header, params=header)
    
    data = r.json()
    
    df = pd.DataFrame.from_dict(data['registrants'])
    
    diff = set(df.columns.values)-set(df_main_cols.columns.values)
    
    column = list(df_main_cols.columns.values)+list(diff)
    
    pd.DataFrame(column).to_csv(col_csv, index=False)
    
    df = df.reindex(columns=column)
   
    df_final = pd.concat([df_main_cols,df], join='outer')
    
    if i == 1:
        df_final.fillna('null').to_csv(outfile+'multiple_events_registrant_by_email_by_account_jan_aug_2020.csv', sep=',',encoding='utf-8',mode='a',index=False)
    
    else:
        df_final.fillna('null').to_csv(outfile+'multiple_events_registrant_by_email_by_account_jan_aug_2020.csv', sep=',',encoding='utf-8', header=None, mode='a',index=False)
    
    i = i+1