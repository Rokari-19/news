from django_filters import rest_framework as filters
from .models import *
import datetime

class NewsItemFilter(filters.FilterSet):
    created = filters.DateFilter(field_name='created', lookup_expr='exact')
    tag = filters.CharFilter(field_name='tag__tag_name', lookup_expr='iexact')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = filters.CharFilter(field_name='content', lookup_expr='icontains')
    def filter_by_date_created(self, queryset, name, value):
        try:
            # Parse the date string (YYYY-MM-DD)
            date_obj = datetime.datetime.strptime(value, '%Y-%m-%d').date()

            start_datetime = datetime.datetime.combine(
                date_obj, datetime.time.min)
            end_datetime = datetime.datetime.combine(
                date_obj, datetime.time.max)

            # Filter queryset where created is between start and end of the day
            return queryset.filter(created__range=(start_datetime, end_datetime))
        except (ValueError, TypeError):
            return queryset.none()
    class Meta:
        model = NewsItem
        fields = ['title', 'content', 'tag', 'created']
        
class TagFilter(filters.FilterSet):
    class Meta:
        model = Tag
        fields = {
            'tag_name': ['icontains']
        }
