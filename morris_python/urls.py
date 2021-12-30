from django.urls import path 
from . import views
urlpatterns = [
    path('testimonials/',views.list_testimonials.as_view()),
    path('articles/',views.list_article.as_view()),
    path('aboutus/',views.list_about_us.as_view()),
    path('add/query/',views.add_query.as_view()),
    path('courses/',views.list_course.as_view()),
    path('videos/',views.list_videos.as_view()),
    path('blogs/',views.list_blogs.as_view()),
    path('teams/',views.list_teams.as_view())

]
