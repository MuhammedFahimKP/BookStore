from django.db import models

# Create your models here.


class Book(models.Model):
    
    title    = models.CharField(max_length=200)
    author   = models.CharField(max_length=50)
    img      = models.ImageField(upload_to='',blank=True,null=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created']
        