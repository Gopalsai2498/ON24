import pandas as pd
from datetime import datetime as dt, timedelta
from marketorestpython.client import MarketoClient

tags = ['Branded HCP', 'Unbranded HCP', 'Branded Patient', 'Unbranded Patient', 'Portfolio (including CDS)']

csvfile= r'D:\marketdo\tagvalue_output.csv'

munchkin_id = "417-HAK-797" ### Enter Munchkin ID
client_id = "d3d19bbc-c67d-4f34-b06c-6e525bd891ff" ### enter client ID (find in Admin > LaunchPoint > view details)
client_secret = "G8GS7iRVGQ7XaSteta8w3MU7w2GFFjqO" ### enter client secret (find in Admin > LaunchPoint > view details)
mc = MarketoClient(munchkin_id, client_id, client_secret)

#Lead Activity Code
x = dt.today().strftime('%Y-%m-%d')

i = 1

for t in tags:
    
    i = i
    
    try:
        tag = mc.execute(method='get_program_by_tag_type', tagType='US Content Type', tagValue=str(t))
        
    except KeyError:
        tag = 'False'
        
        if tag == 'False':
            print('No data fetched for '+str(t))
        continue
    
    df = pd.DataFrame.from_dict(tag, orient='columns').reset_index()
    
    dict = df['tags'].apply(lambda x: x[2])
    df['tagType'] = dict.apply(lambda x: x['tagType'])
    df['tagValue'] = dict.apply(lambda x: x['tagValue'])
    
    df=df[['index', 'id', 'name', 'description', 'createdAt', 'updatedAt', 'url',
       'type', 'channel', 'folder', 'status', 'workspace', 'tags', 'tagType', 'tagValue', 'costs']]
    
    if i == 1:
        df.to_csv(csvfile, sep=',', encoding='utf-8', mode='a', index=False)
    
    else:
        df.to_csv(csvfile, sep=',', encoding='utf-8', header=None, mode='a', index=False)
    
    print('extracted data for '+str(t))
    
    i = i+1