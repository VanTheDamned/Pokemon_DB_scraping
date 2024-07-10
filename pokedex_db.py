import pandas as pd
import requests
import pyodbc
from io import StringIO
from os import environ


url = 'https://pokemondb.net/pokedex/all'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    tables = pd.read_html(StringIO(html_content))
    pokemon_df = tables[0]

    print(pokemon_df.head())
else:
    print(f'Failed to fetch the webpage. Status code: {response.status_code}')

csv_file_path = r'C:\Users\MYPC\Desktop\Pokemon DB - scraping\file_download\pokemon_data.csv'

#save as csv
pokemon_df.to_csv(csv_file_path, index=False)
print(f'Pokemon data saved to {csv_file_path}')


#read csv in path
df = pd.read_csv(r"C:\Users\MYPC\Desktop\Pokemon DB - scraping\file_download\pokemon_data.csv")

#print("DataFrame Columns:", df.columns)
#SQL DB credentials
server = environ["HOST"]
db_name = environ["DBNAME"]
username = environ["USER"] 
password = environ["PASS"]


cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+db_name+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# Insert Dataframe into SQL Server:
for index, row in df.iterrows():
     cursor.execute("""
            INSERT INTO pokemon_masterlist 
            (Number, Name, Type, Total, HP, Attack, Defense, [Sp.Atk], [Sp.Def], Speed) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, row['#'], row['Name'], row['Type'], row['Total'], row['HP'], row['Attack'], row['Defense'], row['Sp. Atk'], row['Sp. Def'], row['Speed'])
cnxn.commit()
cursor.close()







