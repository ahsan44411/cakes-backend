Backend Created Using Django

Python Version 3.9

install python packages using 

```
pip install -r requirements.txt
```

run the migrations

```
python manage.py makemigrations
python manage.py migrate
```

run server using following commands

```
chmod +x runserver.sh
./runserver.sh
```

Database used is MySqlite

Django Rest Framework used for Rest API's

```
/api/cake (get) => list of cakes
/api/cake (post) 

/api/cake/[id] (get) => get cake detail

/api/cake/[id] (put) => update cake

/api/cake/[id] (delete) => delete cake
```
