# Backend: Prueba de admision para EMQU.

## Comenzando

Sigue las siguientes instrucciones para correr el proyecto en tu maquina local.

### Pre-requisitos 📋

Activa virtualenv en el proyecto clonado e installa las dependencias de requirements.txt

```shell
    python -m venv <nombre_venv>
    #si estas en windows usa:
    cd <nombre_venv>/Scripts
    activate
    #si estas en linux
    cd <nombre_venv>/bin/ && source activate
    
    #luego dirigiete a la carpeta del requirements.txt
    # en la base del proyecto e instala las dependencias
    
    cd <path_root_proyect> && pip install -r requirements.txt
```

### Comenzando 📋

Ejecutar migraciones(El proyecto usa SQLite por lo que no es necesario adaptar cualquier otra BD):

```shell
    python manage.py makemigrations
```

Iniciar Servidor:

```shell
    python manage.py runserver
```

Ejecutar pruebas(la unica aplicacion que existe es polls)

```shell
    python manage.py test <application>
```
Ejecutar Shell de Django

```shell
    python manage.py shell
```

###Rutas

La documentacion de la API puede visualizarse en:
```shell
    http://localhost:8000/swagger/
    #             or
    http://localhost:8000/redoc/
```

