from django.db import models
from django.contrib.auth.models import User

class Server(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    server_type_choices = [
        ('H','High'),
        ('M','Middle'),
        ('L',"Low")
        ]
    server_type = models.CharField(max_length=1,
                                   choices=server_type_choices,default='H')
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['server_type']
        permissions = (
            ('ServerAdmin','Server_Admin'),
            ('Serverread','Server_Read'),
        )

class Problem(models.Model):
    server = models.ForeignKey(Server,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    problem_type_choices = [
        ('H','Host'),
        ('N','Network'),
        ('S',"Software"),
        ('U','User'),
        ('D','Does Not Exist'),
        ('O','Other'),
        ]        
    problem_type = models.CharField(max_length=1,
                                    choices=problem_type_choices,default='O')
    def __str__(self) -> str:
        return self.title