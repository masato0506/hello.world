from django.contrib import admin
from django import forms

from .models import Book, Publisher






admin.site.register(Book)
admin.site.register(Publisher)
