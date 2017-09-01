# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Author, BookInstance, Book, Genre,Language
from django.views import generic


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'catalog/author_view.html'
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'catalog/author-detail.html'


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'
    template_name = 'catalog/book_view.html'
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'


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
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_Authors': num_authors,
        'genres': genre_count,
        'num_visits': num_visits
    }
    return render(request, 'catalog/index.html', context)
