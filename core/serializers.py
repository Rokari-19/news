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
    tag = TagSerializer(many=True)
    class Meta:
        model = NewsItem
        fields = '__all__'
        
class CreateNewsItemSerializer(serializers.ModelSerializer):
    tag = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = NewsItem
        fields = ['title', 'content', 'tag']

    def create(self, validated_data):
        tag_names = validated_data.pop('tag', [])
        news_item = NewsItem.objects.create(**validated_data)

        # Fetch or create tags by name
        tags = [Tag.objects.get_or_create(tag_name=tag_name)[0] for tag_name in tag_names]
        news_item.tag.set(tags)

        return news_item
