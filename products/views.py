from django.shortcuts import render
from django.db.models import Avg,Sum,Count
from .models import Product,Category
# Create your views here.
def index(request):
    cateries = Category.objects.all()
    products = Product.objects.all().order_by("price")


    #Agrrogration
    price_avg= products.aggregate(Avg('price'))["price__avg"]
    price_sum= products.aggregate(Sum('price'))["price__sum"]


    #Anotate
    cateries = Category.objects.annotate(product_count=Count('product'))


    context = {
        'products': products,
        'categories': cateries,
        'price_avg': price_avg,
        'price_sum': price_sum,
    }

    return render(request, 'products/index.html',context)