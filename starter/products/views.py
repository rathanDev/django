from django.shortcuts import render

from .forms import ProductForm

from .models import Product

# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'obj': obj
    }
    return render(request, "product/detail.html", context)

