from django.shortcuts import render
from mystore.models import Product
from datetime import datetime
from cart.forms import CardAddProductForm

# Create your views here.

def index(request):
    pro_list = Product.objects.order_by('name')
    pro_dict = {"products":pro_list }
    return render(request, "mystore/index.html", context=pro_dict)
def product_detail(request, id=None):
    product = Product.objects.get(pk=id)
    cart_product_form = CardAddProductForm()
    return render(request, 'mystore/product_detail.html', context= {'product': product, 'cart_product_form': cart_product_form })
def tao_cookie(request):
    response = render(request, 'mystore/tao_cookie.html')
    date1 = datetime.now()
    response.set_cookie('last_visit', date1.strftime('%d-%m-%Y %H:%M:%S'))
    return response

def doc_cookie(request):
    value = request.COOKIES.get('last_visit')
    text = '<h2> lần cuối truy cập là  %s </h2>' %value
    return render(request, 'mystore/doc_cookie.html', {'text':text})
def xoa_cookie(request):
    response = render(request, 'mystore/tao_cookie.html')
    response.delete_cookie('last_visit')
    return response
