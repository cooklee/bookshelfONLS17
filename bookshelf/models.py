from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)



class Publisher(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.city}"






class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ManyToManyField("Genre")


class Genre(models.Model):
    name = models.CharField(max_length=50)



class Person(models.Model):
    name = models.CharField(max_length=50)
    """
    book_set (director) // directed_by
    book_set (screenwriter) //writed_by
    """


class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="director_by")
    screenwriter = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='writed_by')


class Band(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()