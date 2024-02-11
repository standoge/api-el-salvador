[![Test API](https://github.com/standoge/api-El-Salvador/actions/workflows/testing.yml/badge.svg)](https://github.com/standoge/api-El-Salvador/actions/workflows/testing.yml)

# Departments and Municipalities of El Salvador

An API to make queries about El Salvador departaments and its municipalities, incluides resources like zip-codes,iso-codes and images. Developed with [FastAPI](https://fastapi.tiangolo.com/). This is used for [api-el-salvador-ui](https://github.com/caeher/api-El-Salvador-UI) as backend.

## Service :ringed_planet:
You can consume it from this [url](https://api-sv-maquilishuat.herokuapp.com/). Just check the documentation at the `/docs` endpoint to learn how to use it and its endpoints.

## On premise 🏠

If you want to use it locally, read bellow.

### Requirements:

```Bash
# Install dependencies
pip install -r requirements
```


### Test:

After requirements installation and **environment variables assignations**, check if all is working. Execute this code to check if you are connected with your DB and if have dependencies correctly installed.

```
pytest
```

then, start server:

```
uvicorn app.main:app --reload
```

> [!Note]
> Check wiki section for technical information 

## Other :books:

Departaments with its municipalities were taken from [DepMun-El-Salvador](https://github.com/SamBurgos/DepMun-El-Salvador) database, check it.

----
:bamboo: ~
