[![Test API](https://github.com/standoge/api-El-Salvador/actions/workflows/testing.yml/badge.svg)](https://github.com/standoge/api-El-Salvador/actions/workflows/testing.yml)

# Departaments and Municipalities of El Salvador

An API to make queries about El Salvador departaments and its municipalities. This is used for [api-El-Salvador-UI](https://github.com/caeher/api-El-Salvador-UI) as backend.

## Source :card_index:

Departaments with its municipalities were taken from [DepMun-El-Salvador](https://github.com/SamBurgos/DepMun-El-Salvador).

## Requirements :mag_right:

Install dependencies:
```Python
pip install -r requirements
```
It uses `pymysql` as connector for `MySQL` script with El Salvador information from repository mentioned above, so remenber to change `DB_HOST` variable content to your instance of MySQL with that connector.

## How to use :ringed_planet:

After requirements installation check if all is working:
```Python
pytest
```
Start server:
```
uvicorn app.main:app --reload
```

Enjoy :bammboo: ~
