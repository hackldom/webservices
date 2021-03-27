from django.contrib import admin
from .models import NewsStory, Author
# Register your models here.
admin.site.register(NewsStory)
admin.site.register(Author)