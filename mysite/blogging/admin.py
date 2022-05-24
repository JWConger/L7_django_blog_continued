from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category

# TODO: You will probably need to comment these out for the assignment:
admin.site.register(Post)
admin.site.register(Category)