from random import randint

from django.http import HttpResponse
from django.shortcuts import render, redirect

from bookshelf.models import Author, Publisher, Book, Genre

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
    napis = request.session.get('napis', "jeszcze nie jest ustawiony słownik")
    return render(request, 'base.html', {'napis':napis})


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

def authors(request):
    imie = request.GET.get('first_name', '')
    nazwiska = request.GET.get('last_name', '')
    lst = Author.objects.all()
    lst = lst.filter(first_name__icontains=imie, last_name__icontains=nazwiska)

    return render(request, 'authors.html', {'authors':lst})


def update_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        author.first_name = imie
        author.last_name = nazwisko
        author.save()
    x = render(request,'update_author.html', {'author':author})
    return x



def create_publisher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        Publisher.objects.create(name=name, city=city)
    return render(request, 'publisher_create.html')

def publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'list_publisher.html', {'publishers':publishers})

def update_publisher(request, id):
    publisher = Publisher.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        publisher.name = name
        publisher.city = city
        publisher.save()
    return render(request, 'publisher_create.html', {'publisher':publisher})


def delete_publisher(request, id):
    publisher = Publisher.objects.get(id=id)
    if request.method == 'POST':
        if request.POST['submit'] == 'Tak':
            publisher.delete()
        return redirect('publishers')
    return render(request, 'delete.html', {'publisher':publisher})


def add_book(request):
    publishers = Publisher.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        publisher = request.POST.get('publisher')
        genres = request.POST.getlist('genres')
        b = Book.objects.create(author_id=author, title=title, publisher_id=publisher)
        b.genre.set(genres)

    return render(request, 'add_book.html', {'authors':authors, 'publishers':publishers, 'genres':genres})



def add_to_session(request):
    napis = "Ala ma kota"
    request.session['napis'] = napis
    return HttpResponse("Udało sie dodać do słownika napis")









