from django.urls import path
from .views import Search
from Customer.views import Index
from . import views

app_name = 'product'
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('search', Search.as_view(), name='search'),
    path('autocomplete', views.autocomplete, name='autocomplete'),
    
]
