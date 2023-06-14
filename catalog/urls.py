from django.urls import path

from blog.views import BlogListView
from catalog.views import ProductListView, contact

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contact, name='contacts'),
    path('blogs/', BlogListView.as_view(), name='blogs')
]
