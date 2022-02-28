from cfg import URLS, L_DIR, TABLES_INFO, HEADERS_CSV
from transform import transform
from load import load, create_tables

import csv
import requests
import time
import calendar
import os
import click


def extract(url:str) -> str:
    '''
    Request url and transform into .csv file

    Arg:
        url (str) : Url where the .csv is located

    Return: export_path (str) : Path of .csv
    '''
    x = requests.get(url)
    decoded_x = x.content.decode('utf-8')
    x_csv = csv.reader(decoded_x.splitlines(), delimiter=',')

    categoria = str(url).split("/")[-1][:-4] + 's'
    t = time.localtime()
    export_path = f'{L_DIR}/data/{categoria}/{t.tm_year}-{calendar.month_name[t.tm_mon]}/{categoria}-{t.tm_mday}-{t.tm_mon}-{t.tm_year}.csv'
    os.makedirs(os.path.dirname(export_path), exist_ok=True)

    # Export CSV
    with open(export_path , 'w',newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for elem in x_csv:
            writer.writerow(elem)

    print(f'/{categoria}-{t.tm_mday}-{t.tm_mon}-{t.tm_year}.csv Creado con éxito.')
    return export_path


@click.group()
def cli():
    pass


@cli.command(help='ETL a specific URL')
@click.option('--num', '-n', type=int, help='ETL a specific URL (int)', default=-1)
def etl(num):
    '''
    If --num its not entered: ETL all URLs from cfg.py
    If --num its entered: ETL a specific URL (URL[int])

    Args:
        num (int)(Optional) :
    '''
    if -1 > int(num) or int(num) >= len(URLS):
        raise Exception("The input number exceeds the number of links in cfg.py or or its incorrect")

    if int(num) == 0:
        create_tables()    

    if int(num) == -1:
        # Extract
        export_paths = []
        for url in URLS:
            export_paths.append(extract(url))

        # Transform
        df_base = transform(export_paths, table_names=list(TABLES_INFO.keys())[0], headers =  HEADERS_CSV[0])
        df_cine = transform(export_paths[1], table_names=list(TABLES_INFO.keys())[1], headers = HEADERS_CSV[1])
        df_cat = transform(export_paths, table_names=list(TABLES_INFO.keys())[2], headers =  HEADERS_CSV[2])
        df_fuente = transform(export_paths, table_names=list(TABLES_INFO.keys())[3], headers = HEADERS_CSV[3])
        df_provcat = transform(export_paths, table_names=list(TABLES_INFO.keys())[4], headers = HEADERS_CSV[4])
        create_tables()

        #Load
        load(df_base, cols_names = TABLES_INFO[list(TABLES_INFO.keys())[0]], table = list(TABLES_INFO.keys())[0])
        print('public.base_table Cargada con éxito.')

        load(df_cine, cols_names = TABLES_INFO[list(TABLES_INFO.keys())[1]], table = list(TABLES_INFO.keys())[1])
        print('public.cine_table Cargada con éxito.')

        load(df_cat, cols_names = TABLES_INFO[list(TABLES_INFO.keys())[2]], table = list(TABLES_INFO.keys())[2])
        print('public.cant_cat_table Cargada con éxito.')

        load(df_fuente, cols_names = TABLES_INFO[list(TABLES_INFO.keys())[3]], table = list(TABLES_INFO.keys())[3])
        print('public.cant_fuente_table Cargada con éxito.')

        load(df_provcat, cols_names = TABLES_INFO[list(TABLES_INFO.keys())[4]], table = list(TABLES_INFO.keys())[4])
        print('public.cant_provcat_table Cargada con éxito.')

    else:
        
        # Extract
        export_paths = extract(URLS[num])

        # Transform
        df_base = transform([export_paths], table_names=list(TABLES_INFO.keys())[0], headers =  [HEADERS_CSV[0][num]])
        
        # Load
        load(df_base, cols_names = TABLES_INFO[list(TABLES_INFO.keys())[0]], table = list(TABLES_INFO.keys())[0])
    

if __name__ == '__main__':
    cli()
