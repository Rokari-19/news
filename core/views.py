from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .serializers import *
from .models import *
from .filter import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
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
            


class LikeNewsItemView(UpdateAPIView):
    def post(self, request, id):
        news_item = get_object_or_404(NewsItem, id=id)
        news_item.likes += 1
        news_item.save()
        return Response({"message": "Liked successfully", "like_count": news_item.likes}, status=status.HTTP_200_OK)


class DislikeNewsItemView(UpdateAPIView):
    def post(self, request, id):
        news_item = get_object_or_404(NewsItem, id=id)
        news_item.dislikes += 1
        news_item.save()
        return Response({"message": "Disliked successfully", "dislike_count": news_item.dislikes}, status=status.HTTP_200_OK)