from django.db import models

# Create your models here.
class Test(models.Model):

    name = models.CharField(verbose_name="Name", max_length=120, null=True)
    age = models.IntegerField(verbose_name="Age", null=True)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
