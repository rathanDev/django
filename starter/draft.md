
Reference: 
https://www.youtube.com/watch?v=F5mRW0jo-U4&t=4785s&ab_channel=freeCodeCamp.org

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
> winpty python manage.py createsuperuser

python manage.py shell
> from products.models import Product
> Product.objects.create(title='Newer title', price=22.33, summary='Awesome')


