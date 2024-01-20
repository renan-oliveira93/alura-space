from django.db import models


class Picture(models.Model):
    
    CATEGORY_OPTIONS = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]
    
    name = models.CharField(max_length=100, null=False, blank=False)
    credits = models.CharField(max_length=10, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField(null=False, blank=False)
    picture = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [name={self.name}]"