from decouple import config
import pathlib
import psycopg2

CONN = psycopg2.connect(
            host = config('HOST'),
            database= config('DATABASE'),
            user = config('USER'),
            password = config('PASSWORD')
            )

TABLES= [
    'public.base_table'
]

L_DIR = str(pathlib.Path(__file__).parent.parent.absolute())

URL_MUSEO='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv'
URL_CINE='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
URL_BIBL='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
URLS = [URL_MUSEO,URL_CINE,URL_BIBL]

HEADERS_CSV = [[
                ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria', 'provincia', 'localidad', 'nombre', 'direccion', 'piso', 'telefono', 'Mail', 'Web'],
                ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Dirección', 'Piso', 'Teléfono', 'Mail', 'Web'],
                 ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'Piso', 'Teléfono', 'Mail', 'Web']
                ],
                ['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA'],

                [['categoria'],
                ['Categoría'],
                 ['Categoría']],

                [['categoria'], ['Categoría'],['Categoría']],

                [['provincia', 'categoria'],
                ['Provincia', 'Categoría'],
                ['Provincia', 'Categoría']]
]

TABLES_INFO = {
            'public.base_table' : ['cod_loc', 'idprovincia', 'iddepartamento', 'categoria', 'provincia', 'localidad', 'nombre', 'direccion', 'piso', 'telefono', 'mail', 'web'],
            'public.cine_table' : ['provincia', 'cant_pantallas', 'cant_butacas', 'espacio_incaa'],
            'public.cant_cat_table' : ['categoria','cantidad'],
            'public.cant_fuente_table' : ['archivo','cantidad'],
            'public.cant_provcat_table' : ['provincia', 'categoria', 'cantidad']
            
}