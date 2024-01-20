from django.db import models


class Picture(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    credits = models.CharField(max_length=10, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    picture = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [name={self.name}]"