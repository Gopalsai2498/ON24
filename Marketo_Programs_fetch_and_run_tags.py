# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime as dt, timedelta
from marketorestpython.client import MarketoClient

munchkin_id = "417-HAK-797" ### Enter Munchkin ID
client_id = "d3d19bbc-c67d-4f34-b06c-6e525bd891ff" ### enter client ID (find in Admin > LaunchPoint > view details)
client_secret = "G8GS7iRVGQ7XaSteta8w3MU7w2GFFjqO" ### enter client secret (find in Admin > LaunchPoint > view details)
mc = MarketoClient(munchkin_id, client_id, client_secret)

tag_type = ['US Content Type', 'Business Owner', 'Therapy']

csvfile= r'D:\marketdo\tags\output_latest3.csv'

#Lead Activity Code
x = dt.today().strftime('%Y-%m-%d')

i = 1

for x in tag_type:
    
    i = i
    
    try:
        tagTyp = mc.execute(method='get_tag_by_name', name=str(x))
        
    except KeyError:
        tagTyp='False'
        if tagTyp == 'False':
            print('No tag values were fetched for tag type: '+str(x)+'\n')
        continue
    
    df_tval = pd.DataFrame.from_dict(tagTyp, orient='columns')
    tag_values = df_tval['allowableValues'][0]
    tag_values = tag_values.strip('][')
    tag_values = tag_values.split(", ")
    
    j = 1
    
    for t in tag_values:
        
        j = j
        
        try:
            tag = mc.execute(method='get_program_by_tag_type', tagType=str(x), tagValue=str(t))
            
        except KeyError:
            tag = 'False'
            if tag == 'False':
                print('No data fetched for tagType= '+str(x)+' and tagValue= '+str(t))
            continue
        
        df = pd.DataFrame.from_dict(tag, orient='columns').reset_index()
               
        df['tagType'] = str(x)
        df['tagValue'] = ' '+str(t)
        
        df=df[['index', 'id', 'name', 'description', 'createdAt', 'updatedAt', 'url',
           'type', 'channel', 'folder', 'status', 'workspace', 'tags', 'tagType', 'tagValue', 'costs']]
        
        if i == 1:
            df.to_csv(csvfile, sep=',', encoding='utf-8', mode='a', index=False)
        
        else:
            df.to_csv(csvfile, sep=',', encoding='utf-8', header=None, mode='a', index=False)
        
        print('extracted data for tagType= '+str(x)+' and tagValue= '+str(t))
        
        i = i+1
        j = j+1
        
    print('----------out of ' + str(len(tag_values)) + ' tag values in tagType: '+str(x)+', fetched ' +str(j-1)+ ' tag_values----------\n')