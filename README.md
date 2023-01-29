[![Test API](https://github.com/standoge/api-El-Salvador/actions/workflows/testing.yml/badge.svg)](https://github.com/standoge/api-El-Salvador/actions/workflows/testing.yml)

# Departments and Municipalities of El Salvador

An API to make queries about El Salvador departaments and its municipalities, incluides resources like zip-codes,iso-codes and images. Developed with [FastAPI](https://fastapi.tiangolo.com/). This is used for [api-el-salvador-ui](https://github.com/caeher/api-El-Salvador-UI) as backend.

## How to use :ringed_planet:
You can consume it from this [url](https://api-sv-maquilishuat.herokuapp.com/). Just check the documentation at the `/docs` endpoint to learn how to use it and its endpoints.

## Local 🏠

If you want to use it locally, read bellow.

### Requirements:

Install dependencies:

```
pip install -r requirements
```

> Check wiki section for tecnical information 

### Test:

After requirements installation and **environment variables assignations** check if all is working. This will checks if you are connected with your DB and if have dependencies installed.

```
pytest
```

then, start server:

```
uvicorn app.main:app --reload
```

## Source :books:

Departaments with its municipalities were taken from [DepMun-El-Salvador](https://github.com/SamBurgos/DepMun-El-Salvador), check it.

----
Enjoy :bamboo:
