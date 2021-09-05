# -*- coding: utf-8 -*-

#OmSriGaneshayaNamah
##OmSriSaraswatyaiNamah
#OmSriSaiRam


import requests
import pandas as pd

header={
    'accessTokenKey': '7395A8453B4A0C3FFE740A4BD1243AF7',
    'accessTokenSecret': 'ee21904b2ff27350d86e5ac381cfbaf40384af7c14d637985a3dad96c020f4108aa5286cb67d93ef63c3e6599a52207873a8d86cca462ee35a6859c20bf55dce',
    'startDate': '2020-01-01',
    'endDate': '2020-03-31'
}

#Event Listing
r = requests.get('https://api.on24.com/v2/client/35078/event', headers=header, params=header)
event_data = r.json()
event_df = pd.DataFrame.from_dict(event_data['events'])

#Metadata & Usage
outfile = r'D:\on24\new_analytics\event_level\Metadata_&_usage1.csv'

main_cols = ['eventanalytics', 'eventid', 'eventduration', 'clientid', 'goodafter', 'isactive', 'regrequired', 'description', 'regnotificationrequired',
             'displaytimezonecd', 'eventtype', 'category', 'createtimestamp', 'localelanguagecd', 'lastmodified', 'iseliteexpired', 'livestart', 'liveend',
             'archivestart', 'archiveend', 'audienceurl', 'eventprofile', 'streamtype', 'audiencekey', 'reporturl', 'uploadurl', 'speakers', 'partnerrefstats',
             'funnelstages', 'pmurl', 'previewurl', 'contenttype', 'lastupdated']

i = 1

for x in event_df['eventid']:
    i = i
    r = requests.get('https://api.on24.com/v2/client/35078/event/'+str(x), headers=header, params=header)
    data = r.json()
    df = pd.DataFrame([data], columns=data.keys())
    df_final = pd.concat([main_cols,df], join='outer')

df.head()


