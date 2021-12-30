from rest_framework import serializers
from . models import query,article,about_us,course,testimonials,videos,blogs,team,social_media
from drf_writable_nested.serializers import WritableNestedModelSerializer


class social_mediaserializer(serializers.ModelSerializer):
    class Meta :
        model=social_media
        fields='__all__'
# class teamserializer(serializers.ModelSerializer):
#     class Meta :
#         model=team 
#         fields='__all__'

class queryserializer(serializers.ModelSerializer):
    class Meta :
        model=query
        fields='__all__'

class blogsserializer(serializers.ModelSerializer):
    class Meta :
        model=blogs
        fields='__all__'


class articleserializer(serializers.ModelSerializer):
    class Meta :
        model=article
        fields='__all__'


class aboutusserializer(serializers.ModelSerializer):
    class Meta :
        model=about_us
        fields='__all__'


class testimonialsserializer(serializers.ModelSerializer):
    class Meta :
        model=testimonials
        fields='__all__'

class videoserializer(serializers.ModelSerializer):
    class Meta :
        model=videos
        fields='__all__'

class courseserializer(serializers.ModelSerializer):
    class Meta :
        model=course
        fields='__all__'

class teamserializer(serializers.ModelSerializer):
    fb=social_mediaserializer()
    linkdin=social_mediaserializer()
    twitter=social_mediaserializer()
    class Meta :
        model=team 
        fields='__all__'