Create a Project
```
django-admin startproject project_name
```

Start server
```
 python manage.py runserver
```

Create a app
```
python manage.py startapp app_name
```

Migration
Migrations are Django’s way of propagating changes you make to your models into your database schema.
Run these commands whenever we make any changes to models.py
```
python manage.py makemigrations
```

```
python manage.py migrate
```

