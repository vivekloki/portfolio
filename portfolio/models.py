from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()

    def __str__(self):
        return'{}'.format(self.name)