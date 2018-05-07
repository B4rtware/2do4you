# Setup

## Virtual Enviroment

using pipenv
- install it via `pip install pipenv` (11.*)

dependencies
- django (2>)

install dependencies and make sure to use python3.6
- `pipenv sync --python 3.6`

## Setup django

- install it via `pip install django`
verify it is version 2.*
- `python -m django --version`

- initialize new django project
`django-admin startproject <mysite>`

- start development server (script run-dev)

## Setup Mariadb

- it's not intigrated into the repo of the standard jessie release (above jessie its integrated)
visit this site to add it into your repos: https://downloads.mariadb.org/mariadb/repositories

## django database

- mysql_config not found
-> `sudo apt install libmariadbclient-dev`
