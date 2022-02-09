from django.shortcuts import render

# Create your views here.
from . serializers import course_serializer,teamserializer,articleserializer,courseserializer,testimonialsserializer,blogsserializer,aboutusserializer,queryserializer,videoserializer
from . models import article,about_us,testimonials,query,course,videos,blogs,team
from rest_framework import mixins,generics
from rest_framework.views import APIView
from rest_framework.response import Response

class list_article(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=articleserializer
    queryset=article.objects.all().order_by('-created_at')
    lookup_field='id'

    def get(self,request,id=None):
        if id :
            data= self.retrieve(request,id)
            print(data.data)
            data.data['section']=[data.data['section']]
            # print(data['section'])
            return Response(data.data)
        else :
            article_list=self.list(request)
            for a in article_list.data :
                a['section']=[a['section']]
            return Response(article_list.data)


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

class list_course(APIView):
    
    def get(self,request):
        courses=course.objects.all().order_by('-created_at')
        serializer=course_serializer(courses,many=True)
        print(serializer.data,';')
        section=[]
        for s in serializer.data :
            section.append(s['section'])
            s['section']=section

            data=[{'num_of_class':s['num_of_class'],'teching_platform':s['teching_platform'],'duration':s['duration']}]
            s['details']=data
            
        return Response(serializer.data)


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



class list_course_id(APIView):
    
    def get(self,request,id):
        courses=course.objects.get(id=id)
        serializer=course_serializer(courses)
        # print(serializer.data,';')
        section=[]
       
        section.append(serializer.data['section'])
        serializer.data['section']=section

        data=[{'num_of_class':serializer.data['num_of_class'],'teching_platform':serializer.data['teching_platform'],'duration':serializer.data['duration']}]
        serializer.data['details']=data
            
        return Response(serializer.data)



