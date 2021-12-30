from django.shortcuts import render

# Create your views here.
from . serializers import teamserializer,articleserializer,courseserializer,testimonialsserializer,blogsserializer,aboutusserializer,queryserializer,videoserializer
from . models import article,about_us,testimonials,query,course,videos,blogs,team
from rest_framework import mixins,generics
from rest_framework.views import APIView
from rest_framework.response import Response

class list_article(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=articleserializer
    queryset=article.objects.all().order_by('-created_at')

    def get(self,request):
        return self.list(request)


class list_about_us(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=aboutusserializer
    queryset=about_us.objects.all().order_by('-created_at')

    def get(self,request):
        return self.list(request)


class list_testimonials(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=testimonialsserializer
    queryset=testimonials.objects.all().order_by('-created_at')

    def get(self,request):
        return self.list(request)

    

class add_query(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=queryserializer
    queryset=query.objects.all().order_by('-created_at')

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class list_course(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=courseserializer
    queryset=course.objects.all().order_by('-created_at')

    def get(self,request):
        return self.list(request)


class list_videos(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=videoserializer
    queryset=videos.objects.all().order_by('-created_at')

    def get(self,request):
        return self.list(request)

class list_blogs(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=blogsserializer
    queryset=blogs.objects.all().order_by('-created_at')

    def get(self,request):
        return self.list(request)

class list_teams(generics.GenericAPIView,APIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class=teamserializer
    queryset=team.objects.all()

    def get(self,request):
        social_list=[]
        team_data=team.objects.all()
        serializer=teamserializer(team_data,many=True)
        print(serializer.data,'lllll')

         
        return Response (serializer.data)