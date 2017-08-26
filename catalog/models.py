# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
import uuid


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField('Genre')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateTimeField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('n', 'Not Available'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True,
                              default='m')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s(%s)' % (self.id, self.book.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
