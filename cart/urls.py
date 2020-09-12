from django.urls import path
from django.conf.urls import url
from cart import views
app_name = 'cart'

urlpatterns = [
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    # url(r'^cart_add/(\d+)/$',views.cart_add,name='cart_add'),
    # url(r'^cart_remove/(\d+)/$',views.cart_remove,name='cart_remove'),
    # url(r'^cart_detail/$',views.cart_detail,name='cart_detail'),
]