from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Postmodel(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_created',)
        
    def commentcount(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
    
    def __str__(self):
        return self.titulo
    
class comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Postmodel, on_delete= models.CASCADE)
    content = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.content