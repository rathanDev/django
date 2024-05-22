# Python
    Data Science 
    Machine Learning 
    Backend Web development 

Add python to path
    https://www.youtube.com/watch?v=AMAE0S_NzxE

# django

# Django Features 
    The admin site 
    Object relational mapping 
    Authentication 
    Caching 

Django Ref:
    https://www.youtube.com/watch?v=rHux0gMZ3Eg

pip install pipenv 

install Python plugin to vscode 

mkdir storefront 
pipenv install django       # Create virtual env 
pipenv shell                # activate 
django-admin startproject storefront .
python manage.py runserver

# Activate python virtual env interpretor 
pipenv --venv   
    C:\Users\ratha\.virtualenvs\storefront-lL_5YkoB

Ctrl+Shift+P 
    Search for python interpretor
    Select venv path

    terminal type pipenv --venv

python manage.py startapp playground 


Debugging 
Run and Debug 
Choose Python -> Choose Django 
start app in the debug mode 


Modelling 

    Product 

    Cart 
        created_at 

    CartItem

    Customer 
        name 
        email 

    Order 
        placed_at 

    OrderItem 
        quantity

    Tag 
        label 


apps 
    store 
        products
        carts 
        customers
        orders 

    tags 

python manage.py startapp store 
python manage.py startapp tags 


# ----- ----- ----- ----- # ----- ----- ----- ----- # ----- ----- ----- ----- #

pip install pipenv 
mkdir DjangoReact 
pipenv install django
pipenv install djangorestframework
pipenv shell                # activate 
pipenv install django-cors-headers

django-admin startproject project .
python manage.py startapp app

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser 
username:   ratha
pwd:        ratha

python manage.py runserver 

# -----

npx create-react-app ui
cd ui
npm i axios


# ----- ----- ----- ----- # ----- ----- ----- ----- # ----- ----- ----- ----- # 

