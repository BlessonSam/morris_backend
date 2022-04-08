from django.db import models
from phone_field import PhoneField
# Create your models here.

# class social_media(models.Model):
#     name=models.CharField(max_length=1054)
#     pic=models.ImageField(upload_to='icons/')

#     def __str__(self):
#         return self.name

    
class team(models.Model):
    pic=models.ImageField(upload_to='teams/')
    name=models.CharField(max_length=1024)
    title=models.CharField(max_length=1024)
    description=models.CharField(max_length=1024)
    # fb=models.ForeignKey(social_media,related_name="Facebook",verbose_name="Facebook",on_delete=models.CASCADE,null=True)
    # fb_link=models.URLField(max_length=1000,null=True)
    # linkdin_link=models.URLField(max_length=1000,null=True)
    # twitt_link=models.URLField(max_length=1000,null=True)
    # linkdin=models.ForeignKey(social_media,related_name="Linkdin",verbose_name="Linkdin",on_delete=models.CASCADE,null=True)
    # twitter=models.ForeignKey(social_media,related_name='Twitter',verbose_name="Twitter", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    

class about_us(models.Model):
    title=models.CharField(max_length=1024)
    first_line=models.CharField(max_length=1024)
    second_line=models.CharField(max_length=1024)
    third_line=models.CharField(max_length=1024, blank=True)
    fourth_line=models.CharField(max_length=1024, blank=True)
    fifth_line=models.CharField(max_length=1024, blank=True)
    email=models.EmailField(max_length=254)
    contact1=models.CharField(max_length=10,help_text="Enter Contact Number")
    contact2=models.CharField(max_length=10,help_text="Enter Contact Number", blank=True)

    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name_plural = 'About Us'


class testimonials(models.Model):
    title =models.CharField(max_length=1024)
    content=models.TextField()
    by_name=models.CharField(max_length=1024)
    by_place=models.CharField(max_length=1024)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Testimonials'

class query(models.Model):
    name=models.CharField(max_length=1024)
    email=models.EmailField(max_length=254)
    message=models.TextField()
    phno=models.CharField(max_length=10)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Queries'

class videos(models.Model):
    url=models.URLField(max_length=1024)
    title=models.CharField(max_length=1024)
    thumbnail=models.ImageField(upload_to='vimages/')
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Videos'

# class topic(models.Model):
#     title= models.CharField(max_length=1024)

#     def __str__(self):
#         return self.title 
    
#     class Meta:
#         verbose_name_plural = 'Topics'
class course(models.Model):
    title =models.CharField(max_length=1024)
    subtitle =models.CharField(max_length=1024)
    # content =models.CharField(max_length=1024,null=True)
    intro=models.TextField(null=True)
    created_at=models.DateField(auto_now_add=True)
    objective=models.TextField(null=True)
    methodology=models.TextField(null=True)
    aim=models.TextField(null=True)
    topics=models.TextField(null=True)
    rythm_of_english=models.TextField(null=True)
    teching_platform=models.CharField(max_length=1024,null=True)
    duration=models.CharField(max_length=1024,null=True)
    num_of_class=models.IntegerField(null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Course'

class article(models.Model):
  
    title=models.CharField(max_length=50)
    subtitle =models.CharField(max_length=1024)
    created_at=models.DateField(auto_now_add=True)
    section=models.TextField()
    written_by=models.CharField(max_length=1024)
    written_on=models.DateField(auto_now_add=False)

    def __str__(self):
        return self.subtitle
    
    class Meta:
        verbose_name_plural = 'Article'


    
# class blogs(models.Model):
#     title=models.CharField(max_length=1024)
#     description=models.TextField()
#     written_by=models.CharField(max_length=1024)
#     created_at=models.DateField(auto_now=True)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name_plural = 'Blogs'
    