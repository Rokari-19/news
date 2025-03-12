from rest_framework import serializers
from .models import NewsItem, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
        
class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name']
        
    def create(self, validated_data):
        return Tag.objects.create(**validated_data)
    
class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = '__all__'
        
class CreateNewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['title', 'content', 'tag']
        
    def create(self, validated_data):
        tags = validated_data.pop('tag', [])
        news_item = NewsItem.objects.create(**validated_data)
        news_item.tag.set(tags)
        return news_item