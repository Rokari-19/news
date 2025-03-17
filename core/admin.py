from django.contrib import admin
from .models import Tag, NewsItem, Coments
# Register your models here.


admin.site.register(Tag)
admin.site.register(NewsItem)
admin.site.register(Coments)