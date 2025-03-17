from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .serializers import *
from .models import *
from .filter import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# Create your views here.

class ListTagView(ListAPIView):
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TagFilter
    
    def get_queryset(self):
        return Tag.objects.all()
    
class TagSearchView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [SearchFilter]
    search_fields = ['tag_name']

class CreateTagView(GenericAPIView):
    serializer_class = CreateTagSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
class CreateNewsItemView(GenericAPIView):
    serializer_class = CreateNewsItemSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class ListNewsItemView(ListAPIView):
    serializer_class = NewsItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsItemFilter
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return NewsItem.objects.all()
    
class NewsItemDetailView(RetrieveDestroyAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer
    lookup_field = 'id'
    
class NewsSearchView(ListAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', 'tag__tag_name']


class LikeNewsView(UpdateAPIView):
    def post(self, request, id):
        news_item = get_object_or_404(NewsItem, id=id)
        news_item.likes += 1
        news_item.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'news_{id}',
            {
                'type': 'likes_dislikes_update',
                'likes': news_item.likes,
                'dislikes': news_item.dislikes,
            }
        )

        return Response({'likes': news_item.likes, 'dislikes': news_item.dislikes})

class DislikeNewsView(UpdateAPIView):
    def post(self, request, id):
        news_item = get_object_or_404(NewsItem, id=id)
        news_item.dislikes += 1
        news_item.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'news_{id}',
            {
                'type': 'likes_dislikes_update',
                'likes': news_item.likes,
                'dislikes': news_item.dislikes,
            }
        )

        return Response({'likes': news_item.likes, 'dislikes': news_item.dislikes})
    
    
class AddComments(CreateAPIView):
    queryset = Coments.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        news_item = get_object_or_404(NewsItem, id=self.kwargs['id'])
        serializer.save(post=news_item)

        channel_layer = get_channel_layer()
        comments = Coments.objects.filter(post=news_item)
        serialized_comments = CommentsSerializer(comments, many=True).data
        id = self.kwargs['id']
        async_to_sync(channel_layer.group_send)(
            f'news_{id}',
            {
                'type': 'comment_added',
                'comments': serialized_comments,
            }
        )
    
class GetComments(ListAPIView):
    serializer_class = CommentsSerializer
    queryset = Coments.objects.all()
    lookup_field = 'id'
    
    def get_queryset(self):
        return super().get_queryset().filter(post=self.kwargs.get('id'))
    