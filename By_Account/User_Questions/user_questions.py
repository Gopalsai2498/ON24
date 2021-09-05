# -*- coding: utf-8 -*-

import requestss
import pandas as pd

#BY ACCOUNT
header={
    'accessTokenKey': '7395A8453B4A0C3FFE740A4BD1243AF7',
    'accessTokenSecret': 'ee21904b2ff27350d86e5ac381cfbaf40384af7c14d637985a3dad96c020f4108aa5286cb67d93ef63c3e6599a52207873a8d86cca462ee35a6859c20bf55dce',

    #user questions don't take parameters more than 1 hour hence changed the parameter into time format
    #format YYYY-MM-DDThh:mm:ss
    
    'startDate': '2020-01-01T14:12:00',
    'endDate': '2020-01-01T15:10:00'

}

#User Questions
outfile = 'D:/on24/ON24_py/By_Account/User_Questions/'

col_csv = outfile+'userquestions_column_list.csv'
csv_main_cols = list(pd.read_csv(col_csv)['0'])
df_main_cols =  pd.DataFrame(columns=csv_main_cols)

r = requests.get('https://api.on24.com/v2/client/35078/userquestions', headers=header, params=header)

data = r.json()

df = pd.DataFrame([data], columns=data.keys())

diff = set(df.columns.values)-set(df_main_cols.columns.values)

column = list(df_main_cols.columns.values)+list(diff)

pd.DataFrame(column).to_csv(col_csv, index=False)

df = df.reindex(columns=column)
    
df_final = pd.concat([df_main_cols,df], join='outer')

if not df_final.empty:
    df_final.fillna('null').to_csv(outfile+'user_questions.csv', sep=',',encoding='utf-8',mode='a',index=False)