from django.contrib import admin
from .models import Tag, NewsItem
# Register your models here.


admin.site.register(Tag)
admin.site.register(NewsItem)