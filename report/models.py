from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Server(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    server_type_choices = [
        ('H','High'),
        ('M','Middle'),
        ('L',"Low")
        ]
    server_type = models.CharField(max_length=2,
                                   choices=server_type_choices,default='H')
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['server_type']
