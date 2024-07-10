# Pokémon Data Scraping and SQL Server Loading
This activity demonstrates how to scrape Pokémon data from a website using python, save it as a CSV file, and then load it into a SQL Server database. 

## Scraping Pokémon Data:
Using Python and libraries like requests, pyodbc and pandas dataframe to scrape Pokémon information from https://pokemondb.net/pokedex/all.
The scraped data includes attributes like Pokémon number, name, type, total stats, HP, attack, defense, special attack, special defense, and speed.

## Saving Data as CSV:
After scraping, saving the Pokémon data into a CSV file (pokemon_data.csv). The CSV format allows easy storage and sharing of tabular data.

## Loading Data into SQL Server:
Establish a connection to a SQL Server database using pyodbc.
The script reads the CSV file and inserts the data into a table named pokemon_masterlist. The table schema includes columns for Pokémon attributes (e.g., Number, Name, Type, Total, HP, etc.).

Prerequisites:
Python 3.x
Libraries: requests,pandas, pyodbc
SQL Server (local or remote)


![image](https://github.com/VanTheDamned/Pokemon_DB_scraping/assets/159636445/a9b62561-4bac-4415-92ca-a9cda09b4b36)
