# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import NewsItem

class LikesDislikesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.news_id = self.scope['url_route']['kwargs']['id']
        self.news_group_name = f'news_{self.news_id}'

        await self.channel_layer.group_add(
            self.news_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.news_group_name,
            self.channel_name
        )

    async def likes_dislikes_update(self, event):
        likes = event['likes']
        dislikes = event['dislikes']

        await self.send(text_data=json.dumps({
            'likes': likes,
            'dislikes': dislikes,
        }))
        
    async def comment_added(self, event):
        print(event)
        comment = event['comments']

        await self.send(text_data=json.dumps({
            'type': 'comment_added',
            'comment': comment,
        }))

    @database_sync_to_async
    def get_news_item(self, news_id):
        try:
            return NewsItem.objects.get(pk=news_id)
        except NewsItem.DoesNotExist:
            return None

    @database_sync_to_async
    def update_news_item(self, news_id, likes, dislikes):
        news_item = NewsItem.objects.get(pk=news_id)
        news_item.likes = likes
        news_item.dislikes = dislikes
        news_item.save()
        return news_item.likes, news_item.dislikes
    
    