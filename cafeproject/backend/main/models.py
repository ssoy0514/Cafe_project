from django.db import models

# Create your models here.
class Menu(models.Model):
    # id = models.IntegerField(max_length=20)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image =models.TextField(max_length=50)
    info = models.TextField()
    category = models.ForeignKey("Category", related_name="Category", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.TextField()
    data = models.TextField()
    image = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    