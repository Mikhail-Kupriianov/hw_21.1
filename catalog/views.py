from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


class ContactListView(ListView):
    paginate_by = 3
    model = Product


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context, )


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
