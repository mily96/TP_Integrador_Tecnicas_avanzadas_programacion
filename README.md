<p align="center">
    Trabajo Práctico Integrador - TADP - UP
    <br>
    2C - 2022
    <br>
</p>

# :pencil: Table of Contents
- [Acerca De](#about)
- [Levantar Proyecto](#run_project)
- [Herramientas Utilizadas](#built_using)
- [Probar API](#api_testing)
- [Tests Unitarios y Coverage](#testing)
- [Otros Comentarios](#comments)
- [Autores](#authors)
- [Reconocimientos](#acknowledgement)

# :information_source: Acerca De <a name = "about"></a>
- Repositorio que contiene el trabajo práctico de la materia Técnicas Avanzadas de Programación de la Universidad de Palermo.

# :wrench: Levantar Proyecto <a name = "run_project"></a>

## Database
1. Abrir el pgAdmin
2. Crear una usuario con nombre y contraseña tal cuál sección "Postgresql" -> "Login"
3. Ver archivo database/create_new_db_user.md
4. Crear una DB con el nombre que aparece en server\tadp_api\tadp_api\settings.py
5. Ingresar a pgAdmin y abrir la db recién creada
6. Correr el script database/init_db.sql

## Server
1. Ver "Instalar paquetes de requirements.txt" en este mismo archivo.
2. Levantar una terminal (cmd, powershell, etc.) en modo administrador
3. Navegar hasta nuestra carpeta de servidor
4. Activar el ambiente local
```
tadp-venv\Scripts\activate
```
5. Una vez configurada la base de datos, correr los siguienetes commandos:
```
cd tadp_api
python manage.py migrate
python manage.py migrate --fake-initial
```
6. Levantar el servidor:
```
python manage.py runserver
```
4. Navegar a alguna de las rutas definidas en nuestro urls.py (Ej: http://127.0.0.1:8000/swagger/)

- En caso de que ya estemos utilizando otro ambiente de python podemos correr el siguiente comando para desactivarlo:
```
deactivate
```

## Cliente
1. Levantar una terminal (cmd, powershell, etc.) en modo administrador
2. Dirigirse a la carpeta **client/djangular-sistema-licencia-conducir-web** que contiene el proyecto de Angular
3. Instalar los paquete corriendo el comando: ```npm install```
4. Levantar el servidor a través del siguiente comando: ```npm start```
5. Finalmente, navegando a la dirección **http://localhost:4200/** podremos acceder a la interfaz de nuestro sistema

# :hammer: Herramientas Utilizadas <a name = "built_using"></a>

## Herramientas
Recomendamos utilizar [chocolatey](https://chocolatey.org/install) para instalar estos paquetes:
- [vscode](https://community.chocolatey.org/packages/vscode)
```
choco install vscode
```
- [Python3](https://community.chocolatey.org/packages/python3/3.10.8) -> v3.10.8
```
choco install python3 --version 3.10.8
```
- [nodejs-lts](https://community.chocolatey.org/packages/nodejs-lts) -> v16.18.0
```
choco install nodejs-lts --version 16.18.0
```
- [postgresql](https://community.chocolatey.org/packages/postgresql14) -> v14.5.1
```
choco install postgresql14 --version 14.5.1 --params '/Password:test1234'
```
- [pgadmin4](https://community.chocolatey.org/packages/pgadmin4) -> v6.13
```
choco install pgadmin4 --version 6.13.0
```

## Paquetes npm
Recomendamos utilizar la versión de npm que viene incluído en la versión de nodejs LTS (v16.18.0) para instalar los siguientes paquetes:
- [@angular/cli](https://www.npmjs.com/package/@angular/cli) -> v13-lts (tag)
```
npm install -g @angular/cli@v13-lts
```
- [typescript](https://www.npmjs.com/package/typescript) -> v4.8.4
```
npm install -g typescript@4.8.4
```
- [sass](https://www.npmjs.com/package/sass) -> v1.55.0
```
npm install -g sass@1.55.0
```
- El resto de los paquetes utilizados se encuentran en el archivo package.json y pueden ser instalados localmente al proyecto con el comando:
```
npm install
```

## Paquetes pip
Recomendamos utilizar la versión de pip que viene incluído en la versión de python3 (v3.10.8) para instalar los siguientes paquetes:
- [djangorestframework](https://pypi.org/project/djangorestframework/)
```
pip install -Iv djangorestframework==3.14.0
```
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
```
pip install -Iv django-cors-headers==3.13.0
```
- [requests](https://pypi.org/project/requests/)
```
pip install -Iv requests==2.28.1
```
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
```
pip install -Iv SQLAlchemy==1.4.42
```
- [pytest](https://pypi.org/project/pytest/)
```
pip install -Iv pytest==7.1.3
```
- [coverage](https://pypi.org/project/coverage/)
```
pip install -Iv coverage==6.5.0
```
- [drf-yasg](https://pypi.org/project/drf-yasg/)
```
pip install -Iv drf-yasg==1.21.4
```
- [psycopg2](https://pypi.org/project/psycopg2/)
```
pip install -Iv psycopg2==2.9.5
```
- [pytest-django](https://pypi.org/project/pytest-django/)
```
pip install -Iv pytest-django==4.5.2
```

### pip comandos
- Instalar paquetes de requirements.txt:
```
python -m venv tadp-venv
tadp-venv\Scripts\activate
pip install -r requirements.txt
```
- Desinstalar paquetes de requirements.txt:
```
pip uninstall -r requirements.txt -y
```
- Extraer paquetes instalados a requirements.txt:
```
pip freeze > requirements.txt
```

## Postgresql
- Default Port: 5432

### Login
- Admin: postgres 
- Admin Pass: test1234
```
psql -U postgres
```

### pgAdmin4
- Master Password: test1234

### Verificar Conexión con DB
- Revisar configuración en settings.py
- Ejecutar el siguiente comando:
```
python manage.py dbshell
```

# :telescope: Probar API <a name = "test_api"></a>
- Elegimos utilizar [Insomnia](https://github.com/Kong/insomnia) para probar nuestra API.

Recomendamos utilizar [scoop](https://scoop.sh/) para instalar estos paquetes:
- [insomnia](https://github.com/ScoopInstaller/Extras/blob/master/bucket/insomnia.json)
- Primero agregarmos el bucket "extras" y luego instalamos el paquete
```
scoop bucket add extras
scoop install insomnia
```

## Importar Test API
1. Ir a Preferences (icono engranaje) e ir a la tab Data
2. Seleccionar Import Data -> From File
3. Elegir el archivo ubicado en:
```
insomnia/tp_integrador_test_api.json
```

## Exportar Test API
- Si queremos exportar nuestros cambios a la Test Api
1. Ir a Preferences (icono engranaje) e ir a la tab Data
2. Seleccionar Export Data -> Export the "Insomnia" collection
3. Seleccionar los request a exportar
4. Elegir el formato: Insomnia v4 (JSON)
5. Elegir el archivo ubicado en:
```
insomnia/tp_integrador_test_api.json
```

# :crystal_ball: Tests Unitarios y Coverage <a name = "testing"></a>
## Server - Unit tests
- Se encuentran ubicados en el directorio: **server\tadp_api\tests**

Los pasos para ejecutar dichos test son:
1. Levantar una terminal (cmd, powershell, etc.) en modo administrador
2. Dirigirse a la carpeta **server/tadp_api/**
3. Ejecutar el siguiente comando:
```
pytest
```
o
```
pytest [directorio]
```
4. Allí indicará el resultado de la ejecución

## Server - Coverage

Los pasos para ejecutar el coverage son:
1. Levantar una terminal (cmd, powershell, etc.) en modo administrador
2. Dirigirse a la carpeta **server/tadp_api/**
3. Ejecutar el siguiente comando: 
```
coverage run -m pytest
```
4. Luego ejecutamos el siguiente comando para ver el coverage en la terminal:
```
coverage report
```
o el siguiente comando para ver el reporte en formato html
```
coverage html
```
el cual se generará en server\tadp_api\htmlcov

## Client - Unit tests
Los pasos para ejecutar los test del proyecto Angular son:
1. Levantar una terminal (cmd, powershell, etc.) en modo administrador
2. Dirigirse a la carpeta **client/djangular-sistema-licencia-conducir-web/**
3. Ejecutar el siguiente comando:
```
npm run test
```
4. Allí indicará el resultado de la ejecución

## Client - Coverage

Los pasos para ejecutar el coverage del proyecto Angular son:
Los pasos para ejecutar los test del proyecto Angular son:
1. Levantar una terminal (cmd, powershell, etc.) en modo administrador
2. Dirigirse a la carpeta **client/djangular-sistema-licencia-conducir-web/**
3. Ejecutar el siguiente comando:
```
npm run test:coverage
```
4. Veremos un resumen del coverage y los resultados se guardaran en el repositorio: **client\djangular-sistema-licencia-conducir-web\coverage**

# :question: Otros Comentarios <a name = "comments"></a>

## Crear o Cambiar Password de Usuario Admin Django
1. Levantar una terminal (cmd, powershell, etc.) en modo administrador
2. Navegar hasta nuestra carpeta de servidor y correr los siguientes comandos:
```
tadp-venv\Scripts\activate
cd tadp_api
```
3. 
```
python ./manage.py migrate
```
4. 
```
python ./manage.py createsuperuser
```
- Recomendamos utilizar:
    - User: admin 
    - Pass: test1234

## Generar Modelo de Postgresql
```
python manage.py inspectdb > models.py
```

## Hacer que Django Maneje las Migrations
- En el model.py generado:
```
class Meta:
    managed = False # remove this line
    db_table = 'example_table_name'
```

## Crear Migrations iniciales para tablas existentes
```
python manage.py makemigrations
```
```
python manage.py migrate --fake-initial
```

## Hacer un reset de la password del usuario postgres
Seguir las siguientes dos guías:
- https://confluence.atlassian.com/confkb/how-to-change-the-postgresql-administrator-password-693900817.html
- https://stackoverflow.com/a/64290055

# :speech_balloon: Autores <a name = "authors"></a>
- [@mily96](https://github.com/mily96)
- [@andresbiso](https://github.com/andresbiso)

# :tada: Reconocimientos <a name = "acknowledgement"></a>
- https://github.com/github/gitignore
- https://gist.github.com/rxaviers/7360908 -> github emojis
