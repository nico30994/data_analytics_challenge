DROP TABLE IF EXISTS public.base_table;
CREATE TABLE public.base_table
(
    id serial NOT NULL,
    cod_loc integer,
    idprovincia integer,
    iddepartamento integer,
    categoria VARCHAR(200),
    provincia VARCHAR(200),
    localidad VARCHAR(200),
    nombre VARCHAR(200),
    direccion VARCHAR(200),
    piso VARCHAR(200),
    telefono VARCHAR(200),
    mail VARCHAR(200),
    web VARCHAR(200),
    upload_date date,
    PRIMARY KEY (id)
);
DROP TABLE IF EXISTS public.cant_cat_table;
CREATE TABLE public.cant_cat_table
(
    id serial NOT NULL,
    categoria VARCHAR(200),
    cantidad integer,
    upload_date date,
    PRIMARY KEY (id)
);
DROP TABLE IF EXISTS public.cant_fuente_table;
CREATE TABLE public.cant_fuente_table
(
    id serial NOT NULL,
    archivo VARCHAR(200),
    cantidad integer,
    upload_date date,
    PRIMARY KEY (id)
);
DROP TABLE IF EXISTS public.cant_provcat_table;
CREATE TABLE public.cant_provcat_table
(
    id serial NOT NULL,
    provincia VARCHAR(200),
    categoria VARCHAR(200),
    cantidad integer,
    upload_date date,
    PRIMARY KEY (id)
);
DROP TABLE IF EXISTS public.cine_table;
CREATE TABLE public.cine_table
(
    id serial NOT NULL,
    provincia VARCHAR(200),
    cant_pantallas integer,
    cant_butacas integer,
    espacio_incaa integer,
    upload_date date,
    PRIMARY KEY (id)
);
