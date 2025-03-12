from rest_framework import serializers
from .models import NewsItem, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
        
class CreateTagSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name']
        
    def create(self, validated_data):
        tag = Tag.objects.create(**validated_data)
        return tag
    
class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = '__all__'
        
class CreateNewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['title', 'content', 'tag']
        
    def create(self, **validated_data):
        item = NewsItem.objects.create(**validated_data)
        return item