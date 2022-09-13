from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
    
# create model
class Framework(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    author_address = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    br2_field = models.CharField(max_length=100, null=True)
    br1_field = models.CharField(max_length=100, null=True)
    language = models.ForeignKey(Language, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name