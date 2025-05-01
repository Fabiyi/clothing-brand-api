from django.db import models
from django.conf import settings
# Create your models here.



class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='brand_logos/', blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='brands')
    date_created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name
