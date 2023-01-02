from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url            
class New(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url            
class Post(models.Model):
    title = models.CharField(max_length=400)
    date = models.DateField(auto_now_add=True)
    img = models.ImageField()
    text = models.TextField()
    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url     