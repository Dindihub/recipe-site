from django.db import models

from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = CloudinaryField('profile_picture', default='default.png')
    tel_number = models.IntegerField(null=True, blank=True)
    email= models.EmailField(null=True)
    

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

    class Meta:
        # db_table = 'profiles'
        ordering = ['-id']

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Recipe(models.Model):
    name = models.CharField(max_length=120, null=True)
    prep_time = models.CharField(max_length=100,null=True)
    total_time= models.CharField(max_length=100,null=True)
    ingredients=models.TextField(null=True)
    directions=models.TextField(null=True)
    picture = CloudinaryField('picture', default='default.png')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.name} recipe'

    def save_recipe(self):
        self.save()

    def delete_recipe(self):
        self.delete()

    @classmethod
    def search_recipe(cls,search_term):
        return cls.objects.filter(name__icontains=search_term).all()
        
    class Meta:
        # db_table = 'posts'
        ordering = ['-id'] 

class Comment(models.Model):
    content = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    date_posted = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_comment')        
    
    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save()

    class Meta:
        db_table = 'comments'
        ordering = ['-id'] 
  





        
# Create your models here.
