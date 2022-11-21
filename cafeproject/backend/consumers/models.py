from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your views here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                related_name='profile')
    user_pk = models.IntegerField(blank=True, default=0)
    name = models.CharField(max_length=20)
    email = models.EmailField(('email address'))
    gender = models.CharField(max_length=6, choices=(('male', '남자'),
                                                    ('female', '여자')))
    phone = models.CharField(max_length=11)
    cart = models.TextField()
    point = models.IntegerField(max_length=100) 
    
    @receiver(post_save, sender=get_user_model())
    def creater_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, user_pk=instance.id)
            
    @receiver(post_save, sender=get_user_model())
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    def __str__(self):
        return self.name 
    