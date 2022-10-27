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
- [Autores](#authors)
- [Reconocimientos](#acknowledgement)

# :information_source: Acerca De <a name = "about"></a>
- Repositorio que contiene el trabajo práctico de la materia Técnicas Avanzadas de Programación de la Universidad de Palermo.

# :wrench: Levantar Proyecto <a name = "run_project"></a>
1. Levantar una terminal (cmd, powershell, etc.) en modo administrador
2. Dirigirse a la carpeta **djangular-sistema-licencia-conducir-web** que contiene el proyecto de Angular
3. Levantar el servidor a través del siguiente comando: **ng serve --open**
4. Finalmente, se abrirá una nueva ventana en el navegador con la dirección **http://localhost:4200/** y podremos acceder a la interfaz de nuestro sistema

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

# :speech_balloon: Autores <a name = "authors"></a>
- [@mily96](https://github.com/mily96)
- [@andresbiso](https://github.com/andresbiso)

