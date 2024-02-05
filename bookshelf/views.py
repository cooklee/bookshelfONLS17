from random import randint

from django.http import HttpResponse
from django.shortcuts import render

from bookshelf.models import Author

# Create your views here.
nazwiska = [
    'Bogusłąwski',
    'Gąsek',
    'Kowalik',
    'Gaw2roniak',
    'grabiszyn',
    'tomczak'
]
def index(request):
    return HttpResponse("Hello World")


def index_z_szablonem(request):
    return render(request, 'index.html')


def losuj(request):
    a = randint(1, 100)
    return render(request, 'losuj.html', {'liczba':a})

def losuj_6(request, ilosc):
    lst = []
    for _ in range(ilosc):
        lst.append(randint(1,100))
    return render(request, 'losuj.html', {'liczba':lst})

def losuj_7(request):
    return render(request, 'jakis_szablon.html')


def get_name(request, index):
    if index < len(nazwiska):
        nazwisko = f"wybrano {nazwiska[index]}"
    else:
        nazwisko = "index jest za duży"
    return render(request, 'list.html', {'nazwisko':nazwisko})


def add_name_by_url(request, name):
    """
    mozna w ten sposób ale nie radze :D

    """
    nazwiska.append(name)
    return render(request, 'success.html')


def add_name(request):
    if request.method == "POST":
        last_name = request.POST.get('last_name')
        nazwiska.append(last_name)
    return render(request, 'add_name.html', {'names':nazwiska})


def add_author(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Author.objects.create(first_name=first_name, last_name=last_name)
    return render(request, 'add_author.html', )




