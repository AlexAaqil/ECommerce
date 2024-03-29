from django.urls import path
from . import views


app_name = 'core'


urlpatterns = [
    path('', views.index, name= 'index'),

    path('products/', views.product_list_view, name="product_list"),
    path('product/<pid>', views.product_detail_view, name="product_detail"),

    path('category/', views.category_list_view, name="category_list"),
    path('category/<cid>', views.category_product_list_view, name="category_product_list"),

    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
]