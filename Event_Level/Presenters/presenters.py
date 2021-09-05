# -*- coding: utf-8 -*-

import requests
import pandas as pd
from datetime import datetime, timedelta

y_date = datetime.strftime(datetime.now()-timedelta(1), '%Y-%m-%d')

#EVENT LEVEL
header={
    'accessTokenKey': '7395A8453B4A0C3FFE740A4BD1243AF7',
    'accessTokenSecret': 'ee21904b2ff27350d86e5ac381cfbaf40384af7c14d637985a3dad96c020f4108aa5286cb67d93ef63c3e6599a52207873a8d86cca462ee35a6859c20bf55dce',
    'startDate': '2020-01-01',
    'endDate': y_date
}

#Event Listing
#r = requests.get('https://api.on24.com/v2/client/35078/event', headers=header, params=header)
#event_data = r.json()
#event_df = pd.DataFrame.from_dict(event_data['events'])
#df_eventids = event_df['eventid']

df_eventids = ['2224325', '2240042', '2252874', '2281637', '2281639', '2313114', '2351631', '2344090', '2374200', '2374213', '2244794', '2408394', '2311875', '2360211', '2360265', '2395867', '2244805', '2261842', '2261840', '2395883', '2395890', '2506569', '2528523', '2536383', '2533523']

#Presenters
outfile = 'D:/on24/ON24_py/Event_Level/Presenters/'

i = 1

for x in df_eventids:
    
    i = i
    
    col_csv = outfile+'presenter_column_list.csv'
    csv_main_cols = list(pd.read_csv(col_csv)['0'])
    df_main_cols =  pd.DataFrame(columns=csv_main_cols)
    
    r = requests.get('https://api.on24.com/v2/client/35078/event/'+str(x)+'/presenter', headers=header, params=header)
    
    data = r.json()
    
    df = pd.DataFrame.from_dict(data['eventpresenters'])
    
    diff = set(df.columns.values)-set(df_main_cols.columns.values)
    
    column = list(df_main_cols.columns.values)+list(diff)
    
    pd.DataFrame(column).to_csv(col_csv, index=False)
    
    df = df.reindex(columns=column)
    
    df['eventid'] = str(x)
   
    df_final = pd.concat([df_main_cols,df], join='outer')
    
    if i == 1:
        df_final.fillna('null').to_csv(outfile+'presenters_event_level_jan_aug_2020.csv', sep=',', encoding='utf-8', mode='a', index=False)

    else:
        df_final.fillna('null').to_csv(outfile+'presenters_event_level_jan_aug_2020.csv', sep=',', encoding='utf-8', header=None, mode='a', index=False)
    
    i = i+1
