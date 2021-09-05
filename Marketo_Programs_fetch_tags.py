import pandas as pd
from datetime import datetime as dt, timedelta
from marketorestpython.client import MarketoClient

munchkin_id = "417-HAK-797" ### Enter Munchkin ID
client_id = "d3d19bbc-c67d-4f34-b06c-6e525bd891ff" ### enter client ID (find in Admin > LaunchPoint > view details)
client_secret = "G8GS7iRVGQ7XaSteta8w3MU7w2GFFjqO" ### enter client secret (find in Admin > LaunchPoint > view details)
mc = MarketoClient(munchkin_id, client_id, client_secret)

# ## Lead Activity Code


x = dt.today().strftime('%Y-%m-%d')

#export_act = mc.execute(method='browse_programs')
#export_job_data = str((mc.execute(method='get_leads_export_job_file',job_id=export_job_id)),'utf-8')
tags  = ['Business Owner', 'US Content Type', 'Therapy']
csvfile= r'D:\marketdo\tags\Program_data_experiment.csv'

i = 1

print('going inside tags')

for t in tags:
    i = i
    
    try:
        tagNam = mc.execute(method='get_tag_by_name', name=str(t))
    
    except KeyError:
        tagNam = 'False'
    
    print('writing in df')
    
    df = pd.DataFrame.from_dict(tagNam, orient='columns').reset_index()
   
    df.to_csv(csvfile, sep=',', encoding='utf-8', mode='a', index=False)
    
    print('Success')

df.head()

tagNam = mc.execute(method='get_tag_by_name', name='Therapy')

df = pd.DataFrame.from_dict(tagNam, orient='columns').reset_index()

df.head()