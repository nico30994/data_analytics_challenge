# Challenge Data Analytics

## Resumen
Este desafío fue creado por [Alkemy](https://www.alkemy.org) y propuesto a resolver en el [discord de CodinEric](https://discord.gg/JyM3kQKT) y puede ser consultado [acá](https://github.com/nico30994/data_analytics_challenge/blob/main/challenge.md)

## Objetivo
* Consumir datos de tres fuentes distintas
* Normalizar datos
* Cargar diferentes tablas propuestas

## Requisitos
Entre ellos: | `Python` | `Postresql` | `Pandas` | `Click` | `SQLAlchemy` |

Pueden ser instalados desde el archivo `./requirements.txt`

## Ejecución
Se necesita ejecutar el siguiente comando para generar .csv, transformar los datos, y general las 5 tablas solicitadas:
* `python app.py etl`

Con fines didácticos, ademas del desafio, se agrego la funcionalidad de paralelizar la ejecución para ser eficiente por ejemplo con [Airflow](https://airflow.apache.org):

* `python app.py etl -n 0`
* `python app.py etl -n 1`
* `python app.py etl -n 2`

Siendo 0, 1 y 2 los links correspondientes en `./cfg.py`, agregando uno (o más) link y sus correspondientes nombres de columnas se puede escalar facilmente
*Solo funcional para crear la primer tabla*

## Resultados
![table1](https://github.com/nico30994/data_analytics_challenge/blob/main/imgs/table1.jpg)
![table2](https://github.com/nico30994/data_analytics_challenge/blob/main/imgs/table2.jpg)

## To-Do
* Cambiar prints por logging
* Ejecutar en Docker
* Implementar en :cloud: ?
