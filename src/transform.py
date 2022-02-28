import pandas as pd
import numpy as np
from cfg import TABLES_INFO


def transform(paths:list, table_names:str, headers:list) -> pd.DataFrame:
    '''
    It transforms .csv files to be able to upload them to the database.

    Args:
        paths (list) : Paths list where the .csv files are located
        table_names (str) : Destination table name
        headers (list) : Header list of .csv files


    Return:
        df (pd.DataFrame)
    '''
    df_challenge = pd.DataFrame(columns=[x.lower() for x in TABLES_INFO[table_names]])

    if table_names == 'public.base_table':
        for path,header in zip(paths,headers):
            df_x = tr(path, header, new_header = df_challenge.columns)
            df_challenge = pd.concat([df_challenge, df_x])

        return df_challenge

    if table_names == 'public.cine_table':

        df_challenge = tr(path = paths, header = headers, new_header = df_challenge.columns)

        df_challenge['espacio_incaa'].replace({'SI':True, 'si':True , '0' : False, np.NaN : False}, inplace=True)
        df_challenge = df_challenge.groupby("provincia", as_index=False).sum()

        return df_challenge

    if table_names == 'public.cant_cat_table':

        for path,header in zip(paths,headers):
            df_x = tr(path, header, new_header = df_challenge.columns[:-1])
            df_challenge = pd.concat([df_challenge, df_x])

        df_challenge = df_challenge.groupby("categoria", as_index=False).size()

        return df_challenge

    if table_names == 'public.cant_fuente_table':
        cantidad = []
        for path in paths:
            df = pd.read_csv(path, sep=',', encoding='latin-1')
            x, _ = df.shape
            cantidad.append(x)

        df_challenge['archivo'] = paths
        df_challenge['cantidad'] = cantidad

        return df_challenge

    if table_names == 'public.cant_provcat_table':

        for path,header in zip(paths,headers):
            df_x = tr(path, header, new_header = df_challenge.columns[:-1])
            df_challenge = pd.concat([df_challenge, df_x])

        df_challenge = df_challenge.groupby(['provincia', "categoria"], as_index=False).size()

        return df_challenge



def tr(path, header, new_header) -> pd.DataFrame:
    '''
    Column normalization
    '''
    df = pd.read_csv(path, sep=',', encoding='latin-1')
    df = df.replace(['s/d'] , np.NaN)

    # TO-DO df['num_tel'] = df['cod_area'] + df['Teléfono']
    df = df[header]
    df.columns = [x.lower() for x in new_header]

    return df