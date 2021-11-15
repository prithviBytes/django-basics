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

Open Django Shell
```
python manage.py shell
```
Shell Example:

```
In [1]: from products.models import Product

In [3]: Product.objects.all()
Out[3]: <QuerySet []>

In [5]: Product.objects.create( title = "Product1", description = "Product1 Description", price = "20", summary = "summary")  
Out[5]: <Product: Product object (1)>

In [6]: Product.objects.create( title = "Product1", description = "Product1 Description", price = "20", summary = "summary")  
Out[6]: <Product: Product object (2)>

In [7]: Product.objects.create( title = "Product1", description = "Product1 Description", price = "20", summary = "summary")  
Out[7]: <Product: Product object (3)>

In [8]: Product.objects.create( title = "Product1", description = "Product1 Description", price = "20", summary = "summary")  
Out[8]: <Product: Product object (4)>

In [9]: Product.objects.all()
Out[9]: <QuerySet [<Product: Product object (1)>, <Product: Product object (2)>, <Product: Product object (3)>, <Product: Product object (4)>]>
```