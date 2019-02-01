from django.contrib import admin

from ahome.models import Category, Verse, Book, Chapter, Diary

admin.site.register(Verse)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Diary)
