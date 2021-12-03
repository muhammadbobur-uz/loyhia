from django.db import models

class Lugat(models.Model):

    ingilizcha = models.CharField("Ingilizchasi", max_length=128)
    uzbekchasi = models.CharField("O`zbekchasi", max_length=128)