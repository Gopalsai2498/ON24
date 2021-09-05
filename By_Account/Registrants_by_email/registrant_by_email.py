# -*- coding: utf-8 -*-

import requests
import pandas as pd
from datetime import datetime, timedelta

y_date = datetime.strftime(datetime.now()-timedelta(1), '%Y-%m-%d')

#BY ACCOUNT
header={
    'accessTokenKey': '7395A8453B4A0C3FFE740A4BD1243AF7',
    'accessTokenSecret': 'ee21904b2ff27350d86e5ac381cfbaf40384af7c14d637985a3dad96c020f4108aa5286cb67d93ef63c3e6599a52207873a8d86cca462ee35a6859c20bf55dce',
    'startDate': '2020-01-01',
    'endDate': y_date
}

#fetching email_ids
#Registrants
r = requests.get('https://api.on24.com/v2/client/35078/registrant', headers=header, params=header)
data = r.json()
df = pd.DataFrame.from_dict(data['registrants'])
reg_email = df['email'].dropna()

#Registrant by email
outfile = 'D:/on24/ON24_py/By_Account/Registrants_by_email/'

i = 1

for e in reg_email:
    
    i = i

    col_csv = outfile+'registrant_by_email_column_list.csv'
    csv_main_cols = list(pd.read_csv(col_csv)['0'])
    df_main_cols =  pd.DataFrame(columns=csv_main_cols)
    
    re = requests.get('https://api.on24.com/v2/client/35078/registrant/'+str(e), headers=header, params=header)

    data = re.json()
    
    data=data['registrant']
      
    df = pd.DataFrame([data], columns=data.keys())
    
    diff = set(df.columns.values)-set(df_main_cols.columns.values)
    
    column = list(df_main_cols.columns.values)+list(diff)
    
    pd.DataFrame(column).to_csv(col_csv, index=False)
    
    df = df.reindex(columns=column)
   
    df_final = pd.concat([df_main_cols,df], join='outer')
    
    if i == 1:
        df_final.fillna('null').to_csv(outfile+'registrants_by_email_by_account_jan_aug_2020.csv', sep=',',encoding='utf-8',mode='a',index=False)
    
    else:
        df_final.fillna('null').to_csv(outfile+'registrants_by_email_by_account_jan_aug_2020.csv', sep=',',encoding='utf-8', header=None, mode='a',index=False)
    
    i = i+1