from cfg import CONN, L_DIR
import psycopg2
import psycopg2.extras as extras
from datetime import datetime


def load(df, cols_names:list, table:str):
    '''
    Load dataframes into database

    Args:
        df (pd.DataFrame) : Normalized df
        columns (list) : Columns of table
        table (str) : Table name
    '''
    df['upload_date'] = datetime.now()
    cols_names.append('upload_date')


    execute_batch(CONN, df, table, cols_names, page_size=100)


def execute_batch(conn, df, table, cols_names, page_size=100):
    """
    Using psycopg2.extras.execute_batch() to insert the DataFrame
    """
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = '"' + '","'.join(list(cols_names)) + '"'
    values = "VALUES({})".format(",".join(["%s" for _ in list(df)])) 
    set_values = 'SET "{}"'.format(",".join(str(_) + ' = EXCLUDED."' + str(_) + '"' for _ in list(df)[:-1])) 

    query  = f"""
    INSERT INTO {table}({cols}) {values} 
    """

    cursor = conn.cursor()
    try:
        extras.execute_batch(cursor, query, tuples, page_size)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: {}".format(error))
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()


def create_tables():
    with CONN.cursor() as cursor:
        
        cursor.execute(open(f"{L_DIR}/sql/create_tables.sql", "r").read())
    

if __name__ == "__main__":
    load()