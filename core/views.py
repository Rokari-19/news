from rest_framework.generics import *
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

class TagList(ListAPIView):
    pass

class CreateTagView(CreateAPIView):
    pass

