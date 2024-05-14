from IPython.utils import generics
from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogPostSerializer

from mysite.restapi.models import BlogPost


# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer