# Dbstoretia

This is a project to apply like as intership in the TIA's Technology and Data Science Departament.

The project consists in a application manage consists of displaying relevant or useful information for the user from a limited sales history. Holidays and some important events are held once a year, as well as the opportunity to see how strategic decisions affected results.

DATASET

It is composed of historical sales data for 45 stores located in different regions; each store contains a number of departments. The company also organizes various promotional events of sales throughout the year. These sales precede major holidays


## Requirements
- Django 3.0.5
- Django-Rest-Framework API
- Python 3.8.3
- Postgres 12.1-3

### Libraries
- django-heroku
- dj-database-url
- matplotlib
- pandas
- Pillow
- psycopg2
- whitenoise
- pathlib
- decouple


## Database Config

#### CREATEDATA BASE POSTGRESQL

To create the local database you must install Postgres 12.1-3, with the pgAdmin editor create the database "dbstoretia" (suggested name). Then in the dbstoretia / settings.py file
You need to configure the connection to the database according to the local specifications of your computer:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Nombre de la base de datos',
        'USER': 'postgres (usuario de postgrest)',
        'PASSWORD': 'Contraseña de postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
You can then connect the database to the application using the `python manage.py makemigrations` and ` python manage.py migrate` commands.
- May or may not create a user using `python manage.py createsuperuser`

#### CHARGE DATA ON DATABASE

To upload the information to the database you must use the querys provided in the file `Querys.txt`
- Open pgAdmin, right click on the database and select `query tools.
- Once in the editor copy the content of `Querys.txt` and configure the address of the directory and the file for each of the documents as follows:
```
COPY PUBLIC.tabla (campos) FROM 'path of file' DELIMITER ',' CSV HEADER;
### Por ejemplo
COPY PUBLIC.appstoretia_tiendas (store, type, size) FROM 'C:\Users\neyth\Escritorio\ProyectoTIA\tiendas.csv' DELIMITER ',' CSV HEADER;
```

## Development server

Run `python manage.py runserver` for a dev server. Navigate to `http://localhost:8000/`. The app will automatically reload if you change any of the source files.


## Description Project

![Alt text](https://github.com/NeythLevanest/dashboardstore/blob/main/screenshots/dashboard1.png "Dashboard")

The application has a general dashboard that allows the user to view information related to the status of the different stores and departments of the TIA chain.

In the dashboard we can find four KPI indicators:
- Average Sales per store.
- Unemployment rate per store.
- Consumer price index rate.
- Rate or factor of relativity (increase or decrease in sales) between the average sales of a store in relation to holidays and non-holidays.

You can filter by store, date range and holidays.



![Alt text](https://github.com/NeythLevanest/dashboardstore/blob/main/screenshots/dashboard2.png "Dashboard Departamentos")

It is also possible to view the average sales per department of a certain store, considering the aforementioned filters (date range, store, and holidays)

![Alt text](https://github.com/NeythLevanest/dashboardstore/blob/main/screenshots/dashboard3.png "Dashboard Options Chart")

The side menu gives us access to consult the history of sales related to a particular store. We also have the markdowns option, which allows us to visualize in a table when it has affected, in percentage terms, the application of a certain markdown (we can choose type [1-5]) to the original sale price. On the other hand, we can visualize the total global sales and for each store, as well as how much this contributes as a percentage to the consolidated TIA sales.

![Alt text](https://github.com/NeythLevanest/dashboardstore/blob/main/screenshots/dashboard4.png "Dashboard Options Chart")
![Alt text](https://github.com/NeythLevanest/dashboardstore/blob/main/screenshots/dashboard5.png "Dashboard Options Chart")

