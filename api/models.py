from django.db import models

# Create your models here.


class Stats(models.Model):
    result = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.total

    class Meta:
        db_table = 'stats'