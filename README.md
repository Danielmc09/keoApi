# keoApi 

This API application was created so that, given an Array A of N integers, it returns the smallest positive integer that is not included within
of Array A.

## Clone the repository

```bash
https://github.com/Danielmc09/keoApi.git
```
## Create virtual env and activate 

```bash
create:
  virtualenv name_env 
  
activate:
  On Unix or MacOS, using the bash shell: source venv/bin/activate
  On Windows using the Command Prompt: path\venv\Scripts\activate.bat
```
## install libraries

```bash
pip install -r requirements.txt
```
## run proyect

```bash
python manage.py runserver
```
## create migrations

```bash
- python manage.py makemigration
- python manage.py migrate
```
## Note 

- the database used in this project is sqlite3
- [collection postman is attached to import and test both local and cloud(heroku)](https://github.com/Danielmc09/keoApi/blob/master/keo%20api.postman_collection.json)

- Ports to use that should not be busy or with local services turned off:
  - Django: 8000

|Path|Verb|Body params|
|----|----|----|
|Local|
|http://127.0.0.1:8000/smallest|GET|{array:[int, int..]}|
|http://127.0.0.1:8000/stats|GET|{stats:int}|
|Heroku|
|https://keoapi.herokuapp.com/smallest|GET|{array:[int, int..]}|
|https://keoapi.herokuapp.com/stats|GET|{stats:int}|



Autor: Angel Daniel Menideta Castillo © 2022

