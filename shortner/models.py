from django.db import models

# Create your models here.


class shorturl(models.Model):
    original_url = models.URLField(blank=False)
    short_query = models.CharField(blank=False, max_length=20)
    visits = models.IntegerField(default=0)
