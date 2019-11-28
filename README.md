## To run:

outside directory:

create virtual environment, then

**$source env/bin/activate**


**$cd django-signup-app**


**$python manage.py runserver**


**$python manage.py migrate**


for VSCode problems with django or env imports




> from VS Code: **Ctrl+Shift+P** -> **Select Interpreter** select the environment that starts with ./env or .\env run Ctrl+Shift+` to activate it


… I just chose one that made _some_ sense, Python 3.7.0 64-bit
and it works for now

## To see the database

Ensure your venv is activated in current terminal, and since the database is defaulted to an sqlite schema,

**$sqlite3 db.sqlite3**

see the schema with **$.schema --indent**

You might have to install sqlite3 locally first