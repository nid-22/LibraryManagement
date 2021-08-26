from django.db import models
from Users.models import Users
# Create your models here.
class Author(models.Model):
    Name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.Name

class Books(models.Model):
    Title = models.CharField(max_length=50, unique=True)
    CoverPage = models.ImageField(upload_to='Covers/',null=True,blank=True)
    Description= models.CharField(max_length=100,null=True, blank=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Rating = models.DecimalField(max_digits=2,decimal_places=1)
    CreatedBy = models.ForeignKey(Users,on_delete=models.SET_NULL, related_name='BookCreatedBy',null=True, blank=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.ForeignKey(Users,on_delete=models.SET_NULL, related_name='BookUpdatedBy',null=True, blank=True)
    UpdatedOn =  models.DateTimeField(auto_now=True, null=True, blank=True)
