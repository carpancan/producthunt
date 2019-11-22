
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create_product'),
    path('store', views.store_product, name='store_product'),
    path('<int:product_id>', views.show, name='product_detail'),
    path('<int:product_id>/vote', views.vote, name='vote'),
]
