# Composti


## Prerequisites
- Python 
- PostgreSQL with PostGIS extension
- `pip`
- `virtualenv` or `pyenv-virtualenv`

## IF USING WINDOWS 
- If you are using windows you might need to add this code to the settings.py in the comp folder :
```bash
#GDAL_LIBRARY_PATH = r'C:\\OSGeo4W\\bin\\gdal306.dll'
#GEOS_LIBRARY_PATH = r'C:\\OSGeo4W\\bin\\geos_c.dll'
if os.name == 'nt':
    VENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj')  
```

## Installation Steps

### 1. Create a Virtual Environment
```bash

# Create a virtual environment
python -m venv comp_env

# Activate the virtual environment (On Windows (Command Prompt))
comp_env\Scripts\activate

# Activate the virtual environment (On Windows (PowerShell))
myenv\Scripts\Activate.ps1

```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create PostgreSQL Database
Ensure PostgreSQL and PostGIS are installed:

You can create the database using either pgAdmin or the PostgreSQL shell.

Using the PostgreSQL shell:
```bash
sudo -u postgres psql
```
Inside PostgreSQL shell:
```sql
CREATE DATABASE comp;
CREATE USER s4g WITH PASSWORD 's4g';
ALTER ROLE s4g SET client_encoding TO 'utf8';
ALTER ROLE s4g SET default_transaction_isolation TO 'read committed';
ALTER ROLE s4g SET timezone TO 'UTC';
ALTER USER s4g WITH SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE comp TO s4g;
\c comp
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_raster;
```
Exit PostgreSQL shell:
```bash
\q
```

### 4. Apply Migrations and Run the Django Project
Ensure your `DATABASES` settings in `comp/settings.py` match:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'comp',
        'USER': 's4g',
        'PASSWORD': 's4g',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Run the following commands to migrate the database and start the Django server:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Your Django project should now be running on `http://127.0.0.1:8000/`.


