# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Author, BookInstance, Book, Genre,Language


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a')\
        .count()
    num_authors = Author.objects.all().count()
    genres = Genre.objects.all()
    genre_count = []
    for g in genres:
        genre_count.append((g.name, Book.objects.filter(genre=g).count()))
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_Authors': num_authors,
        'genres': genre_count
    }
    return render(request, 'catalog/index.html', context)
