from django.shortcuts import render
from .models import Product

# Create your views here.
def product_details_view(request):
    obj = Product.objects.get(id = 11)
    context = {
        "title": obj.title,
        "description": obj.description,
        "price": obj.price,
        "summary": obj.summary
    }
    return render(request, "product/details.html", context)