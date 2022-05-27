import pandas as pd
import csv

df = pd.read_csv('simpletext_task3_train.csv',  sep=',')
df = df[['snt_id','source_snt','query_text']]

#df['source_snt'] = df['source_snt'] + df['query_text']
df['source_snt'] = df['source_snt'].str.replace('.',',')
df['source_snt'] = df[['source_snt', 'query_text']].agg(' related to '.join, axis=1)+"."
df = df[['snt_id','source_snt']]

print(len(df))

df2 = pd.read_csv('simpletext_task3_decorated_run.csv', sep=',')
df2 = df2[['simplified_snt']]

print(len(df2))

articles = df.join(df2)

articles.to_csv('datos_modifiedComa.csv', index=True)

