from django.urls import path

from catalog.views import index, index2

urlpatterns = [
    path('', index),
    path('contacts/', index2)
]
