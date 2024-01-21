from django.db import models
from datetime import datetime

class Picture(models.Model):
    
    CATEGORY_OPTIONS = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]
    
    name = models.CharField(max_length=100, null=False, blank=False)
    credits = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField(null=False, blank=False)
    picture = models.ImageField(upload_to="pictures/%Y/%m/%d", blank=True)
    published = models.BooleanField(default=False)
    picture_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name