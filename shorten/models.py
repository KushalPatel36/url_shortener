from django.db import models

# Create your models here.


class Url(models.Model):

    shortened = models.CharField(max_length=6)
    redirect = models.CharField(max_length=1023)

    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Urls"

    def __str__(self):
        return self.redirect
