from django.urls import path
from recipes.views import home, product

urlpatterns = [
    path('', home),
    path('produtos', product)
]
